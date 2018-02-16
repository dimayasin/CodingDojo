import random

def Coin_Tosses():
    Head_count=0
    Tail_count=0
    count=0
    msg=""
    while count <=5000:
        random_num=random.randint(1,2)
        if random_num ==1:
            Head_count +=1
            msg="It's a head!"
        elif random_num == 2:
            Tail_count +=1
            msg="It's a tail!"
        print "Attempt #{}: Throwing a coin... {} ... Got {} head(s) so far and {} tail(s) so far".format(count,msg,Head_count,Tail_count)
        count +=1
Coin_Tosses()


