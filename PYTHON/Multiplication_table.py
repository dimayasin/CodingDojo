
newList=""
for i in range (1,12):
    if i==1:
        newList += "x"
    else: 
        newList = newList+str(i)

    for j in range (1,12):
        newList = newList + "\t"+ str(i*j)    
        
    print newList
    newList = ""
   