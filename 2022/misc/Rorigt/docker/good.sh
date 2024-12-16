# This is the benign version of the script, which should mean that you are viewing
# its source instead of piping it to bash. Good job!
# You should always download and examine a script before running it!

echo Welcome to the Crate CTF flag decryption service!
flag="pengrpgs{phey_gb_onfu_rirelguvat_zvtug_penfu}"
alphabet=abcdefghijklmnopqrstuvwxyz
rot=13

echo "Decrypting flag: ${flag}"
echo ""

sleep 2

for i in $(shuf -i 0-$((${#flag}))); do
    echo $flag

    flag_char=$(echo ${flag:i:1} | sed "y/${alphabet}/${alphabet:$rot}${alphabet::$rot}/")
    flag="$(echo $flag | sed "s/\(.\{$i\}\).\(.*\)/\1$flag_char\2/")"
    sleep 0.1
    printf '\e[A\e[K'

done
echo $flag
