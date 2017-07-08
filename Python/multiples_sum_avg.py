#multiples part I
for val in range(0,1000):
    if val % 2 != 0:
        print val
    else:
        continue

#multiples part II
for val in range(5,1000000):
    if val % 5 == 0:
        print val
    else:
        continue

#sum list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for val in range(0,len(a)):
    sum = sum + a[val]
print sum

# average list
a = [1, 2, 5, 10, 255, 3]
sum = 0
for val in range(0,len(a)):
    sum = sum + a[val]
avg = sum/len(a)
print avg
