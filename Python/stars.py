#Part 1
def draw_stars(x):
    for each in x:
        str = ""
        for star in range(each):
            str+='*'
        print str

x = [4,6,1,3,5,7,25]
draw_stars(x)

#Part 2
def draw_stars2(x):
    for each in x:
        if type(each) == int:
            print "*" * each
        if type(each) == str:
            print each[0].lower() * len(each)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
draw_stars2(x)
