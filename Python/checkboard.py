def check():
    checker = " * * * * "
    for val in range(8):
        if val % 2 == 0:
            print checker
        else:
            print " " + checker

check()
