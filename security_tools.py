#Security_tools
#This program is a reusable cyber security functions 
#this consists of a password validation an IP address checker and a Password generator 

import random 
import string

#Below are the symbols that will be accepted and used in passwords 
ALLOWED_SYMBOLS = "!()+=_-%#@$[]:;,.<>?/{}"
#below is the minumum allowed length for passwords 
MIN_LENGTH = 10

def validation(password):
    #this function will check if the password has more or the min length for the password
    #the password also must consist of atleast one letter one number and symbol in order to make it strong

    #if password does not meet the min length then it is sent back false 
    if len(password) < MIN_LENGTH:
        return False
#this part checks to make sure that the password has atleasr a letter a number and symbol
    letter = any(char.isalpha() for char in password)
    number = any(char.isdigit() for char in password)
    symbol = any(char in ALLOWED_SYMBOLS for char in password)

    return letter and number and symbol

def valid_ip(ip: str) ->str:
    #This part of the program will just check the ip to make sure it is valid 
    #like the previous task it will check for exactly three dots and four sections that have numbers between 0-255

    ip = ip.strip()
    if ip.count(".") != 3:
        return False
    sections = ip.split(".")
    if len(sections) != 4:
        return False
#this will check if it has any empty part of the ip or not 0 to 255
    for section in sections:
        if not section.isdigit() or not 0 <= int(section) <= 255:
            return False
    return True

def password_generator():
    #this function will generate a strong password all randomly but will always have Uppercases, lowercase, numbers and symbols in order to make it secure 
    length= random.randint(10, 16)
#this part will pick a random thing from each topic in order to strengthen the security of the password
    chars = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(ALLOWED_SYMBOLS),

    ]
#this will constantly add randon char numbers and symbols until the length that was randomly generated is met
    all_characters = string.ascii_letters + string.digits + ALLOWED_SYMBOLS
    while len(chars)< length:
        chars.append(random.choice(all_characters))
#in order to make sure the uppercases, lowercases and sumbols and numberss are not always at the start of the password
    random.shuffle(chars)
    return "".join(chars)
