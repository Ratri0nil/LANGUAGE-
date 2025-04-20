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

COMMENTED
#read file data seperated with comma or space etc
while IFS="," read name age rank
do 
    echo "$name $age $rank"
done < test.csv

