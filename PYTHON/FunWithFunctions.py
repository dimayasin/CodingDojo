# Odd/Even

# print "Odd or Even numbers:"
# print "================================================="



# def odd_even():
#     for i in range (1, 2000):
#         if i%2 == 0:
#             print "Number is {}. This is an even number.".format(i)
#         else:
#             print "Number is {}. This is an odd number.".format(i)

# odd_even()
print "================================================= \n"

print "Function Multiples: \n"

a = [2, 4, 10, 16]

def multiply(arr, val):
    new_arr=[]
    for i in arr:
        new_arr.append(i*val)
    return new_arr

print "The list before the function call is: {}".format(a)
print "The list before the function call is: {}".format(multiply(a,5))

print "================================================= \n"


print "Hacker Challenge: "
print "================================================= \n"

arr=[]
def layered_multiples(arr):
    list1=[]
    new_array=[]

    for i in range(0,len(arr)):

        value=arr[i]
        for j in range(0,value):
            list1[j]=1
        print list1 
        new_array[i]=list1

    #    print "index is {}. arr is {}".format(i, item)



     return new_array

x = layered_multiples(multiply([2,4,5],3))
print x