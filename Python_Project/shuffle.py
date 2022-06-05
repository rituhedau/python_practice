from random import shuffle
def shuffel_list(list1):
    shuffle(list1)
    return list1

def user_input():
    guess = ' '
    while guess not in ['0','1','2']:
        guess = input("Enter your guess 0,1 and 5: ")
    return int(guess)

def check_guess(list1,guess):
    if list1[guess] == 0:
        print("Your guess is right!")
    else:
        print("Wrong Guess")
        print("Right guess is : ", list1)

##list input
mylist = [' ',0,' ']

#shuffel list
mixed_list = shuffel_list(mylist)

#user_input
guess = user_input()

#check guess
check_guess(mixed_list,guess)
