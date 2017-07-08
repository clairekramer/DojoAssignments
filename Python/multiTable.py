def multiTable():
    print 'x  1 2 3 4 5 6 7 8  9  10  11  12'
    for row in range(1,13):
        for col in range(1,13):
            print row * col, ' '
        print

multiTable()
