import os
import base64
import random
import requests
import threading

from colorama import Fore
from os.path import isfile, join




def change_pfp():

    tokens = open('tokens.txt', 'r').read().splitlines()
    token = random.choice(tokens)

    picture = [f for f in os.listdir("avatars/") if isfile(join("avatars/", f))]
    random_picture = random.choice(picture)

    with open(f'avatars/{random_picture}', "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())

    headers = {
        'authority': 'discord.com',
        'accept': '*/*',
        'accept-language': 'en-GB,en;q=0.9',
        'authorization': token,
        'cookie': '__dcfduid=904754d01e0f11edbc8e137cc7c473ca; __sdcfduid=904754d11e0f11edbc8e137cc7c473caaf269406fe90d738955d66c8929cd997a08c8669ef42a295aac84cc43230a150; __cf_bm=uXHYoYl9KmWotP8UeGBa6PejMQCeibzDkDYmf2MsY9s-1660728773-0-AS+XIQ7NNSyCZ4NlcXTdL0oVGueHXZdj2D0+lSifopWh7sUykquNKC/lA3UpNMqVrjBh728hF1wibQBsBEFv69LTkEam4T1CLerS8v2rjGVq0ZwVEPXbnDz7iPfEX8AvEA==; locale=en-GB',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/@me',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'x-discord-locale': 'en-GB',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEwNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTA0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjE0MjAwMCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=',
    }

    json = {
        'avatar': f"data:image/png;base64,{(encoded_string.decode('utf-8'))}",
    }

    r = requests.patch('https://discord.com/api/v9/users/@me', headers=headers, json=json)
    if r.status_code == 200:
        print(f"{Fore.GREEN}Profile updated{Fore.RESET} | {token[0:30]}********************************")
    else:
        print(f"{Fore.RED}Error{Fore.RESET}")


threads = input("Enter amount of profiles to change > ")
for i in range(int(threads)):
    threading.Thread(target=change_pfp).start()
