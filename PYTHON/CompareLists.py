# list_one = [1,2,5,6,2]
# list_two = [1,2,5,6,2]

# list_one = [1,2,5,6,5]
# list_two = [1,2,5,6,5,3]

# list_one = [1,2,5,6,5,16]
# list_two = [1,2,5,6,5]

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

if len(list_one) == len(list_two):

    same=False
    i=0
    while i< len(list_one):
        if list_one[i] == list_two[i] :
            same = True
       

        else: 
            same=False
            break;
        i +=1
    if same :
        print "The lists are the same."
    else:
        print "The lists are not the same."
else:
    print "The lists are not the same."