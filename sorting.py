# this is a comment
print("starting the sorting program!")

#creating a list variable in python
mylisttosort=[0,1,4,3,5,444444444,23,5,219,-5,2,485,4,-124,69,420,564]

print("Before sorting")
print(mylisttosort)

lengthoflist=len(mylisttosort)
print(lengthoflist)

i=0

sorted=False

swap=0

#Creating an outer loop
while(sorted==False):
	#print("sorted=", sorted)
	i=0
	sorted = True
	while(i<lengthoflist-1):
		#Check to see if the 2 values are in order
		if mylisttosort[i] > mylisttosort[i+1]:
			#print("Swapping", mylisttosort[i], " with ", mylisttosort[i+1] )
			sorted = False
			swap = mylisttosort[i]
			mylisttosort[i] = mylisttosort[i+1]
			mylisttosort[i+1] = swap
		#end of if section

		#Increment i
		i=i+1
		#This is the end of the inner loop
	#this is the end of the outer loop

print("After sorting")
print(mylisttosort)