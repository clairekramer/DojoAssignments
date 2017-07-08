#Odd/Even:
def odd_even():
    for number in range(1,2001):
        if(number % 2 == 0):
            print 'Number is {}. This is an even number.'.format(number)
        else:
            print 'Number is {}. This is an odd number.'.format(number)

odd_even()

#Multiply
def multiply(arr, val):
    for x in range(len(arr)):
        arr[x] = arr[x] * val
    return arr

a = [2,4,10,16]
b = multiply(a, 5)
print b

#Hacker Challenge
def layered_multiples(arr):
    new_arr = []
    for x in range(len(arr)):
        inside_arr = []
        for y in range(arr[x]):
            inside_arr.append(1)
        new_arr.append(inside_arr)
    return new_arr

x = layered_multiples(multiply([2,4,5],3))
print x
