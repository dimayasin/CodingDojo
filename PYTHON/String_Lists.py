
# Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"

print words.find("day")


NewStr = ""
NewStr = words.replace("day", "month")

print NewStr
        
# Min and Max
x = [2,54,-2,7,12,98]
print "The smallest number in the list is: "+ str (min(x))
print "The largest number in the list is: "+ str (max(x))


#First and Last

x = ["hello",2,54,-2,7,12,98,"world"]
x.sort()
print "first item in the list is: " + str(x[0])
print "lat item in the list is: " + str(x[len(x)-1])

# New List

x = [19,2,54,-2,7,12,98,32,10,-3,6]
i = 0
list1=[]
while i<len(x)/2:
    list1.append(x[i])
    i=i+1

print "The old list is: "
print x[:]

finalList=[0]

finalList[0] = list1 
i=len(x)/2 +1
while i<len(x):
    finalList.append(x[i])
    i=i+1

print "The new list is: "
print finalList[:]
        