class Bike(object):
    def __init__(self, price,max_speed,miles):
        self.price=price
        self.max_speed=max_speed
        self.miles=miles

    
    def displayInfo(self):
        print "The bike's price is: ", self.price
        print "Maximum Speed is: ", self.max_speed
        print "Total miles is: ",self.miles
        return self

    def ride(self):
        print "Riding......."
        self.miles += 10
        return self
    
    def reverse(self):
        print "Reversing........"
        self.miles -= 10
        return self


myBike = Bike(200,20, 0)
myBike.displayInfo().ride()
myBike.displayInfo()


    