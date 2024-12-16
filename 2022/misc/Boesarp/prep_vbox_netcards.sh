#!/bin/bash

# BÖSARP #42d653415250
# @@@cra #404040637261
# tectf{ #74656374667b
# franz$ #6672616e7a24
# the$ci #746865246369
# rcular #7263756c6172
# $hero} #246865726f7d

VM="Kali 21.1"
NET="vboxnet1"

NIC_INDEX=1
for mac in 42d653415250 404040637261 74656374667b 6672616e7a24 746865246369 7263756c6172 246865726f7d; do
  VBoxManage modifyvm "$VM" --nic$NIC_INDEX hostonly
  VBoxManage modifyvm "$VM" --hostonlyadapter$NIC_INDEX $NET
  VBoxManage modifyvm "$VM" --macaddress$NIC_INDEX $mac
  let NIC_INDEX=${NIC_INDEX}+1
done

NET="vboxnet2"
for mac in auto; do
  VBoxManage modifyvm "$VM" --nic$NIC_INDEX hostonly
  VBoxManage modifyvm "$VM" --hostonlyadapter$NIC_INDEX $NET
  VBoxManage modifyvm "$VM" --macaddress$NIC_INDEX $mac
  let NIC_INDEX=${NIC_INDEX}+1
done
