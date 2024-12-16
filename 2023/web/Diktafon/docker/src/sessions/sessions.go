package sessions

import (
	"context"
	"crypto/sha256"
	"net/http"

	"challs.crate.nu/diktafon/database"
	"github.com/google/uuid"
)

type sessionHandler struct {
	inner http.Handler
}

func New(inner http.Handler) http.Handler {
	return &sessionHandler{inner}
}

func TrackingSessionID(r *http.Request) uuid.UUID {
	id, _ := r.Context().Value(trackingSessionKey{}).(uuid.UUID)
	return id
}

func LoggedInUser(ctx context.Context) string {
	username, _ := ctx.Value(loginSessionKey{}).(string)
	return username
}

func LogInAs(ctx context.Context, w http.ResponseWriter, username string) error {
	loginSessionID := uuid.New()
	if err := database.CreateSession(ctx, loginSessionID, username); err != nil {
		return err
	}
	http.SetCookie(w, &http.Cookie{
		Name:     "login-session",
		Value:    loginSessionID.String(),
		HttpOnly: true,
		SameSite: http.SameSiteLaxMode,
	})
	return nil
}

func (s *sessionHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	cookie, _ := r.Cookie("tracking-session")
	var trackingSessionID uuid.UUID
	if cookie != nil {
		trackingSessionID, _ = uuid.Parse(cookie.Value)
	} else {
		trackingSessionID = uuid.Must(uuid.NewRandom())
		http.SetCookie(w, &http.Cookie{
			Name:     "tracking-session",
			Value:    trackingSessionID.String(),
			HttpOnly: true,
			SameSite: http.SameSiteLaxMode,
		})
	}
	ctx := r.Context()
	if trackingSessionID != uuid.Nil {
		hash := sha256.Sum256(trackingSessionID[:])
		copy(trackingSessionID[:], hash[:])
		ctx = context.WithValue(ctx, trackingSessionKey{}, trackingSessionID)
	}

	cookie, _ = r.Cookie("login-session")
	if cookie != nil {
		loginSessionID, err := uuid.Parse(cookie.Value)
		if err == nil {
			username, _ := database.GetSession(ctx, loginSessionID)
			if username != "" {
				ctx = context.WithValue(ctx, loginSessionKey{}, username)
			}
		}
	}

	r = r.WithContext(ctx)
	s.inner.ServeHTTP(w, r)
}

type loginSessionKey struct{}
type trackingSessionKey struct{}
