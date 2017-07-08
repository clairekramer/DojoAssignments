def grade():
    print 'Scores and Grades'
    for val in range(10):
        import random
        score = random.randint(0,100)
        if score >= 90:
            print 'Score: {}; Your grade is A'.format(score)
        elif score >= 80:
            print 'Score: {}; Your grade is B'.format(score)
        elif score >= 70:
            print 'Score: {}; Your grade is C'.format(score)
        elif score >= 60:
            print 'Score: {}; Your grade is D'.format(score)
        else:
            print 'Score: {}; Your grade is F'.format(score)
    print 'End of the program. Bye!'

grade()
