class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12

    def display_all(self):
        print "Price: {}".format(self.price)
        print "Speed: {}mph".format(self.speed)
        print "Fuel: {}".format(self.fuel)
        print "Mileage: {}mpg".format(self.mileage)
        print "Tax: {}".format(self.tax)
        return self

car1 = Car(2000, 35, 'Full', 15)
car2 = Car(2000, 5, 'Not Full', 105)
car3 = Car(20000, 25, 'Empty', 15)

car3.display_all()
