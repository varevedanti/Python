# Python code to demonstrate type conversion
# using dict(), complex() , str()

#initializing integers
a = 1
b = 2
#initializing tuple
tup = (('a',1) ,('f',2),('g',3))

#printing integer converting to complex number
c= complex(1,2)
print ("After converting integer to complex number : ",end="")
print (c)

#printing integer converting to string
c= str(a)
print ("After converting integer to string : ",end="")
print (c)

#printing integer converting to expression dicitionary
c= dict(tup)
print ("After converting tuple to dicitionary : ",end="")
print (c)
