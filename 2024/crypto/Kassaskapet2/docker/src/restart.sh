while true; do
    t="$(date | awk '{print $4 $5}')"
    if [[ "$t" == "11:00:00PM" ]]; then
        pid="$( ps aux | grep anvil | grep -v grep | awk '{print $2}')"
        echo "Killing proccess" $pid "at" $t 
        kill -9 $pid
        rm -r /root/.foundry/anvil/tmp/*
    fi
    sleep 1
done