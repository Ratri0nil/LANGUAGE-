#!/bin/awk -f

#Declare Functions On Top Here
function Area(x,y){
    area=x*y
    print "Area is : " area
}

BEGIN{
	print "\n____________Started Task_____________\n"
	
    #Variable Declaration
    max=0
    
    #Cannot Give Multiple Values at Indexes Same Time in Array 
    myarray[0]=10
    myarray[1]=13
    score["phy"]=49
    score["math"]=35
}
		
{
    if(length($0)>max)
	    max=length($0)
}

END{
	print "Length OF Longest Line : " max
    print score["math"]

    for(i in myarray)
        print myarray[i]

    for(i=0;i<10;i++)
        print i

    count=5
    while(count<10){
        print count
        count++
    }
    
    Area(12,10)

	print "\n_________End of Task____________\n"
}

#This Is Comment

