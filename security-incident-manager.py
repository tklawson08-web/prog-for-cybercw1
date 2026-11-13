#Task 4 Security Incident Manager
#This program will be able to store aswell as also update information in it about a security incident by using a dictionary.

#This first part of the code will create a dictionary 

incident = {
    "User": "Tlawson",
    "IP_address": "192.168.6.24",
    "event_type": "Login Failure",
    "risk": "Low",
}


#This nextpart will displat the username aswell as the IP address that was in the icident report
print("username:", incident["User"])
print("ip address", incident["IP_address"])

#the next part will create a new part to the dictionary called status
incident["status"] = "Open"

#This next part will update the risk level of the incident
incident["risk"] = "High"
print("The risk level has been upadate to high")

#this removes the field event_type
incident.pop("event_type")
print("The removed field was 'event_type'")

#this next part will display all of the remaining key and values
print("Remaining key and values of the report")
for key , value in incident.items():
    print(f"{key}: {value}")

#this last part will display the total number of key-value pairs.

print("Total number of key-value pairs ", len(incident))
