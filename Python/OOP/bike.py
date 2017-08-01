class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayinfo(self):
        print "The bike for sale is ${}, has a maximum speed of {}, and has {} total miles.".format(self.price, self.max_speed, self.miles)
        return self

    def ride(self):
        self.miles += 10
        print 'Riding'
        return self

    def reverse(self):
        self.miles -= 5
        print "Reversing"
        return self

bike1 = Bike(300, '80mph')
bike2 = Bike(200, '25mph')
bike3 = Bike(100, '10mph')

print bike1.ride().ride().ride().reverse().displayinfo()
print bike2.ride().ride().reverse().reverse().displayinfo()
print bike3.reverse().reverse().reverse().displayinfo()
