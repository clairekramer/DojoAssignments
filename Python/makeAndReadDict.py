myDict = {
    "name": "Claire",
    "age": "24",
    "country of birth": "The United States",
    "favorite language": "Python"
}

def readDict(dict):
    for key, value in dict.iteritems():
            print "My {} is {}".format(key, value)


readDict(myDict)
