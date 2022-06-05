##takes a two-word string and returns True if both words begin with same letter
def animal_crackers(str1,str2):
    if str1[0] == str2[0]:
        return True
    else:
        return False


b = animal_crackers('Crazy','Kangaroo')
print(b)