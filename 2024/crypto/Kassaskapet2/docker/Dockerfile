FROM gcc:bookworm

ENV DEBIAN_FRONTEND noninteractive

# Dependencies
RUN apt-get update --fix-missing && apt-get -y upgrade && rm -rf /var/lib/apt/lists/*

# Dependencies
RUN apt-get update && apt-get install -y python3 python3-pip xinetd supervisor locales && rm -rf /var/lib/apt/lists/*

# Set the locale
RUN sed -i '/en_US.UTF-8/s/^# //g' /etc/locale.gen && locale-gen
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8

# CTF user account
RUN groupadd -r ctf && useradd -r -g ctf ctf
# Add Resources
COPY ctf.xinetd /etc/xinetd.d/ctf
COPY src /home/ctf/src

# Permissions
RUN chown -R root:ctf /home/ctf
RUN chmod -R 775 /home/ctf
#supervisord
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Set up the local chain
RUN curl -L https://foundry.paradigm.xyz | bash
RUN $HOME/.foundry/bin/foundryup
RUN pip install --break-system-packages web3 py-solc-x
# CMD $HOME/.foundry/bin/anvil --block-time 1 --balance 100000000000000000 --host 0.0.0.0 --mnemonic "barrel detail defense baby hair breeze cactus split virtual drum list usage shove aspect disorder version execute flip photo season spatial banner mention together" & \
# TEMP=$(python3 build.py | grep address | awk '{print $5}') && sed "s/FACTORYADDRESS/${TEMP}/" FactoryInteraction.py | tee Factory.py && /usr/sbin/xinetd -dontfork
#CMD bash /home/ctf/src/start.sh
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
