#!/bin/sh

# This Script creates direcotires in the /tmp folder,
# that mimics the /etc/sv and /var/service folders in Void linux.
# It exists to test svs without changing actual system services.

#Create service directories
DIR="/tmp/svs/sv/"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi

DIR="/tmp/svs/service/"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi

# Create a few services
# Enabled Services
DIR="/tmp/svs/sv/agetty-tty1"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi
ln -sf $DIR /tmp/svs/service/

DIR="/tmp/svs/sv/dhcpd"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi
ln -sf $DIR /tmp/svs/service/

DIR="/tmp/svs/sv/openntpd"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi
ln -sf $DIR /tmp/svs/service/

# Disabled Services
DIR="/tmp/svs/sv/sshd"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi

DIR="/tmp/svs/sv/alsa"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi

DIR="/tmp/svs/sv/lightdm"
if [ ! -d $DIR ]; then
    mkdir -p $DIR
fi
