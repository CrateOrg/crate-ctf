package main

import (
	"context"
	"log/slog"
	"net/http"

	"challs.crate.nu/diktafon/sessions"
)

type loggerHandler struct {
	inner http.Handler
}

func WithLogger(inner http.Handler) http.Handler {
	return &loggerHandler{inner}
}

// ServeHTTP implements http.Handler.
func (h *loggerHandler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	log := slog.With("session-id", sessions.TrackingSessionID(r))
	log.Info("Handling request", "path", r.URL.Path, "method", r.Method)

	h.inner.ServeHTTP(w, r.WithContext(context.WithValue(r.Context(), loggerKey{}, log)))
}

type loggerKey struct{}

func GetLogger(ctx context.Context) *slog.Logger {
	return ctx.Value(loggerKey{}).(*slog.Logger)
}
