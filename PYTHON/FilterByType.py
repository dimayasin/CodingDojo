sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']


# Integers:

def Big_SmallNumbers(num):
    if num >=100:
        print "You chose {}. That's a big number!".format(num)
    else:
        print "You chose {}. That's a small number!".format(num)


Big_SmallNumbers(sI)
Big_SmallNumbers(bI)

print "==================================================================="

def StringSize(myStr):
    if len(myStr) >= 50:
        print "You string '{}' is too big!".format(myStr)
    else: 
        print "You string '{}' is a short sentence.".format(myStr)


StringSize(sS)
StringSize(bS)



print "==================================================================="

def ListSize(myList):
    if len(myList) >= 10:
        print "You string '{}' is a big list!!".format(myList)
    else: 
        print "You string '{}' is a short list.".format(myList)

ListSize(aL)
ListSize(lL)



