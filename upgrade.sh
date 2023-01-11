#!/bin/bash

# Comment out the existing Proxmox Enterprise repository
sed -i "s/^deb/\#deb/" /etc/apt/sources.list.d/pve-enterprise.list 

# Add the Proxmox Community repository
echo "deb http://download.proxmox.com/debian/pve $(grep "VERSION=" /etc/os-release | sed -n 's/.*(\(.*\)).*/\1/p') pve-no-subscription" > /etc/apt/sources.list.d/pve-community.list

# Update the package list
apt update 

# Apply the modification to the proxmoxlib.js file and backup the original
sed -Ezi.bak "s/(Ext.Msg.show\(\{\s+title: gettext\('No valid sub)/void\(\{ \/\/\1/g" /usr/share/javascript/proxmox-widget-toolkit/proxmoxlib.js

#Installs pip library
apt-get install pip

#Installs inplace modu
python3 -m pip install in_place
