#!/bin/bash

#check root user
if [[ ${UID} -ne 0 ]]
then
echo "please come with root Permissions next time"
exit 1
fi

#check username entered
if [[ ${#} -lt 1 ]]
then 
echo "Usage : ${0} USERNAME [optinal Comments]"
echo "Enter UserName and comments as above"
exit 1
fi

#Take UserName
UserName=${1}
#Take comments
shift
Comment=${@} 

#Random password 
Password=$(date +%s)

echo "Creating User for $UserName and commented out $Comment"

# create user with comments and home directory
useradd -c "${Comment}" -m $UserName 

#check user created
if [[ $? -ne 0 ]]
then 
    echo "Sorry ! User Creation Failed"
    exit 1
else
   echo "Created User Successfully"
fi

#set password
echo $Password | passwd --stdin $UserName

#check password created
if [[ $? -ne 0 ]]
then 
    echo "Sorry ! User password Creation Failed"
    exit 1
else
   echo "Created User password Successfully"
fi

#change password on first login
passwd -e $UserName

echo "UserName : $UserName"
echo "Password : $Password"
echo "Thank You"

