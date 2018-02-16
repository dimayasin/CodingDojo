name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
  new_dict = dict(zip(list1, list2))
  # your code here
  return new_dict


for key, val in make_dict(name,favorite_animal).items():
    print key, " : ", val

print "======================================================="
print "Hacker's Challenge"
print "======================================================="


def make_dict2(list1, list2):
    if len(list1) > len(list2):
        new_dict1 = dict(zip(list1, list2))
    else:
        new_dict1 = dict(zip(list2, list1))
  # your code here
    return new_dict1


name1 = ["Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal1 = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

for key, val in make_dict2(name1,favorite_animal1).items():
    print key, " : ", val
