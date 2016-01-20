#!/bin/bash

# installation tested on Ubuntu 15 clean

sudo apt -y install gcc gfortran unixodbc-dev libblas-dev liblapack-dev cython unixodbc-dev unixodbc-bin unixodbc

# Dont use this line in production
sudo pip3 install -r requirements.txt

# log file, launch and database dirs
# sudo mkdir -p /var/local/aaa
# sudo chmod a+rwx /var/local/aaa
