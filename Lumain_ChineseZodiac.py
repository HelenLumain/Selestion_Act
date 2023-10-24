#This program will will find a Chinses Zodiac Sign in a given year

name = input("What is your name?")
age = int(input("How old are you?"))

print("Full name, ", name)
print("Age, ", age)
while True: 
    try:
        chineseZodiac = int(input("Enter your birth year: "))
    except ValueError:
        print('Please enter a valid year')
        continue 
    else: 
        break 
    
    
if chineseZodiac % 12 == 0:
    print('Your Chinese Zodiac is monkey, ')
if chineseZodiac % 12 == 1:
    print('Your Chinese Zodiac is Rooster, ')
if chineseZodiac % 12 == 2:
    print('Your Chinese Zodiac is Dog, ')
if chineseZodiac % 12 == 3:
    print('Your Chinese Zodiac is Pig, ')
if chineseZodiac % 12 == 4:
    print('Your Chinese Zodiac is Rat, ')
if chineseZodiac % 12 == 5:
    print('Your Chinese Zodiac is Ox, ')
if chineseZodiac % 12 == 6:
    print('Your Chinese Zodiac is Tiger, ')
if chineseZodiac % 12 == 7:
    print('Your Chinese Zodiac is Rabit, ')
if chineseZodiac % 12 == 8:
    print('Your Chinese Zodiac is Dragon, ')
if chineseZodiac % 12 == 9:
    print('Your Chinese Zodiac is Snake, ')
if chineseZodiac % 12 == 10:
    print('Your Chinese Zodiac is Horse, ')
if chineseZodiac % 12 == 11:
    print('Your Chinese Zodiac is Goat, ')
