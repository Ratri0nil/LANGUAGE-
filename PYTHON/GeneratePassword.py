import random
import string

opt1=input("Would you like to have Uppercase alphabets in your password ? Yes(Y) or No(N) : ")
opt2=input("Would you like to have Lowercase alphabets in your password ? Yes(Y) or No(N) : ")
opt3=input("Would you like to have digits in your password ? Yes(Y) or No(N) : ")
opt4=input("Would you like to have special symbols in your password ? Yes(Y) or No(N) : ")


if (opt1=="Y" or opt1=="y") :
    choice1 = string.ascii_uppercase
else:
    choice1 = ""

if (opt2=="Y" or opt2=="y") :
    choice2 = string.ascii_lowercase
else:
    choice2 = ""

if (opt3=="Y" or opt3=="y") :
    choice3 = string.digits
else:
    choice3 = ""

if (opt4=="Y" or opt4=="y") :
    choice4 = string.punctuation
else:
    choice4 = ""

choice=choice1 + choice2 + choice3 +choice3 + choice4

password=""
length=int(input("enter password length: "))

for value in range(length):
    password += random.choice(choice)

print("password is: ",password)






