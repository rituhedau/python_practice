st = 'Print only the words that start with s in this sentence Same'

sp = st.split()
print(sp)
for item in sp:
    if item[0] == 's'or item[0] == "S":
        print(item)