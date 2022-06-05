for num in range(1,100):
    if (num % 3 == 0) and (num % 5 == 0):
        print(f"The {num} is FIZZBUZZ")
    elif num % 3 == 0:
        print(f"The {num} is FIZZ")
    elif num %5 == 0:
        print(f"The {num} is BUZZ")
    else:
        print(num)
