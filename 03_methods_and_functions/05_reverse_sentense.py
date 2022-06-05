def revers_sentense(sentense):
    list_string = sentense.split()
    rev_string = list_string[: :-1]
    d = ' '
    for item in rev_string:
        d = d + item + ' '
    return d

v = revers_sentense("We are ready for sport")
print(v)







