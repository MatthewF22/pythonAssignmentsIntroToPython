# Assignment 8 - marquee sequence
# Matthew Franklin 10-31-2022
def get_next_marquee(aString):
    """Returns a string with the first character of aString put at the end"""
    return aString[1:] + aString[0]


def second_get_next_marquee(num, aString2):
    """Returns number determines how many characters from the front are moved to the back of aString"""
    """Returns the string value afterwords"""
    return aString2[num:] + aString2[0:num]


def isValid(text, displaySize):
    """Validates that the display size is 5 and total length of the message"""
    return displaySize >= 5 and displaySize < len(text)


def main():
    message = "This is a long string of characters"
    size = int(input("Enter a whole number display size: "))
    ###Loop to determine if the display size is valid, will continue to ask for new value if invalid
    while not isValid(message, size):
        size = int(input("Enter a valid whole number display size: "))
    ###newMessage uses the user input and determine the characters to use based on that value and the original message
    newMessage = message[0:]
    z = 0
    ###for loop to print out the original marquee sequence
    while z < len(message):
        print(newMessage[0:size])
        newMessage = get_next_marquee(newMessage)
        z += 1
    ###This is the few print statements for the second get marquee function
    print(second_get_next_marquee(2 ,"hello"))
    print(second_get_next_marquee(6, "This is a test"))
    print(second_get_next_marquee(15, "Did you know you have rights? The constitution says you do!"))
    print(second_get_next_marquee(34, "My momma always said life was like a box of chocolates You never know what youre gonna get"))


main()