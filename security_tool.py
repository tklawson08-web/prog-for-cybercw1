# Task 1: Security tools 
# This task is a basic security tool for a small organisation
# After authentication is passed the user will be asked to pick between the following 
#1: Security Event counter
#2: Brute-Force simulation 
#3: Login authentication
#4: Exit

#All stored credentials are here and will be unchanged

STORED_USER = "admin"
STORED_PASS = "Security#223"
#Below are the max amount of login attempts that are allowed
MAX_LOGIN_TRYS = 3
#Below is the number of password entires allowed in Option 1 
EVENT_COUNTER_TIMES = 10
#Below is the percentage where an alert will be given anything higher or the same inccorect % will give an alert and lock the account
ALERT_MAX = 50
#below is the allowed number of guesses for the Brute Force Simulation
SIMULATION_MAX_ATTEMPTS = 5
SIMULATION_PASSWORD = "Cyberpass#20@26"

def ask_credentials():
    #ask the user for a username and password to be entered
    username = input("username:").strip()
    password = input("password:").strip()
    #This will return a tuple with both the username and password
    return username, password

def check_credentials(username,password: str) ->str:
    #this compares the entered pass and username from the user to the stored credentials and returns true if both are the same
    return username == STORED_USER and password == STORED_PASS

def run_login_trys():
    #allow the user to try to login with the max amount of login trys
    #this will return true if the user is authenticated properly 
    failed_logins = 0
    while failed_logins < MAX_LOGIN_TRYS:
        username, password = ask_credentials()
        if check_credentials(username, password):
            print("Authentication Passed: Welcome ")
            return True
        else:
            failed_logins += 1
            print(f"authentication has been failed. attenpts {failed_logins} of {MAX_LOGIN_TRYS}.")
    print("There was too many failed attempts to login. Therefore the account has been locked for 24 hours.")
    return False

def security_event_counter():
    #Option 1 Security Event counter this asks for a password 10 times and will count the amount of right and wrong attempts 
    # once the program has finish it will display the percentage of right and wrong trys and display an alert if the amount of inccorect attempts exceeds 50%

    correct_count = 0
    incorrect_count = 0

    for attempt in range(1, EVENT_COUNTER_TIMES + 1):
        user_pass = input(f"Enter password attempt Number: {attempt}/{EVENT_COUNTER_TIMES}):")
        if user_pass == STORED_PASS:
            correct_count += 1
        else:
            incorrect_count +=1
    wrong_percentage = (incorrect_count / EVENT_COUNTER_TIMES) * 100
    #displaying the amount of correct gueses incorrect guess and wrong percentage

    print(f"correct password amount: {correct_count}")
    print(f"Incorrect password amount: {incorrect_count}")
    print(f"Wrong amount percentage: {wrong_percentage}%")
    # if the percentage is more than 50 display an alert
    if wrong_percentage > ALERT_MAX:
        print("ALERT: There was a higher percentage than 50 of wrong passwords.")

def brute_force_sim():
    #Option 2 this allows the user to try and guess a predefined password and will stop once the password has been guessed or maximum number of attempts has been reached

    attempt = 0

    print(f"Try to guess the correct password you have {SIMULATION_MAX_ATTEMPTS} attempts")

    while attempt < SIMULATION_MAX_ATTEMPTS:
        pass_guess = input("Your guess: ")
        attempt += 1
        if pass_guess == SIMULATION_PASSWORD:
            print(f"The password has been guess and it took {attempt} attempts")
            return
        else:
            print("Incorrect guess please try again")
    print(f"Maximum attempts ({SIMULATION_MAX_ATTEMPTS}) has been reaches the Sim will now stop")

def login_authentication():
    #option 3 this allows for the user to enter a pair of credentials in order to authorize up to 3 tries 
    run_login_trys()

def menu():
    #This will print the security menu showinf the options
    print("\n ----Security Tools Menu ----")
    print("Option 1: Security Event Counter")
    print("Option 2: Brute-Force Sim")
    print("Option 3: Login authentication")
    print("Option 4: Exit")

def main():
    #In order to access the menu the user first must authenticate then the menu will keep running until the user decides to Exit
    print("---Security Tools---")
    print("In order to access the menu please authenticate")
    #if the authentication does not come back successful the account will be frozen therefore the menu will not show
    if not run_login_trys():
        return 

    while True:
        menu()
        try:
            Option = int(input("Please pick between the following Options (1-4):"))
            #This will deal with things that are not an integer input
        except ValueError:
            print("The Choice you have entered is not a valid input please enter a number between 1 to 4")
            continue

        if Option == 1:
            security_event_counter()
        elif Option ==2:
            brute_force_sim()
        elif Option ==3:
            login_authentication()
        elif Option ==4:
            print("Thank you for using this security tool and have a good day.")
            break
        else:
            print("the option you have picked is invalid please pick an option between 1 - 4")

    if __name__ == "__main__":
        try:
            main()
        except(EOFError, KeyboardInterrupt):
            #this will handle the close of the input stream by using crt+d or ctr+c
            print("Program has been interrupted")
            