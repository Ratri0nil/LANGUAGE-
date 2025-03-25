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



"""
lists=(1,4,9,16,25)
i=0
search=int(input("Enter number to search:"))
while i<len(lists):
    if (lists[i]==search):
        print("found at index:",i)
    else:
        print("searching...")
    i+=1


