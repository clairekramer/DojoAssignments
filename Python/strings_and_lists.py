# Find and Replace
words = "It's thanksgiving day. It's my birthday, too!"
print words.find('day')

words = words.replace('day', 'month')
print words

#Min and Max
x = [2,51,-2,7,12,98]
print x
print min(x)
print max(x)

#First and Last
x = ['hello',2,54,-2,7,12,98,'world']
print x[0]
print x[len(x)-1]
new_list = []
new_list.append(x[0])
new_list.append(x[len(x)-1])
print new_list

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
new_list = x[:len(x)/2]
print new_list
x = x[len(x)/2:]
print x
x.insert(0,new_list)
print x
