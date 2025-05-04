
BEGIN{
	print "Started Task"
	max=0
}
		
{
    if(length($0)>max)
	    max=length($0)
}

END{
	print "Length OF Longest Line : " max
	print "End of Task"
}
