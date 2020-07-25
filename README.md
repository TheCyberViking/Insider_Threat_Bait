# Insider_Threat_Bait
A tool for Baiting Insider Threats into running an exploit based off research conducted with Myself @ZepherFish, @TJNull, @ZoomerX 

The original Research can be found : https://blog.zsec.uk/cve-2020-1350-honeypoc/



## So how does this work
Build the CanaryToken - https://canarytokens.org/generate
Build the Script in python 
comiple it anyway you want - python script with obfiscated or exe complied with pyarmour 
Leave this sitting on your share to see who grabs it and runs it on their system against policy

Your IDS / IPS should alert when there is a request sent, this should alert you in two ways, One on your logs and two on your canary tokens such as browser date and time






# Brake Down the Code 
Here we will brake down the code to show you nothing malious here


## Modules
these are the rquired modules for this to run, using a tool like 

import time
import webbrowser
import requests
import sys


## Function to Offer Fake Menu and CVE
in this section you can see the menu works and to atempt to make it look like a real scanner

def main():
        print("CVE-2020-1350 Vulnerablity Scanner by @TheCyberViking, @ZepherFish, @TJ_Null, @ZoomerX")
        print("This is in attempt to scan and open the link to prove exploitation")
        print(".")
        ip = input("Please Enter the IP you wana scan: ")
        print(".")
        print("Now Testing For CVE-2020-XXXX on:" + ip)
        print("Now Scanning Address")
        time.sleep(3)
        print(ip + " Apeears to be Vulnerable Opening Test Page Now")
        time.sleep(2)


## Troll Link
This section is the link that will open for the subject when they run the code, you can change the link it directs to a troll video

        webbrowser.open_new('https://www.youtube.com/embed/gMpLLq7DomQ?start=0&fs=1&autoplay=1')
        time.sleep(2)
 
 
## Hidden CanaryToken
This section will request and alert the CanaryToken after you add your URL in in the section TargetURL
        
        targeturl = (" ENTER YOUR CanaryTokens URL")
        response = requests.get(targeturl, verify=False, timeout=2)
        
        
## Response codes
Here you can see how the responses are handeled from the CanaryToken

        if response.status_code == 200:
                sys.stdout.write("\033[1;31m")
                print("CAUGHT See HR Soon or they will see you")
        elif response.status_code == 404:
                sys.stdout.write("\033[0;32m")
                print(".")


## Run Code
This section will run the code defined in the function

main()
