#Task 2 Security Event Logger 
#This task will ask the user to enter a username and password up until the correct credentials are entered and will then print an event log for each attempts 
#both failed and success 

import random 
from datetime import datetime 

#All the credentials will be stored here and remain unchanged 
CORRECT_USER ="admin"
CORRECT_PASS ="CorrectPass@123"

#This will be the makeup ip address of the machine that will be making these logins
IP_ADDRESS = "192.168.2.34"

def generate_event():
    #this will generate an event id for the log and will return a random 4 digit number 

    return random.randint(1000,9999)

def event_log(username, event_info: str) -> str:
    #this will print an event log entry and add it

    #it will use username for the username in the attempt 
    #the event info will be used in order to see if it was a succesfull of failed login attempt
    #this will display the time of the event through the Year, month ,day ,hour ,minute and seconds
    timestamp = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print("\n ---Event Log---")
    print(f"ID: {generate_event()}")
    print(f"username: {username}")
    print(f"Ip address: {IP_ADDRESS}")
    print(f"Event info: {event_info}")
    print(f"Timestamp: {timestamp}")

def main():
    #The program will keep asking for the credentials until they are correct and with log each attempt that is made by the user
    print("Event Logger")
    attempt = 0

    while True: 
        try:
            username = input("Please enter Username").strip()
            password = input("Please enter the password").strip()
            #the code below will alow the useer to close the input stream by using ctr+c
        except (EOFError, KeyboardInterrupt):
            print("Inputs have been cancelled")
            break 

        attempt +=1

        if username == CORRECT_USER and password == CORRECT_PASS:
            info = ("Successful login")
            event_log(username,info)
            print(f"Login has succeded after {attempt} attempts")
            break 

        else:
            event_log(username, "Failed login attempt")
            print("The incorrect credentials have been entered please try and enter them again")


if __name__ == "__main__":
    main()
    
            

