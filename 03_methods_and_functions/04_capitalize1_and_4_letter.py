def old_macdonald(string):
    i = 1
    a = ''
    for word in string:
        if i == 1 or  i == 4:
            word = word.upper()
        a = a + word
        i = i + 1
    return  a

c = old_macdonald("ashish")
print(c)

