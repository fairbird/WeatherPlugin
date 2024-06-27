#!/bin/bash
# ###########################################
# SCRIPT : DOWNLOAD AND INSTALL WeatherPlugin
# ###########################################
#
# Command: wget https://raw.githubusercontent.com/fairbird/WeatherPlugin/master/installer.sh -qO - | /bin/sh
#
# ###########################################

###########################################
# Configure where we can find things here #
TMPDIR='/tmp'
PLUGINDIR='/usr/lib/enigma2/python/Plugins/Extensions'

#######################
# Remove Old Version #
rm -rf $PLUGINDIR/WeatherPlugin
rm -rf $PLUGINDIR/Biscotto
rm -rf $TMPDIR/*master*

#########################
if [ -f /etc/opkg/opkg.conf ]; then
    STATUS='/var/lib/opkg/status'
    OSTYPE='Opensource'
    OPKG='opkg update'
    OPKGINSTAL='opkg install'
elif [ -f /etc/apt/apt.conf ]; then
    STATUS='/var/lib/dpkg/status'
    OSTYPE='DreamOS'
    OPKG='apt-get update'
    OPKGINSTAL='apt-get install'
fi
#########################
if [ -f /usr/bin/python3 ] ; then
    echo ":You have Python3 image ..."
else
    echo ":You have Python2 image ..."
fi
#########################
cd $TMPDIR
set -e
echo "Downloading And Insallling WeatherPlugin Please Wait ......"
echo
wget https://github.com/fairbird/WeatherPlugin/archive/refs/heads/master.tar.gz -qP $TMPDIR
tar -xzf master.tar.gz
cp -r WeatherPlugin-master/usr /
rm -rf *master*
set +e
cd ..
#########################

sleep 1
clear
echo "#########################################################"
echo "#          WeatherPlugin INSTALLED SUCCESSFULLY         #"
echo "#########################################################"

exit 0
