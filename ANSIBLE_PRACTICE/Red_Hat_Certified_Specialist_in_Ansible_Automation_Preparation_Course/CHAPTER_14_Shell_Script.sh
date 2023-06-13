#!/bin/bash
#Command line variable is $1
if [ -n "$1" ]
  echo "Package to install is $1"
else
  echo "Package to install not supplied"
  exit
fi

ansible all -b -m yum -a "name=$1 state=present"

##chmod +x CHAPTER_14_Shell_Script.sh 
##./CHAPTER_14_Shell_Script.sh elink