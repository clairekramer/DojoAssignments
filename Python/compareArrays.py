def compare(list_one,list_two):
    count = 0
    if len(list_one) != len(list_two):
        count =+ 1
    for val in range(0,len(list_one)):
        if list_one[val] != list_two[val]:
            count =+ 1
        else:
            continue
    if count == 0:
        print "The lists are the same"
    else:
        print "The lists are not the same"

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

compare(list_one,list_two)
