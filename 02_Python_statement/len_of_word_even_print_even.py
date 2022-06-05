st = 'Print every word in this sentence that has an even number of letters'
for word in (st.split()):
    if len(word) % 2 == 0:
        print(f"The len of {word} is even")
    else:
        print(f"the len of {word} is odd")