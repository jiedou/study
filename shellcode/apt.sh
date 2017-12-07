#!/bin/bash
set -e
sudo mv /var/lib/dpkg/info /var/lib/dpkg/info_old 
sudo mkdir /var/lib/dpkg/info
sudo apt-get update && apt-get -f install
sudo  mv /var/lib/dpkg/info/* /var/lib/dpkg/info_old
sudo rm -rf /var/lib/dpkg/info
sudo mv /var/lib/dpkg/info_old /var/lib/dpkg/info 
sudo pt-get update -y && apt-get upgrade -y
sudo pt autoremove -y
