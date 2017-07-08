def printDict():
    dict = {'name':'Claire','age':'24','country of birth':'USA','language':'Python'}
    for key, val in dict.iteritems():
        print 'My {} is {}'.format(key,val)

printDict()
