import random

opt=input("Choose Level:\nEasy(E)\nMedium(M)\nHard(H)\n")
if (opt=="E" or opt=="e"):
    randnum = random.randint(0,10)

if (opt=="M" or opt=="m"):
    randnum = random.randint(0,100)

if (opt=="H" or opt=="h"):
    randnum = random.randint(0,1000)

while True:

    userchoice=input("enter the number you guess or quit(Q): ")
    if(userchoice=="Q" or userchoice=="q"):
        break
    else:
        usernum=int(userchoice)

    if(usernum==randnum):
        print("yay ! you won")
        break
    elif(usernum>randnum):
        print("oh no ! too big guess")
    else:
        print("oh no ! too small guess")

print("Thanks for playing.")
