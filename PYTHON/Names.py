print "====================================================================="
print "Part I"
print "====================================================================="

students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


for index in students:
        print "{} {}".format(index['first_name'], index['last_name'])

print "====================================================================="
print "Part II"
print "====================================================================="

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

for key,val in users.items():
    counter=1
    print key, " :"
    for index in val:
        print counter ," - ",index['first_name']," " , index['last_name']," - " ,  str((len(index['first_name'])+len(index['last_name'])))
        counter +=1
