#l = ['magical unicorns',19,'hello',98.98,'world']
#l = [2,3,1,7,4,12]
l = ['magical','unicorns']

i=0
flagStr=False
flagNum=False
sum=0.0
NewList=""

while i< len(l):
    if type(l[i]) == str:
        flagStr=True
        NewList += l[i] + " "
    elif type(l[i]) == int:
        flagNum=True
        sum += l[i]
    i +=1

if flagStr and flagNum :
    print "The list you entered is of mixed type"
    print "String: {}".format(NewList)
    print "Sum: {}".format(sum)
elif flagStr and not flagNum:
    print "The list you entered is of string type"
    print "String: {}".format(NewList)
elif flagNum and not flagStr:
    print "The list you entered is of integer type"
    print "Sum: {}".format(sum)   

    
