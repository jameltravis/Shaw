
number = "9,223,373,036,854,775,807"
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]

newNumber = int(cleanedNumber)
print("the number is {} ".format(newNumber))

# augmented assignment is the '+=' thing.
# look at the example below:

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x //= 4
print(x)

# as you can see, augmented assignment is math then assign to left variable


