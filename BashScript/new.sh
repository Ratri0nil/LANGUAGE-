#!/bin/bash

echo Welcome
echo 22

#this is single line comment
<<anyword
this
is multi 
line comment
anyword

echo "hey welcome again"

: <<'COMMENTED'
echo "let us begin"

var=$(hostname)
echo $var

readonly var="myname" #can not modify variable value
echo $var
var="name"
echo $var

newarray=(nil nisha 22 1.5 "hello buddy !")
echo ${#newarray[@]} # length of array

newarray=(nil nisha 22 1.5 "hello buddy !")
echo "values in a range : ${newarray[@]:1:2}" # two values from 1st index

newarray+=( 99 100 )
echo "updated array : ${newarray[@]}"

#key value pair
declare -A myarray
myarray=( [name]=nil [age]=22 [city]=bangalore )
echo ${myarray[*]}
echo "key value of name = ${myarray[name]} "
echo "and age = ${myarray[age]}"

#string operations
mystring="Hello Everyone !"

strlength=${#mystring}
echo "string length is=$strlength"

echo "uppercase is = ${mystring^^}"
echo "lower case is = ${mystring,,}"

newstring=${mystring/Everyone/Dear}
echo "new string is = $newstring"

echo "sliced from 3rd index for length of 4 = ${mystring:3:4}"

read -p "enter your name : " name
echo "Welcome $name"

#Arithmatics
i=0
let i++
a=20
b=10
let c=$a*$b
echo "$i and $c"

#if elif else
read -p "enter score out of 100 : " marks
if [[ $marks -ge 35 ]]
then
    echo "passed exam ! Congrats!!"
elif [[ $marks -lt 35 ]]
then
    echo "sorry :( you failed exam."
else
    echo "Invalid score"

fi

#case statements
echo "choose option 1 or 2"
echo "1 to see date"
echo "2 to list files in directory"
read opt
case $opt in
    1)date;;
    2)ls;;
    *)echo "invalid choice !"
esac

#logical operators
read -p "enter score out of 100 : " score
read -p "enter gender: M for male F for female : " gender

if [[ $score -gt 80 ]] && [[ $score -le 100 ]]
then
    echo " passed Congrats !!"

elif [[ $score -gt 50 ]] || [[ $gender == "F" ]]
then
    echo "Passed"

else
    echo " Sorry bye :( "

fi

age=18
[[ $age -gt 18 ]] && echo "Adult" || echo "Minor"

#for loops
for i in {1..10}
do
    echo "number = $i"
done

for word in ram sham 
do
    echo " word is : $word"
done

#files and for loop
filename="file.txt"
for word in $(cat $filename)
do
    echo "$word"
done

filename="file.txt"
for word in chess ludo
do
    echo $word >> $filename
done

myarray=( 1 2.2 "mew mew")
length=${#myarray[*]}
for ((i=0;i<$length;i++))
do
    echo "${myarray[i]}"
done

#while loop
read -p "enter number to create its table : " num
count=1
while [ $count -lt 11 ]
do
    echo "$(($num*$count))"
    let count++
done

#until loop
i=10
until [[ $i -eq 5 ]]
do
    echo "$i"
    let i--
done

until false #or while true
do
    echo "scanning..."
    sleep 1s
done

for (( ;; ))
do
    echo "in process..."
    sleep 2s
done

#while with file
while read word
do
    echo $word
done < file.txt

#read file data seperated with comma or space etc
while IFS="," read name age rank
do 
    echo "$name $age $rank"
done < test.csv

#functions
function funname {
    echo "new function is here"
}
funname

#Arguments to script
echo "$1"
echo "$2"
echo "$#"   #number of arguments entered
echo "$@"   #print all entered arguments

#for loop with arguments
for arg in $@
do
    echo "copied $arg"
done

#SHIFT arguments
echo "name is : $1"
shift               #ignored first argument and took all remaining in one go
echo "About : $@"

#break in loop
for ((i-=0;i<10;i++)){
    if [ $i -eq 5 ]
    then
        break
    else
        echo "$i"
    fi
}

#continue
for ((i=0;i<10;i++)){
    if [[ $(($i%2)) -eq 0 ]]
    then
        continue
    else
        echo "$i"
    fi
}

#sleep to give time delay
#exit to stop script
if [[ $# -eq 0 ]]
then
    echo "no arguments entered"
    exit 1
else
    echo "$1 and $2"
fi

#exit status if previous command is successful
ls nothing
echo $?
ls
echo $?

#connectivity check
read -p "enter website : " sitename
ping -c 3 $sitename

if [[ $? -eq 0 ]]
then
    echo "success!"
else
    echo "Error in website"
fi

#basename : give only end file name skipping path entered
#realpath : give complete path of file or entered arguments
#dirname : gives only directory name skipping entered path

#check file or directory exist
folderpath=$1
if [[ -d $folderpath ]]
then
    echo " folder exist"
else
    echo " folder not found"

fi

filepath=$1
if [[ ! -f $filepath ]]
then
    echo "file not found"
    echo "creating file..."
    touch $filepath
    echo "file created"
else
    echo "file found"
fi

#RANDOM : a random int from 0 to 32767
echo "$RANDOM"
#UID : user id logged in user
echo "$UID"

DiceGame(){
    echo "Throwing dice.."
    echo " number came = $(($RANDOM%6 +1))"
}
DiceGame

CheckRootUser(){
    if [[ $UID -eq 1000 ]]
    then
        echo "It is root user"
    else
        echo "Not root user"
    fi
}
CheckRootUser

#Redirection in Scripts
ls >> file.txt
cat "file.txt"

# if do not want to print in terminal or in file : &> /dev/null
read -p "enter website : " sitename
ping -c 3 $sitename &> /dev/null

echo "script name is : ${0}"

#Debugging
set -x #execute line by line with debugging
echo "hey"
read -p "write your name : " name
echo "nice to see you $name"

#exit script if error comes in a line
set -e
echo "error or not checking"
datey
whoami

#run script in background even after closing terminal
# commands used : nohup filename.exe &
for i in {1..5}
do
    echo "$i" >
    sleep 1s
done

#Automate script
at DD:MM
bash filename.sh
ctrl+D
#check auto scripts
atq
#remove auto script
atrm ID

COMMENTED

