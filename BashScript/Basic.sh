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

#Arguments Passing while running script

#echo $0 Reserved for file name not compulsion to declare
echo $1
echo $2 # so on till 9 and not necessary to be entered

echo $@ # print all given parameters
echo $# #print number of arguments passed

name=$1
echo "name is : $name"

# Arithmatics Operators
read -p "enter one number : " n1
read -p "enter other number : " n2
echo "Addition is = "$((n1+n2))
echo "Substraction is = "$((n1-n2))
echo "multiplication is = "$((n1*n2))
echo "division is = "$((n1/n2))
echo "Remainder is = $((n1%n2))"
echo "pre increment of first : $((++n1))"

# if else
read -p "enter first number : " a 
read -p "enter seconds numbers : " b

if [ $a -eq $b ] 
then
echo "a=b"

elif [ $a -gt $b ]
then
echo "a>b"

else
echo "a<b"

fi

#case
echo "A for 18+"
echo "B for 18-"
read -p "Enter option: " opt
case $opt in
    A)
        echo "Eligible to vote"
        ;;
    B)
        echo "not eligible to vote"
        ;;
    *)
        echo "Invalid age !"
        ;;
esac

#array
names=(nil nisha);
echo "one name is : ${names[1]}"
echo "another name is :  ${names[0]}"
echo "all names are : ${names[*]}"
echo "all names : ${names[@]}" 

# for loop
names=(nil nisha 22 21)
echo " names : ${names[*]}"
for((i=0;i<6;i++)){
    echo "name[$i] = ${names[i]}";
}

for i in 1 2 3 4
do
    echo "yes $i"
done 

#while loop
i=1
read -p " enter age to increase for 10 years from 2025 : " age
while [ $i -le 10 ];
do
    echo "in $((2025 +$i)) you will be $(($age+$i))";
    let i++;
done

#until
aged=1
read -p "enter age less than ten : " age
until [ $aged -ge 10 ];
do
let age++
echo "$age";
let aged++;
done

#break and continue
i=1
read -p "enter a number one: " num
while [ $i -le 10 ];
do
    if [ $num -lt 5 ]
    then
    break

    elif [ $num -lt 10 ]
    then
    let i++
    let num++
    continue
    
    else
    echo " number in process : $num";
    let i++;

    fi
done

#autocreate directory or files
echo "hey I will create 5 directory with below name"
read -p "Enter directory name : " name
for((i=1;i<6;i++)){
    mkdir $name$i
}

echo "hey I will create 5 directory with below name"
read -p "Enter file name : " name
for((i=1;i<6;i++)){
    touch $name$i
}

#auto create user
read -p " enter username to create : " name
read -p " enter user password : " passcode

sudo useradd -m -s /bin/bash $username
echo "$name:$passcode" | sudo chpasswd

#functions

printing(){
    echo " 2+3 = 5"
}
printing

average(){
    num1=$1
    num2=$2
    echo "Average of $num1 and $num2 is : $(($num1 + $num2))"

}
average 5 6
average 5 11

adding(){
    num=$1
    num2=$2
    addnum=$(($num + $num2))
    return $addnum
}
adding 5 10
added=$?
echo "addition is $added"

#nested function
fun1(){
    echo "function one"
}
fun2(){
    echo " function two"
    fun21(){
        echo " function 1 of 2"
    }
}

fun1
fun2

squarefun(){
    num=$1
    numsquare=$(($num*$num))
    return $numsquare
}
addnum_square(){
    num=$1
    squarefun $num
    sq=$?
    added=$(($num + $sq))
    return $added
}
addnum_square 10
result=$?
echo "result = $result" 

#global and local variable
var=100
fun1(){
    var=$1
    echo $var
}
echo $var
fun1 10
echo $var

END_COMMENT

















