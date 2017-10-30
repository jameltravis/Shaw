# for i in range(1,20):
#     print("i is now {}".format(i))

# number = "1,234,567,8910"
# for i in range(0, len(number)):
#     print(number[i])

number = "1,234,567,8910"
cleanedNumber = ''


# newNumber = int(cleanedNumber)
# # print("the number is {} ".format(newNumber))
#
# for char in number:
#     if char in '0123456789':
#         cleaned number = cleanedNumber + char

for char in number:
    if char in '0123456789':
        cleanedNumber = cleanedNumber + char

newNumber = int(cleanedNumber)

for state in ["not pinin'", "no more", "an invisible member", "a stiff", "bereft of life"]:
    print("This parrot is " + state)
    # print("This parrot is {}".format(state))

for i in range(0, 100, 5):
    print("i is {} ".format(i))

for i in range(1, 13):
    for j in range(1, 13):
        print("{1} times {0} is {2}".format(i, j, i*j))
    print("===================")



