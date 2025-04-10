"""

coordinates=[1,2,3]
x,y,z=coordinates
print(x,y,z)

name="nil \" kill"
print(name)

n1="nil"
n2="kill"
n=f"{n1} {n2}"
print(n)

age=24
if 18< age < 26 :
    print("yes")

def increase(val ,by):
    return val+by
print(increase(4, by=1))

def increase(val ,by=3):
    return val+by
print(increase(4))

def nums(*num):
    print(num)
    total=0
    for numb in num:
        total=total+numb
        print(total )
nums(1,2,3,4)

def info(**user):
    print(user)
    print(user["age"])
info(id=1,age=22.5,name="nil")


def fizz_buzz(input):
    if input%3==0 and input%5==0:
        return "fizzbuzz"
    if input%3 ==0:
        return "Fizz"
    if input%5 ==0:
        return "Buzz"

    else:
        return input
    
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))
print(fizz_buzz(19))


x=1
print(id(x))
x+=1
print(id(x))

x=[1,2,3,5]
print(id(x))
x.append(9)
print(id(x))

x=2.5
y=3.5
x=round(x)
y=round(y)
print(x,y)
x=abs(-4.9)
print(x)

import math
print(math.cos(30))

matrix=[
    [1,2,3],
    [4,5,6]
    
    ]
print(matrix[0][1])
matrix[0][1]=99
print(matrix[0][1])
for row in matrix:
    print(row)
    for item in row:
        print(item)


message=input("say>> ")
words=message.split(" ")
emojis={
    ":)" : "😊",
    ":(" : "😒"
}
output=""
for word in words:
    output=output+ emojis.get(word,word)+" "
print(output)


try :
    age = int(input("enter age: "))
    print("age is: ",age)
    income= 10000
    net=income/age
except ZeroDivisionError:
    print("age can't be zero")    
except ValueError:
    print("Invalid age")

import converters
#OR
from converters import INR_USD
print(converters.INR_USD(900))

def adding(num1,num2):
    num=num1+num2
    return num, num1,num2
print(adding(4,5))



 
"""

