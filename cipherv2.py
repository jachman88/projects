#This is the a basic cipher written in Python2 written using functions/methods
#This will take a string of text and a key from a user
#And it will encrypt or decrypt the users message

message = raw_input("please enter in your message: ")
key = len(raw_input("Please enter in your passphrase: "))
action = raw_input("Would you like to Encrypt (e) or Decrypt (d) your message? ")

#method that converts letters to there ASCII value and then changes that value using the provided key.
def convert (message, key):
    if action == "d":
        key = -key
    numMessage=""
    for letter in message[::1]:
        letter = ord(letter) + key
        numMessage += letter.__str__()
    return numMessage

#method that converts ASCII values to letters
def numToLetter():
    counter = 0
    numMessage = convert(message, key)
    messageLenght = len(numMessage)
    new_letter = ""
    new_message = ""
    while counter <= messageLenght -1:
        value = numMessage[counter]
        if value == "1":
            new_value = numMessage[counter] + numMessage[counter + 1] + numMessage[counter + 2]
            new_letter = int(new_value)
            new_message = new_message + chr(new_letter)
            counter += 3
        else:
            new_value = numMessage[counter] + numMessage[counter + 1]
            new_letter = int(new_value)
            new_message = new_message + chr(new_letter)
            counter += 2
    return new_message


numToLetter()


raw_input("\n\nPress any key to Exit!")



