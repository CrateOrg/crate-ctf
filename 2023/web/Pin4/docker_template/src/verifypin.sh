authData="wJrl9eDEHW21MDptlgDXxXxOSbNF3VS4UD9TcaJe"
pin="5728175662871847216237"
if [ $1 = $pin ]; then
  echo -n $authData
  exit 0
fi
exit 1
