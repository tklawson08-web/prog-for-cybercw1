#Task 3 IP address Validator 
#This program will preform a forman check on an ip address by using different string operations 


def ip_validation(ip_address: str) ->str:
    #this function will check if an IP has the normal IPv4 format
    #it does this by doing different checks such as removing any kind of uneccessary spaces 
    #making sure that the address contains the 3 dots 
    #it will also check that there are 4 number parts between the dots and that numbers are between the range of 0 to 255 as thats the max and min a IP can contain 
    
    #this will remove the spaces within the ip and replace it with no space
    ip_address = ip_address.strip().replace(" ","")

    #This will check that the address does infact include dots and 3 of them and if it doesnt it will return false  
    if "." not in ip_address or ip_address.count(".") != 3:
        return False

    #this next part will split the part inbetween the dots and we expect there to be exactly 4 parts as is in a ip address
    
    sections = ip_address.split(".")
    if len(sections) != 4:
        return False

    for section in sections:
        #Each different section must contain only digits and the program will reject it if its type in string form or if nothing is entered or negative numbers
        if not section.isdigit():
            return False
        #This next part checks if each of the numbers is between the range of 0-255 as an ip address can have no less or no more
        if int(section) < 0 or int(section) > 255:
            return False
    return True


def main(): 
    #Here the user is asked to enter an ip address and the program will display it if it passes all the checks
    try:
        ip =input("Please enter a Valid Ip address")
    except (EOFError, KeyboardInterrupt):
        print("The input has been cancelled by the user")
        return 
    if ip_validation(ip):
        print("The IP address that has been entered has passed all checks and is valid.")
    else:
        print("the IP address that was entered is an Invalid IP address")

if __name__ =="__main__":
    main()
