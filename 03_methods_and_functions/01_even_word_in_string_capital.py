##ashish
##aShIsH

def myfunc(string):
    i = 1
    b = ' '
    for word in string:
        if i % 2 == 0:
            word = word.upper()
        else:
            word = word.lower()
        b = b + word
        i = i + 1
    return b

c = myfunc("Anthropomorphism")
print(c)