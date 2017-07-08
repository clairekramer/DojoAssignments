def coinToss():
    print 'Starting the program...'
    heads = 0
    tails = 0
    for x in range(1,5001):
        import random
        num = round(random.random())
        if num == 1:
            heads = heads + 1
            print "Atempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(x,heads,tails)
        else:
            tails = tails + 1
            print "Atempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(x,heads,tails)
    print 'Ending the program, thank you!'

coinToss()
