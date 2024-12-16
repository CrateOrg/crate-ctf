set -m
/root/.foundry/bin/anvil --block-time 1 --balance 100000000000000000 --host 0.0.0.0 --mnemonic "barrel detail defense baby hair breeze cactus split virtual drum list usage shove aspect disorder version execute flip photo season spatial banner mention together" &
cd /home/ctf/src
TEMP=$(python3 build.py | grep address | awk '{print $5}') 
sed "s/FACTORYADDRESS/${TEMP}/" FactoryInteraction.py | tee Factory.py
fg %1