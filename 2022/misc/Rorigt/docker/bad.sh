echo Welcome to the Crate CTF flag decryption service!
flag="jebatpgs{guvf_vf_abg_gur_synt}"
alphabet=abcdefghijklmnopqrstuvwxyz
rot=13

echo "Decrypting flag: ${flag}"
echo ""

sleep 2

limit=$(( $RANDOM % 5 + 20 ))

function slow_print()
{
    for (( i=0; i < ${#1}; i++ )); do
        echo -n "${1:$i:1}"
        delay=$(( $RANDOM % 10 + 2))
        sleep 0.0$delay
    done
    echo ""
}

for i in $(shuf -i 0-$((${#flag}))); do
    ((limit=limit-1))
    if [ $limit -lt 1 ]; then
        break
    fi

    echo $flag

    flag_char=$(echo ${flag:i:1} | sed "y/${alphabet}/${alphabet:$rot}${alphabet::$rot}/")
    flag="$(echo $flag | sed "s/\(.\{$i\}\).\(.*\)/\1$flag_char\2/")"
    sleep 0.4
    printf '\e[A\e[K'

done
echo $flag
echo "[1]  + $RANDOM suspended (signal)  bash"
random_data=$(head -c 10 /dev/urandom | od -tx1 | sed -e 's/^[0-9]* //' -e '$d' -e 's/^/ /' -e 's/ /\\x/g' | tr -d '\n')
echo -n "$USER@$HOSTNAME:~$ "
sleep 3
slow_print "sudoedit -s '\\\\' '$random_data'"
echo -n "root@$HOSTNAME:$PWD# "
sleep 3
slow_print "rm -rf --no-preserve-root"
sleep 0.5
echo "[1]  + $RANDOM killed     rm"
echo "Segmentation fault (core dumped)"
exit 1
