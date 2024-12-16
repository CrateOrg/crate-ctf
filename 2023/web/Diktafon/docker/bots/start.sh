#!/usr/bin/env bash

echo Started bot runner

while [ true ]; do
    sleep $(( 1200 + "$RANDOM" % 300 )) # 20 till 25 minuter
    echo Running Login Mixup for admin
    node ./bots/loginMixup.mjs admin "$FLAG"
done &

while [ true ]; do
    sleep $(( 900 + "$RANDOM" % 300 )) # 15 till 20 minuter
    echo Running Login Mixup for badmin

    if [ -z "$badminpw" ]; then
        badminpw="$RANDOM$RANDOM"
        node ./bots/register.mjs badmin "$badminpw"
    fi

    node ./bots/loginMixup.mjs badmin "$badminpw"
done &

while [ true ]; do
    sleep $(( 60 + "$RANDOM" % 480 )) # 1 till 9 minuter
    echo Running Fake Login mixup for admin
    node ./bots/loginMixup.mjs admin "alsonottheflag"
done &

for i in $(seq 1 5); do
    username="alfred.$i.nobel"
    pw="$RANDOM$RANDOM"

    echo Registering account "$username"

    node ./bots/register.mjs "$username" "$pw"

    sleep $(( 10 + "$RANDOM" % 30 ))

    while [ true ]; do
        echo Reading some poems as account "$username"

        node ./bots/readSomePoems.mjs "$username" "$pw"

        sleep $(( 60 + "$RANDOM" % 300 )) # 1 till 6 minuter
    done &
done &

wait
