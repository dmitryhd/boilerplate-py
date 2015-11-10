#!/bin/bash

# installation tested on Ubuntu 15 clean

sudo apt -y install gcc gfortran unixodbc-dev libblas-dev liblapack-dev cython unixodbc-dev unixodbc-bin unixodbc

# Dont use this line in production
sudo pip3 install -r requirements.txt


# log file, launch and database dirs
sudo mkdir -p /var/local/aaa
sudo chmod a+rwx /var/local/aaa

# copy example file
NOW=$(date +"%m-%d-%Y-%H-%M")
cp -v /var/local/crm/crm.campaigns.db /var/local/crm/crm.campaigns.db-$NOW
cp -v docs/crm.campaigns.db /var/local/crm/

# sudo apt -y install unixodbc-dev unixodbc-bin unixodbc
