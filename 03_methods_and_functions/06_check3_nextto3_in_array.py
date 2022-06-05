def has33(list1):
    for i in range (len(list1) + 1):
        if list1[i] == 3 and list1[i+1] == 3:
            return True
        else:
            return False

a = has33([3, 1, 3])
print(a)
