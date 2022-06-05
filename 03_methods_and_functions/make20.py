def makes_twenty(num1,num2):
    if num1 == 20 or num2 == 20:
        return True
    elif num1 + num2 == 20:
        return True
    else:
        return False

c = makes_twenty(10,10)
print(c)