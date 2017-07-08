def typeList(x):
    sum = 0
    strCount = 0
    word = ""
    for each in x:
        if isinstance(each, int):
            sum += each
        elif isinstance(each, float):
            sum += each
        elif isinstance(each, str):
            word += " "+ each
            strCount= strCount + 1
    if sum == 0:
        print "The array you entered is of string type"
    elif strCount == 0:
        print "The array you entered is of integer type"
    else:
        print "The array you entered is of mixed type"
    if strCount > 0:
        print "String:" + word
    if sum > 0:
        print 'Sum: {}'.format(sum)

typeList(['magical unicorns',19,'hello',98.98,'world'])
