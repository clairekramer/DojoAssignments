#Coin Tosses
def toss():
    import random
    print "Starting the program..."
    heads = 0
    tails = 0
    for each in range(1, 5001):
        x = random.randint(0,1)
        if x == 0:
            heads = heads + 1
            print "Attempt #{}: Throwing a coin... It's heads! ... Got {} head(s) so far and {} tail(s) so far".format(each,heads,tails)
        else:
            tails = tails + 1
            print "Attempt #{}: Throwing a coin... It's tails! ... Got {} head(s) so far and {} tail(s) so far".format(each,heads,tails)
    print "Ending the program. Thank you!"

toss()
