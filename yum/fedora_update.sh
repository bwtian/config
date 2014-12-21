#!/bin/sh
sudo yum update
sudo yum upgrade
su -c 'yum localinstall --nogpgcheck http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm'
sudo yum update
sudo yum install -y leafpad
sudo yum install -y liveusb-creator
sudo yum install -y emacs
sudo yum install -y R
sudo yum install -y qgis
sudo yum install -y libreoffice-base,libreoffice-writer,libreoffice-impress
sudo yum install -y stardict,goldendict
sudo yum install -y dkms
