#!/bin/sh
sudo apt-get install samba -y
sudo apt-get install nautilus-share
sudo groupadd sambashare
sudo adduser `whoami` sambashare
sudo smbpasswd -a `whoami`
sudo gedit /etc/samba/smbusers
smbpasswd t
