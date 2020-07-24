import time
import webbrowser
import requests
import sys


def main():
        print("CVE-2020-1350 Vulnerablity Scanner by @TheCyberViking, @ZepherFish, @TJ_Null, @ZoomerX")
        print("This is in attempt to scan and open the link to prove exploitation")
        print(".")
        ip = input("Please Enter the IP you wana scan: ")
        print(".")
        print("Now Testing For CVE-2020-5902 on:" + ip)
        print("Now Scanning Address")
        time.sleep(3)
        print(ip + " Apeears to be Vulnerable Opening Test Page Now")
        time.sleep(2)
        webbrowser.open_new('https://www.youtube.com/embed/gMpLLq7DomQ?start=0&fs=1&autoplay=1')
        time.sleep(2)
        targeturl = ("canarytokens")
        response = requests.get(targeturl, verify=False, timeout=2)
        if response.status_code == 200:
                sys.stdout.write("\033[1;31m")
                print("CAUGHT See HR Soon")
        elif response.status_code == 404:
                sys.stdout.write("\033[0;32m")
                print("CAUGHT See HR Soon")
main()
