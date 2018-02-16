class Animal(object):
    def __init__(self, name, health):
        self.name=name
        self.health = health
    
    def walk(self):
        self.health -=1
        print "Animal walked...."
        return self
  
    def run(self):
        self.health -=5
        print "Animal ran...."
        return self
  
    def display_health(self):
        print "Health is: {}".format(str(self.health))
        print "=======================================\n \n"
        return self

pet = Animal("Cocoa", 20)
pet.walk().walk().walk()
pet.run().run()
pet.display_health()

class Dog(Animal):
    
    
    def pet(self):
        self.health += 5
        print "Animal was pet...."
        return self

MyDog = Dog("toto",150)
MyDog.walk().walk().walk()
MyDog.run().run()
MyDog.pet()
MyDog.display_health()

class Dragon(Animal):
    def __init__(self,name="Drago",health = 170):
        super(Dragon, self).__init__(name, health)


    def fly(self):
        print "Animal Fly .............."
        self.health -=10
        return self
    
    def display_health(self):
        super(Dragon, self).display_health()
        print "I am a Dragon!"
        print "========================================="
        return self

myDragon = Dragon()
myDragon.fly().fly()
myDragon.display_health()




