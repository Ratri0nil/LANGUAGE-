print("I am I\n####################")

"""
name="nilkanth"
print("my name is: ",name)
age=22
print("my age is: ",age,"years")
IQ=9.9
print("my IQ is: ",IQ)

print(type(name))
print(type(age))

boolean1=True
boolean2=False
print(boolean1,boolean2)
print(2==2,2!=2)
NoneVariable=None
print(NoneVariable)

num1,num2=11,14
sum,diff =num1+num2 , num1-num2
print(sum,diff)

num1,num2=2,3
str="*"
print(num1*str*num2)

str1,str2="2x","."
num=4
print((str1+str2)*num)

num1,num2=2,4.0
print(num1+num2,num1-num2,num1*num2,num1/num2,num1//num2,num1%num2,num2**num1)

num1,num2=4,2
print(num1/num2,num2/num1,num1//num2,num2//num1)

num1,num2=4.0,2
print(num1/num2,num2/num1,num1//num2,num2//num1)

num1,num2=4.0,-2
print(num1/num2,num2/num1,num1//num2,num2//num1)

num1,num2=4,-3
print(num1%num2,num2%num1)

"""

# print("comment")
"""print(comments)"""

"""
name=input("enter name: ")
age=int(input("enter age: "))
rating=float(input("rate yourself: "))
print("Hi",name,"your age is:",age,"years and you are: ",rating)

if(age>=18 and age <=25):
    print("you can vote but can't get vote")
elif(name=="nilkanth" or name=="nisha"):
    print("It is me")
else:
    print("bye")"

nature="smart" if name=="nilkanth" else "bad"
print("you are very",nature)

nature=("green","red") [age>25]
print("you are a",nature,"flag")
"
"""

"""
num1=int(input("enter number one: "))
num2=int(input("enter number two: "))
sum=num1+num2
print("sum of",num1,"and",num2,"is",sum)

side=float(input("enter side of square:"))
area=side**2
print("area of square is:",area)"

num1=int(input("enter number one: "))
num2=int(input("enter number two: "))
print(num1>=num2)"

str1= input("enter string one: ")
str2= input("enter string two: ")
strnew=str1+str2
print(strnew)
print(len(strnew))

str="good morning!"
# str[0]="w" not allowed
print(str[1],str[:],str[:8],str[4:],str[-4:-1])

str="my name is nilkanth !"
print(str.endswith("kanth"))
print(str.capitalize())
print(str)
print(str.replace("n","wtf"))
print(str)
print(str.find("ni"))
print(str.count("n"))

name=input("enter name: ")
print(len(name))
occur=input("enter to know occurence of: ")
print(name.count(occur))


num=int(input("enter number: "))
if(num%2==0):
    print("Even number")
else:
    print("Odd number")

num1=float(input("enter number: "))
num2=float(input("enter number: "))
num3=float(input("enter number: "))
if(num1>num2):
    if(num1>num3):
        print("greatest number : ",num1)
    else:
        print("greatest number : ",num3)
elif(num2>=num1 and num2>=num3):
    print("greates number is: ",num2)
else:
    print("greatest number is: ",num3)


#lists
marks=[10,10.2,-1,"hey hey"]
print(marks)
print(marks[1])

print(len(marks))

marks[0]="nil"
print(marks)

print(marks[:],marks[3:],marks[:3],marks[2:3],marks[-3:-1])

marks.append(90)
print(marks)

list1=["apple","Apple","nil"]
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.reverse()
print(list1)

list1.insert(2,"yes")
print(list1)

list1.remove("apple")
print(list1)

list1.pop(1)
print(list1)

#Tuples
tups=()
print(tups)
tups=(1,)
print(tups)
tups=(1,2.2,"hello")
print(tups)

tups=(1,11,2,1)
print((tups.index(1)))
print(tups.count(1))

movies=[]
name=input("enter favourite movie: ")
movies.append(name)
name=input("enter favourite movie: ")
movies.append(name)
name=input("enter favourite movie: ")
movies.append(name)
print("your fav movies are: ",movies)

palindrome=[1,2,3,22,1]
newpalindrome=palindrome.copy()
newpalindrome.reverse()
if palindrome==newpalindrome:
    print("it is a palindrome")
else:
    print("Not palindrome")

#dictionary
info={
    "name": ["nil","nisha"],
    "age": 22,
    "rating": 9.0,
    "isPsycho": True,
    22.22: 22.2

}
print(info)
print(info["name"])
info["name"]="kill"
print(info)
info["surname"]=0
print(info)

nulldict={}
print(nulldict)

info={
    "name":"krish",
    "marks": {
        "phy":90,
        "bio":99
    }
}
print(info)
print(info["marks"])
print(info["marks"]["phy"])

print(list(info.keys()))
print(info["marks"].keys())

print(info.values())
print(info["marks"].values())
print(list(info.values()))

pair=list(info.items())
print(pair[0])

print(info.get("name"))
print(info.get("na666me"))

info.update({"city":"banglore", "age": 66})
print(info)

#sets
sets={1,2.2,1,"hello",(6,9)}
print(sets)

nullset=set()
print(nullset)

nullset.add("hello")
nullset.add(1)
print(nullset)

nullset.remove(1)
print(nullset)

nullset.clear()
print(nullset)

sets.pop()
print(sets)
print(len(sets))

set1={1,2,3,4}
set2={2,3,4,5}
set3=set1.union(set2)
print(set3)
set4=set1.intersection(set2)
print(set4)

diction={
    "table":("a piece of furniture","list of facts and figures"),
    "cat":"a small animal"
}
print(diction)

students={}
sub=input("enter subject: ")
mark=int(input("Enter marks: "))
students.update({sub:mark})
sub=input("enter subject: ")
mark=int(input("Enter marks: "))
students.update({sub:mark})
sub=input("enter subject: ")
mark=int(input("Enter marks: "))
students.update({sub:mark})
print(students)

nums={("int",9),("float",9.0)}
print(nums)

count=1
while count<=100:
    print(count)
    count+=1

while count>0:
    print(count)
    count-=1

i=1
num=int(input("enter number: "))
while i<=10:
    print(num*i)
    i+=1

lists=[1,4,9,16,25]
i=0
while i<len(lists):
    print(lists[i])
    i+=1

lists=(1,4,9,16,25)
i=0
search=int(input("Enter number to search:"))
while i<len(lists):
    if (lists[i]==search):
        print("found at index:",i)
    else:
        print("searching...")
    i+=1

i=0
while i<5:
    print(i)
    if(i==3):
        break
    else:
        i+=1

i=0
while i<5:
    if(i==3):
        i+=1
        continue
    else:
        print(i)
    i+=1

numbers=[1.1,2,"hello"]
for num in numbers:
    print(num)

str="nilkanth"
for char in str:
    if(char=="z"):
        print("found")
        break
else:
    print("Not found")

#Range
for i in range(2,10,3):
    print(i)

num=int(input("enter number: "))
for i in range(1,11):
    print(i*num)

for i in range(100):
    pass

sum,i=0,1
n=int(input("enter number: "))
while i<=n:
    sum=sum+i
    i+=1
print("sum is: ",sum)

i=1
n=int(input("enter number: "))
while i<=n:
    fact=1
    for j in range(1,i+1):
        fact=j*fact
    print("factorial of",i,"is",fact)
    i+=1

def sum(a,b):
    s=a+b
    return s

s=sum(11,22)
print(s)

print("hello",end="%")
print("world")

def sum(a,b=0):
    s=a+b
    return s

s=sum(1,1)
print(s)

def listlen(lists):
    count=0
    for i in lists:
        count+=1
    return count

lists=[1,2,3,"1.2"]
print(listlen(lists))

def print_ele(lists):
    for i in lists:
        print(i,end=" ")

lists=[1,2,3,"1.2"]
print_ele(lists)

def factorial(n):
    fact,i=1,1
    while i<n+1:
        fact=i*fact
        i+=1
    print("factorial is:",fact)

n=int(input("enter number:"))
factorial(n)

def facto(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*facto(n-1)

num=int(input("enter number:"))
print(facto(num))


#file
f=open("file.txt","r")
print(f.read())
print(f.read(5))
print(f.readline())
f.close()

f=open("file.txt","a")
f.write("TO WRITE: \nF.WRITE()")

with open("file.txt","r") as f:
    print(f.read())

import os
os.remove("file.txt")

with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning F i/o\nusing java.\ni hate I")
with open("practice.txt","r") as f:
    data=f.read()
    print(data.replace("java","qpython"))
    if(data.find("python")!=-1):
        print("found")

count=1
data=True
with open("practice.txt","r") as f:
    while data:
        data=f.readline()
        if("python" in data):
            print(count)
        else:
            count+=1
        
lists=[]
with open("practice.txt","r") as f:
    data=f.read()
    num=""
    for i in range(len(data)):
        if(data[i]==","):
            lists.append(int(num))
            num=""
        else:
            num+=data[i]
for i in lists:
    if(i%2==0):
        print(i)

with open("practice.txt","r") as f:
    data=f.read()
    lists=data.split(",")
for i in lists:
    if(int(i)%2==0):
        print(i)

#class and object
class student:
    name="nil"
    age=22
s1=student()
print(s1.name,s1.age)

#constructor
class student:
    species="human"
    name="null"
    def __init__(self, name,age):
        print("adding new student...")
        self.name=name
        self.age=age
    def YOB(self):
        year=2025-self.age
        print("year of birth is: ",year)

s1=student("nilkanth",22)
s2=student("nil",222)
print(s2.name,s2.age,s2.species)
print(s1.name,s1.age)
s1.YOB()
s2.YOB()

class student:
    def __init__(self):
        print("welcome")
        self.name=input("enter name: ")
        self.subj1=int(input("enter physics marks: "))
        self.subj2=int(input("enter math marks: "))
        self.subj3=int(input("enter bio marks: "))
        
    def average(self):
        avg=(self.subj1 +self.subj2+self.subj3)/3
        print("average is=",avg)

s1=student()
s1.average()

#decorator
class student:
    @staticmethod
    def hello():
        print("no need of self here")

s1=student()
s1.hello()



"""

class bank:
    def __init__(self):
        print("welcome to Children's bank of India")
        self.id=int(input("enter account number: "))
        self.bal=float(input("enter balance: "))
        
    def balance(self):
        ids=int(input("enter account number:"))
        if(ids==self.id):
            print("your current balance is: INR",self.bal)
        else:
            print("Invalid account number")

    def credit(self,amount):
        self.bal+=amount

    def debit(self,amount):
        if(self.bal>=amount):
            self.bal -=amount
        else:
            print("insufficient balance")

p=bank()
p.balance()
class bank:
    def __init__(self):
        print("welcome to Children's bank of India")
        self.id=int(input("enter account number: "))
        self.bal=float(input("enter balance: "))
        
    def balance(self):
        ids=int(input("enter account number:"))
        if(ids==self.id):
            print("your current balance is: INR",self.bal)
        else:
            print("Invalid account number")

    def credit(self,amount):
        self.bal+=amount

    def debit(self,amount):
        if(self.bal>=amount):
            self.bal -=amount
        else:
            print("insufficient balance")

p=bank()
p.balance()
p.credit(1000)
p.balance()











































































