#!/bin/bash
# Worked well
# sudo echo "export http_proxy=http://proxy.kuins.net:8080"  >> /etc/profile
# Then setup Network/Network Proxy/Manual/Http,Httpps, Ftp
## Others
# echo "export http_proxy=http://proxy.kuins.net:8080"  >> /etc/environment
# echo "export http_proxy=http://proxy.kuins.net:8080"  >> /etc/wgetrc
# echo "export http_proxy=http://proxy.kuins.net:8080"  >> ~/.bashrc
# echo "export ftp_proxy=http://proxy.kuins.net:8080"  >> ~/.bashrc

## Export one time
export http_proxy=http://proxy.kuins.net:8080
export HTTP_PROXY=http://proxy.kuins.net:8080
export https_proxy=http://proxy.kuins.net:8080
export HTTPS_PROXY=http://proxy.kuins.net:8080
export ftp_proxy=http://proxy.kuins.net:8080
export FTP_PROXY=http://proxy.kuins.net:8080