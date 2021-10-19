import os 
import subprocess
import sys 
import time 
from discord_webhook import DiscordWebhook
import requests 

hwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
r = requests.get("Website Here With List Of Whitelisted Hwids")

discordname = input("Your Discord Username For Contact > ")

def printSlow(text):
    for char in text:
        print(char, end="")
        sys.stdout.flush()
        time.sleep(.1)

def Main_Program():
    if hwid in r.text:
        printSlow("Hwid Success | You Have Access!")
        time.sleep(.1)
    else:
        print("Hwid Error! | Your Hwid Has Not Been Whitelisted!")
        print("Please Contact Merkz-Dev#0001 With Your Hwid | Hwid: " + hwid)
        os.system('pause >NUL')

webhook = DiscordWebhook(url='Webhook To Log Hwid And Discord Username', content='Hwid > ' + hwid + '\n' + 'Contact Information | Discord Username > ' + discordname)
response = webhook.execute()

if __name__ == "__main__":
    Main_Program()
