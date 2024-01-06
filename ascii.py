import string
def check(a):
    for letter in a:
        if letter not in string.ascii_uppercase:
            return False
    return True
value="This is my sample program"
print(value,": ",check(value))
value1="thisismysampleprogram"
print(value1,": ",check(value1))
value2="THISISMYSAMPLEPROGRAM"
print(value2,": ",check(value2))
value3="THIS IS MY SAMPLE PROGRAM"
print(value3,": ",check(value3))
