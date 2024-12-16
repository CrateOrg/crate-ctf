#!/bin/bash

service ssh start

sudo -u flagholder bash -c 'eval "$(ssh-agent)" ssh-add /home/flagholder/.ssh/id_ed25519 && ssh-add -L && ssh -o StrictHostKeyChecking=no -n -f -A chall@127.0.0.1 vim' &
sleep 1 # This seems to be required
