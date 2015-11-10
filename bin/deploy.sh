#!/bin/bash

USER=user
PASS=111111

# must be run from proj root on local machine
git checkout production
git push
ssh $USER@$PASS 'bash -ic "cd /; git pull && AAA.service restart"'
