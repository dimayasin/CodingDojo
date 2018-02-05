# printing odd numbers between 1 and 1000

print "======================="
print "Odd numbers 1 - 1000: "
print "======================="
for i in range( 1, 1000, 2):
    print (i)

# printing all multiples of 5 betwen 5 - 1000000


print "===================================="
print "Multiples of 5 from 5 - 1000,000: "
print "===================================="
for i in range (5, 1000000, 1):
    if i%5 == 0 :
        print i


# Sum List

print "========================================================="
print "Sum of all items in the list: a = [1, 2, 5, 10, 255, 3] "
print "========================================================="

a = [1, 2, 5, 10, 255, 3]
sum=0
i=0
while i< len(a):
    sum += a[i]
    i +=1

print "The sum of all the items in the list is: {}".format(sum)

avg=0
avg= sum / len(a)
print "The avrg of the list items is: {}".format(avg)
