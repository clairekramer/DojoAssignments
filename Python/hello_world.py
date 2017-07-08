print "Hello World!"

x = "Hello Python"
print x
y = 42
print y

print "read below for more on multi-line comments in python!" #this would execute
# This line and below would not execute
'''
    Triple quotations allow us to comment across multiple lines as long as
    the triple quoted comment is not the first thing in your file.
    You can use double or single quotes!
    '''

first_name = "Zen"
last_name = "Coder"
print "My name is {} {}".format(first_name, last_name)


x = "Hello World"
print x.upper()
# output: uppercase

#for loop
for count in range(0, 5):
    print "looping - ", count

#while loop
count = 0
while count < 5:
    print 'looping - ', count
    count += 1
