class Product(object):
    def __init__(self, price, item_name, weight, brand, status= "for sale"):
        self.price=price
        self.item= item_name
        self.weight= weight
        self.brand= brand
        self.status=status
    
    def sell(self):
        self.status="Sold"
        return self
  
    def Add_tax(self,tax):
        self.price += self.price * tax
        return self.price
    
    def Return(self, reason):
        
        if reason == "defective":

            self.status = reason
            self.price = 0
        elif reason == "in the box, like new":
            self.status = "For Sale"
        elif reason =="the box has been opened":
            self.status = "used"
            self.price -= self.price * 0.20

        return self

    
  
    def display_info(self):
        print  "===================================="        
        print "Item Name: {}".format(self.item)
        print "Price: {}".format(str (self.price))
        print  "Weight: {}".format(self.weight)
        print  "Brand: {}".format(self.brand)
        print  "Status: {}".format(self.status)
        print  "===================================="

        return self




product1 = Product(999.99,"Laptop", "5lbs","Dell")
product1.display_info()
product1.Return("the box has been opened")
product1.display_info()