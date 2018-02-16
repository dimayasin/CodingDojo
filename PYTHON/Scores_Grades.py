import random

def Scores_Grades():
    count=1
    grade=''
    while count <=10:
        random_num=random.randint(60,101)
        if random_num >= 90:
            grade='A'
        elif random_num>=80:
            grade='B'
        elif random_num >= 70:
            grade='C'
        elif random_num >=60:
            grade='D'
        print "Score: {}; Your grade is {}".format(random_num, grade)
        count +=1
Scores_Grades()


