package database

import (
	"context"
	"os"
	"time"

	"github.com/google/uuid"
	"github.com/redis/go-redis/v9"
)

var rdb *redis.Client

func Init() error {
	opts, err := redis.ParseURL(os.Getenv("REDIS_URL"))
	if err != nil {
		return err
	}
	rdb = redis.NewClient(opts)
	return rdb.Ping(context.Background()).Err()
}

// CreateUser attempts to create a user with the given username and password hash. If the username
// is already taken, no user is created and false is returned. Otherwise true is returned.
func CreateUser(ctx context.Context, username string, hash []byte) (bool, error) {
	didSet, err := rdb.SetNX(ctx, "password:"+username, hash, 0).Result()
	if err != nil {
		return false, err
	}
	return didSet, err
}

// GetHash returns the password hash for a given username. If no such user exists, nil is returned.
func GetHash(ctx context.Context, username string) ([]byte, error) {
	hash, err := rdb.Get(ctx, "password:"+username).Bytes()
	if err == redis.Nil {
		return nil, nil
	}
	if err != nil {
		return nil, err
	}
	return hash, nil
}

func CreateSession(ctx context.Context, sessionID uuid.UUID, username string) error {
	return rdb.Set(ctx, "session:"+sessionID.String(), username, time.Minute*10).Err()
}

// GetSession returns the username associated with the sessionID. If none is, the empty string is
// returned.
func GetSession(ctx context.Context, sessionID uuid.UUID) (string, error) {
	username, err := rdb.GetEx(ctx, "session:"+sessionID.String(), time.Minute*10).Result()
	if err == redis.Nil {
		return "", nil
	}
	if err != nil {
		return "", err
	}
	return username, nil
}
