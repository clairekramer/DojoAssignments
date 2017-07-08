# fizzbuzz function
def fizzbuzz(num):
    for idx in range(0,num+1):
        if (idx % 3 is 0 and idx % 5 is 0):
            print 'FizzBuzz'
        elif (idx % 3 == 0):
            print 'Fizz'
        elif (idx % 5 == 0):
            print 'Buzz'
        else:
            print idx

fizzbuzz(15)

#Lists = Arrays
myList = [1,2,3]
print myList[2]

#Dictionarys:
myDictionary = {
    'name': 'Todd',
    'age': 33
}

myDictionary['age'] = 21
print myDictionary['age']

#Tuple = immutable array
myTuple = (1,2,3)
