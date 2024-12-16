# JWT site haxx

A simple php backend that uses JWT with a dictionary (rockyou.txt) secret.

## Backend

PHP logging in with static users, zeke and admin. Admin has a long and complex complex password.
The only thing visible after logging in is the curernt username and a text, for zeke something like "no flags to show".

Crack the JWT password and re-sign the token with admin as scope instead, and the page shows the flag.

Using adhocore/jwt composer lib for JWT-functionality in php.


