ip=${1//[^0-9.]/}
dns=${2//[^a-zA-Z0-9.]/}
port=${3//[^0-9]/}
res="$(timeout 10 dig +tcp -p $port -x $ip @$dns| grep PTR | awk '{print $5}')"
n=$(grep -c $ip /etc/hosts)
if [[ -z $res ]]; then
    exit
fi
if [[ $n -eq 0 ]]; then
    echo $ip ${res:0:-1} >> /etc/hosts
else
    sed "s/.*\(${ip}.*$\)/$(echo $ip ${res:0:-1})/" /etc/hosts > /etc/hosts.bak
    mv /etc/hosts.bak /etc/hosts
fi
