class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price=price
        self.speed=speed
        self.fuel=fuel
        self.mileage=mileage
        if self.price > 10000:
            self.tax=0.15
        else:
            self.tax=.12

    
    def display_all(self):
        msg = "Price:" + str (self.price)
        msg =msg+ "\nSpeed: " + self.speed
        msg = msg + "\nFuel: "+ self.fuel
        msg = msg + "\nMileage: "+ self.mileage
        msg = msg + "Tax: "+ str (self.tax) + "\n \n"

        return msg




mycar = Car(2000,"35mph", "Full","15mph")
bigMsg = mycar.display_all()
print bigMsg

mycar1 = Car(2000,"5mph", "Not Full","10mph")
bigMsg = mycar.display_all()
print bigMsg

mycar = Car(2000,"15mph", "Kind of Full","95mph")
bigMsg = mycar.display_all()
print bigMsg
    
mycar = Car(2000,"25mph", "Full","25mph")
bigMsg = mycar.display_all()
print bigMsg

mycar = Car(2000,"45mph", "Empty","25mph")
bigMsg = mycar.display_all()
print bigMsg

mycar = Car(20000000,"35mph", "Empty","15mph")
bigMsg = mycar.display_all()
print bigMsg