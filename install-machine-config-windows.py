import requests
import sys
import os
import getpass
import platform

Username = getpass.getuser()
print ("User Name detected: " + Username)

ConfigFileName = "makerverse-config.txt"
AuthFileName = "aObiWwqtnQLlZdRqXc3iHMCrVoqHKW9Y.json"

WindowsLocations = ["C:\\Users\\" + Username + "\\.makerverse", "C:\\Users\\" + Username + "\\.makerverse-sessions\\" + AuthFileName]


configFile = requests.get("http://45.91.93.219/makerverse-config/makerverse-config.txt")
print ("Getting Machine Configuration from Server...")


AuthFile   = requests.get("http://45.91.93.219/makerverse-config/aObiWwqtnQLlZdRqXc3iHMCrVoqHKW9Y.json")
print ("Getting Machine Autherization token fron Server...")

#if(configFile.status_code == 200):
#  if(AuthFile.status_code == 200):
# Both Files have been downloaded - write them to their respective locations based on the OS parameter
config = open(WindowsLocations[0], "wb")
cookie = open(WindowsLocations[1], 'wb')
   
# Write the machine configuration files
print ("Writing to: " + WindowsLocations[0])
config.write(configFile.content)
print ("Writing to: " + WindowsLocations[1])
cookie.write(AuthFile.content)
config.close()
cookie.close()

print ("...Finished")
