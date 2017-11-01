from random import randrange


# Create a program that takes an IP address entered at the keyboard
# and prints out the number of segments it contains and the length of each segment.

# create function:
# finds number of segments
# finds the length of each segment

# find instances of "."
# initialize dot = "."
# start second search for "." => s.find(dot)
# initialize firstSecLen = s.find(dot) + 1
# Initialize secDot => s.find(dot, firstSecLen) + 1
# Initialize secSecLen = secDot - firstSecLen
# Init thirdDot = s.find(dot, secDot)
# and so on

# OR

# create a function that asks the user for sections of IP,
# counts the number of digits in each section
# and concatenates it

# ipAddress = "{}.{}.{}.{}".format(randrange(0, 255), randrange(0, 255), randrange(0, 255), randrange(0, 255))


# print(ipAddress)

def ip_info():
    ipType = input("How many digits does the first section of your IP address have? ")
    if ipType == "3":
        ip_section1 = input("What are the first three digits of your IP Address? ")
        section1_count = 1
        ip_section2 = input("What are the next three digits of your IP Address? ")
        section2_count = 1
        ip_section3 = input("What are the next three digits of your IP Address? ")
        section3_count = 1
        ip_section4 = input("What are the final three digits of your IP Address? ")
        section4_count = 1
        total_sections = section1_count + section2_count + section3_count + section4_count
        print("Your IP address is {}.{}.{}.{}".format(ip_section1, ip_section2, ip_section3, ip_section4))
        print("There are {} sections with {}, {}, {} and {} digits, respectively.".format(total_sections, len(ip_section1), len(ip_section2), len(ip_section3), len(ip_section4)))
    elif ipType == 4:
        ip_section1 = input("What are the first three digits of your IP Address? ")
        section1_count = 1
        ip_section2 = input("What are the next three digits of your IP Address? ")
        section2_count = 1
        ip_section3 = input("What are the next three digits of your IP Address? ")
        section3_count = 1
        ip_section4 = input("What are the final three digits of your IP Address? ")
        section4_count = 1
        ip_section5 = input("What are the first three digits of your IP Address? ")
        section5_count = 1
        ip_section6 = input("What are the next three digits of your IP Address? ")
        section6_count = 1
        ip_section7 = input("What are the next three digits of your IP Address? ")
        section7_count = 1
        ip_section8 = input("What are the final three digits of your IP Address? ")
        section8_count = 1
        total_sections = (section1_count + section2_count + section3_count + section4_count +
                          section5_count + section6_count + section7_count + section8_count)
        print("Your IP address is {}.{}.{}.{}".format(ip_section1, ip_section2, ip_section3, ip_section4))
        print("There are {} sections with {}, {}, {}, {}, {}, {}, {} and {} digits, respectively.".format(total_sections,
                                                                                          len(ip_section1),
                                                                                          len(ip_section2),
                                                                                          len(ip_section3),
                                                                                          len(ip_section4),
                                                                                          len(ip_section5),
                                                                                          len(ip_section6),
                                                                                          len(ip_section7),
                                                                                          len(ip_section8)))
    else:
        if 2 >= ipType >= 5:
            print("Invalid amount of numbers, please try again...or not")



ip_info()
