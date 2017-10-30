from random import randrange


# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains and the length of each segment.

ipAddress = "123.0.0.1"


#  or

def IP_info(ip):
    segCount = 0
    totalCount = 0
    for i in range(0, len(ip)):
        if ip[i] in '.':
            segCount + 1
            break
        else:
            if ip[i] != ".":
                totalCount + 1

IP_info("{}.{}.{}.{}".format(randrange(100, 199), randrange(100, 199), randrange(100, 199), 1))

