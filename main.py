#main.py
#This program uses the security_tools in order to check a password and the ip address.

import security_tools

def main():
    #This will ask the user to provide an IP address along with a password it will then check to see id they are valid and then display the results
    print("------ Cyber Utilities ------")

    try:
        password = input("Please enter a valid password")
        ip = input("Please enter a valid IP address")
    except (EOFError, KeyboardInterrupt):
        print("The input has been cancelled by the user")
        return 

    #this part will check the password using the module function from security tools 
    if security_tools.validation(password):
        print("the password is strong and secure")
    else:
        print("The password is quite weak you should have (10+ characters with a letter, number and a symbol to make it stronger)")
        #this next part will suggest a strong password using the generator from security tools
        print("A strong password we would suggest:", security_tools.password_generator())

    #check the ip address that the user entered by using the valid ip function from securtiy tools
    if security_tools.valid_ip(ip):
        print("the IP address you have entered is a valid IP")
    else:
        print("The IP address that you have entered is not a valid IP")


if __name__ =="__main__":
    main()
    