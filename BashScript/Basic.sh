#!/bin/bash
echo "I am I"

: <<'END_COMMENT'

#Variable
name="nil"
age=20
rating=9.9

echo "Name is : $name"
echo "Age is : $age yearss"
echo "Rating is : $rating"

echo $name $age $rating

echo "SHELL is environment variable : "$SHELL

#read input
echo "enter name : "
read name
echo "your name is : $name"

read -p "enter age : " age
echo "you are $age years old"

echo " i don't need variable to reply same"
read
echo " you said : $REPLY"

echo " you can not see password you entering"
read -sp "enter password : " password
echo ""
echo "you entered : " $password 

#Commands Substitution
current_directory=`pwd`
echo "current directory is : $current_directory"

current_directory=$(pwd)
echo "current directory is : $current_directory"

echo "enter contents in new.txt file"
newfile=`cat > new.txt`
echo $newfile

echo "check file once before overwrite"
newfile=$(cat > new.txt)
echo $newfile


END_COMMENT
#Arguments Passing while running script

#echo $0 Reserved for file name not compulsion to declare
echo $1
echo $2 # so on till 9 and not necessary to be entered

echo $@ # print all given parameters
echo $# #print number of arguments passed

name=$1
echo "name is : $name"

