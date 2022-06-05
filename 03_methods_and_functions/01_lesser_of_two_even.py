def lesser_of_two_even(num1,num2):
    if (num1 % 2 == 0 ) and (num2 % 2 == 0):
        if num1 < num2:
            return num1
        else:
            return num2
    elif (num1 % 2 != 0) or (num2 %2 != 0):
        if num1 > num2:
            return num1
        else:
            return num2


c = lesser_of_two_even(6,5)
print(c)