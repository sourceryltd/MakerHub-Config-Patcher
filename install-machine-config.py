import requests
import sys
import os
import getpass
import platform

Username = getpass.getuser()
ConfigFileName = "makerverse-config.txt"
AuthFileName = "aObiWwqtnQLlZdRqXc3iHMCrVoqHKW9Y.json"

LinuxLocations = ["/home/" + Username + "/.makerverse", "/home/" + Username + "/.makerverse-sessions/" + AuthFileName]
MacOSLocations = ["/Users/" + Username + "/.makerverse", "/Users/" + Username + "/.makerverse-sessions/" + AuthFileName]
WindowsLocations = ["C:\\Users\\" + Username + "\\.makerverse", "C:\\Users\\" + Username + "\\.makerverse-sessions\\" + AuthFileName]
LinuxNames = ["Linux", "Ubuntu", "4.", "5."]
WindowsNames = ["Windows", "windows", "10", "11"]

configFile = requests.get("https://raw.githubusercontent.com/sourceryltd/MakerHub-Config-Patcher/main/makerverse-config.txt")
print ("Getting Machine Configuration from Server...")


AuthFile   = requests.get("https://raw.githubusercontent.com/sourceryltd/MakerHub-Config-Patcher/main/aObiWwqtnQLlZdRqXc3iHMCrVoqHKW9Y.json")
print ("Getting Machine Autherization token fron Server...")

while (True):
      if(configFile.status_code == 200):
        if(AuthFile.status_code == 200):
           # Both Files have been downloaded - write them to their respective locations based on the OS parameter
         
           for x in range(len(LinuxNames) -1):
               if(platform.system() == LinuxNames[x]):
                 print ("Linux Detected...")
                 config = open(LinuxLocations[0], "wb")
                 cookie = open(LinuxLocations[1], 'wb')
                 # Write the machine configuration files
                 config.write(configFile.content)
                 cookie.write(AuthFile.content)
                 config.close()
                 cookie.close()
         
                 print ("...Finished")
                 quit()           

           for x in range(len(WindowsNames) -1):
               if(platform.system() == WindowsNames[x]):
                 print ("Windows OS Detected...")
                 config = open(WindowsLocations[0], "wb")
                 cookie = open(WindowsLocations[1], 'wb')

                 # Write the machine configuration files
                 config.write(configFile.content)
                 cookie.write(AuthFile.content)
                 config.close()
                 cookie.close()
         
                 print ("...Finished")
                 quit()

           if(platform.system() == "Darwin"):
                 print ("MacOS Detected...")
                 config = open(MacOSLocations[0], "wb")
                 cookie = open(MacOSLocations[1], 'wb')

                 # Write the machine configuration files
                 config.write(configFile.content)
                 cookie.write(AuthFile.content)
                 config.close()
                 cookie.close()
         
                 print ("...Finished")
                 quit()
           print ("Platform could not be identified.")
           quit()      
                 
