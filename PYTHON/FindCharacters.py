word_list = ['hello','world','my','name','is','Anna']
char = 'o'
new_list = []

for items in word_list:
    i=0
    while i<len(items):
        if items[i] == char:
            new_list.append(items)
        i+=1

print new_list[:]