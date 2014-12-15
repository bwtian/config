#!/bin/bash
# created on 20110509
# alias uu='source ~/Dropbox/config/deb/0_update.deb.sh' in .bash_aliases
# ln -s ~/Dropbox/config/bash/.bash_aliases ~/.bash_aliases
# latest_update: <2013-02-21 Thu>
sudo rm /var/lib/apt/lists/lock

sudo apt-get autoremove -y
sudo aptitude remove -y
sudo aptitude autoclean -y
sudo aptitude clean -y

sudo apt-get update -y
sudo aptitude update -y
sudo apt-get upgrade -y
sudo aptitude dist-upgrade -y
sudo aptitude safe-upgrade -y
sudo apt-get install -f
sudo aptitude install -f


sudo apt-get install apt-file -y
apt-file update


sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 



echo "Update was Finished"
echo "$(date)"
# Show some info
uname -a
lsb_release -a
lsblk
df -lh
# Upgrade to a new Release
#sudo update-manager -d
# sudo do-release-upgrade -d
