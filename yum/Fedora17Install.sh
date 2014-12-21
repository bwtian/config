# Set up Proxy for XFCE: failed
sudo echo http_proxy=http://proxy.kuins.net:8080 >>/etc/environment
sudo echo ftp_proxy=http://proxy.kuins.net:8080 >>/etc/environment
sudo echo https_proxy=http://proxy.kuins.net:8080 >>/etc/environment

# Change to Gnome Version

# Proxy
# Set up Proxy in network-proxy,Firefox
# Set up Proxy Globaly in etc/yum.conf
proxy=http://proxy.kuins.net:8080
proxy_usrname=ID
proxy_password=passwd

# Other methods
# Set as once
export http_proxy=http://ID:passwd@proxy:port/
# /etc/profile.d/proxy.sh
export http_proxy=http://ID:passwd@proxy:port/
export ftp_proxy=http://ID:passwd@proxy:port/
export FTP_PROXY=http://ID:passwd@proxy:port/
export HTTP_PROXY=http://ID:passwd@proxy:port/
# /etc/profile.d/proxy.csh
setenv http_proxy=http://ID:passwd@proxy:port/
setenv ftp_proxy=http://ID:passwd@proxy:port/
setenv FTP_PROXY=http://ID:passwd@proxy:port/
setenv HTTP_PROXY=http://ID:passwd@proxy:port/
# for wget etc/wgetrc ~/.wgetrc
use_proxy = on
proxy_user = ID
proxy_passwd = passwd
http_proxy=http://proxy:port/
# Fastestmirror
sudo yum -y install yum-fastestmirror
#Update and Upgrade
sudo yum update
sudo yum upgrade


# Edit Grub.cfg
edit /boot/grub2/grub.cfg

#

sudo yum -y install yum-fastestmirror
sudo yum upgrade
# rpmfusion
rpm -ivh http://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-stable.noarch.rpm http://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-stable.noarch.rpm


sudo yum install axel
# Gnome
sudo yum install gconf-editor
sudo yum install gnome-tweak-tool
sudo yum install gnome-shell-extension*
# yum
sudo yum install yumex
