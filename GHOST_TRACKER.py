#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import requests
import time
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

# ===================== COLORS =====================
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Wh = '\033[1;37m'

# ===================== DECORATOR =====================
def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)
    return wrapper

# ===================== FUNCTIONS =====================

# IP Tracker
@is_option
def IP_Track():
    ip = input(f"{Wh}\n Enter IP target : {Gr}")  # INPUT IP ADDRESS
    print()
    print(f' {Wh}============= {Re}SHOW INFORMATION IP ADDRESS {Wh}=============')
    try:
        req_api = requests.get(f"http://ipwho.is/{ip}")
        ip_data = json.loads(req_api.text)
        time.sleep(1)
        lat = ip_data.get('latitude')
        lon = ip_data.get('longitude')
        google_map_url = f"https://www.google.com/maps/place/{lat},{lon}/@{lat},{lon},20z"
        osm_map_url = f"https://www.openstreetmap.org/?mlat={lat}&mlon={lon}#map=19/{lat}/{lon}"
        print(f"{Wh}\n IP target       : {Gr}{ip}")
        print(f"{Wh} Type IP         : {Gr}{ip_data.get('type')}")
        print(f"{Wh} Country         : {Gr}{ip_data.get('country')} {ip_data['flag']['emoji']}")
        print(f"{Wh} Country Code    : {Gr}{ip_data.get('country_code')}")
        print(f"{Wh} Continent       : {Gr}{ip_data.get('continent')}")
        print(f"{Wh} Continent Code  : {Gr}{ip_data.get('continent_code')}")
        print(f"{Wh} Region          : {Gr}{ip_data.get('region')}")
        print(f"{Wh} Region Code     : {Gr}{ip_data.get('region_code')}")
        print(f"{Wh} City            : {Gr}{ip_data.get('city')}")
        print(f"{Wh} Postal Code     : {Gr}{ip_data.get('postal')}")
        print(f"{Wh} Capital         : {Gr}{ip_data.get('capital')}")
        print(f"{Wh} Borders         : {Gr}{ip_data.get('borders')}")
        print(f"{Wh} EU              : {Gr}{ip_data.get('is_eu')}")
        print(f"{Wh}\n Latitude        : {Gr}{lat}")
        print(f"{Wh} Longitude       : {Gr}{lon}")
        print(f"{Wh}\n {Ye}🌍 Google Maps : {Gr}{google_map_url}")
        print(f"{Wh} 🗺 OpenStreetMap: {Gr}{osm_map_url}")
        print(f"\n{Wh} Calling Code    : {Gr}{ip_data.get('calling_code')}")
        print(f"{Wh} ASN             : {Gr}{ip_data['connection']['asn']}")
        print(f"{Wh} ORG             : {Gr}{ip_data['connection']['org']}")
        print(f"{Wh} ISP             : {Gr}{ip_data['connection']['isp']}")
        print(f"{Wh} Domain          : {Gr}{ip_data['connection']['domain']}")
        print(f"\n{Wh} Timezone        : {Gr}{ip_data['timezone']['id']} ({ip_data['timezone']['abbr']})")
        print(f"{Wh} DST             : {Gr}{ip_data['timezone']['is_dst']}")
        print(f"{Wh} Offset          : {Gr}{ip_data['timezone']['offset']}")
        print(f"{Wh} UTC             : {Gr}{ip_data['timezone']['utc']}")
        print(f"{Wh} Current Time    : {Gr}{ip_data['timezone']['current_time']}")
    except:
        print(f"{Re}[!] Failed to get IP details.")

# Phone Number Tracker
@is_option
def phoneGW():
    User_phone = input(
        f"\n {Wh}Enter phone number target {Gr}Example [+xxxxxxxxxxxxx] {Wh}: {Gr}")  # INPUT NUMBER PHONE
    default_region = None

    parsed_number = phonenumbers.parse(User_phone, default_region)  # VARIABLE PHONENUMBERS
    region_code = phonenumbers.region_code_for_number(parsed_number)
    jenis_provider = carrier.name_for_number(parsed_number, "en")
    location = geocoder.description_for_number(parsed_number, "id")
    is_valid_number = phonenumbers.is_valid_number(parsed_number)
    is_possible_number = phonenumbers.is_possible_number(parsed_number)
    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
    formatted_number_for_mobile = phonenumbers.format_number_for_mobile_dialing(parsed_number, default_region,
                                                                                with_formatting=True)
    number_type = phonenumbers.number_type(parsed_number)
    timezone1 = timezone.time_zones_for_number(parsed_number)
    timezoneF = ', '.join(timezone1)

    print(f"\n {Wh}========== {Gr}SHOW INFORMATION PHONE NUMBERS {Wh}==========")
    print(f"\n {Wh}Location             :{Gr} {location}")
    print(f" {Wh}Region Code          :{Gr} {region_code}")
    print(f" {Wh}Timezone             :{Gr} {timezoneF}")
    print(f" {Wh}Operator             :{Gr} {jenis_provider}")
    print(f" {Wh}Valid number         :{Gr} {is_valid_number}")
    print(f" {Wh}Possible number      :{Gr} {is_possible_number}")
    print(f" {Wh}International format :{Gr} {formatted_number}")
    print(f" {Wh}Mobile format        :{Gr} {formatted_number_for_mobile}")
    print(f" {Wh}Original number      :{Gr} {parsed_number.national_number}")
    print(
        f" {Wh}E.164 format         :{Gr} {phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)}")
    print(f" {Wh}Country code         :{Gr} {parsed_number.country_code}")
    print(f" {Wh}Local number         :{Gr} {parsed_number.national_number}")
    if number_type == phonenumbers.PhoneNumberType.MOBILE:
        print(f" {Wh}Type                 :{Gr} This is a mobile number")
    elif number_type == phonenumbers.PhoneNumberType.FIXED_LINE:
        print(f" {Wh}Type                 :{Gr} This is a fixed-line number")
    else:
        print(f" {Wh}Type                 :{Gr} This is another type of number")

# Username Tracker
@is_option
def TrackLu():
    username = input(f"\n {Wh}Enter Username : {Gr}")
    print(f"\n {Wh}========== {Re}USERNAME RESULTS {Wh}==========\n")

    social_media = [
        {"name": "Facebook", "url": f"https://www.facebook.com/{username}", "check": ["facebook", "id=\"pageTitle\""]},
        {"name": "Twitter", "url": f"https://www.twitter.com/{username}", "check": ["twitter.com", "profile"]},
        {"name": "Instagram", "url": f"https://www.instagram.com/{username}", "check": ["instagram", "profilePage"]},
        {"name": "LinkedIn", "url": f"https://www.linkedin.com/in/{username}", "check": ["linkedin.com", "profile"]},
        {"name": "GitHub", "url": f"https://github.com/{username}", "check": ["github", "followers"]},
        {"name": "GitLab", "url": f"https://gitlab.com/{username}", "check": ["gitlab", "projects"]},
        {"name": "Snapchat", "url": f"https://www.snapchat.com/add/{username}", "check": ["snapchat"]},
        {"name": "TikTok", "url": f"https://www.tiktok.com/@{username}", "check": ["tiktok"]},
        {"name": "Telegram", "url": f"https://t.me/{username}", "check": ["telegram"]},
        {"name": "YouTube", "url": f"https://www.youtube.com/@{username}", "check": ["youtube", "channel"]}
    ]

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
    }

    for site in social_media:
        try:
            r = requests.get(site["url"], headers=headers, timeout=8)
            page_text = r.text.lower()
            if r.status_code == 200 and any(ch.lower() in page_text for ch in site["check"]):
                print(f"{Re}[ + ] {site['name']} : {Gr}{site['url']}")
            else:
                print(f"{Re}[ - ] {site['name']} : {Wh}Not Found")
        except:
            print(f"{Ye}[ ! ] {site['name']} : Error")

# Show My IP
@is_option
def showIP():
    try:
        response = requests.get('https://api.ipify.org')
        print(f"\n {Wh}========== {Re}YOUR IP INFORMATION {Wh}==========")
        print(f"{Wh} Your IP : {Gr}{response.text}")
    except:
        print(f"{Re}[!] Unable to fetch IP.")

# ===================== MENU =====================
options = [
    {'num': 1, 'text': 'IP Tracker', 'func': IP_Track},
    {'num': 2, 'text': 'Show Your IP', 'func': showIP},
    {'num': 3, 'text': 'Phone Number Tracker', 'func': phoneGW},
    {'num': 4, 'text': 'Username Tracker', 'func': TrackLu},
    {'num': 0, 'text': 'Exit', 'func': exit}
]

# ===================== CORE =====================
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def call_option(opt):
    for option in options:
        if option['num'] == opt:
            option['func']()
            return
    raise ValueError('Option not found')

def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Re}+ {Wh}] {Gr}Press enter to continue')
        main()
    except ValueError:
        print(f"{Re}[!] Invalid Option")
        time.sleep(1)
        main()
    except KeyboardInterrupt:
        print(f"\n{Re}[!] Exit")
        exit()

def option_text():
    return ''.join([f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n' for opt in options])

def option():
    clear()
    stderr.writelines(f"""
       {Re}________               __      ______                __      
      / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__    
     / / __/ __ \\/ __ \\/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/    
    / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<       
    \\____/_/ /_/\\____/____/\\__/     /_/ /_/   \\__,_/\\___/_/|_|     

              [ + ]  GHOST - TRACKER  |  CODE BY AL-MARID  [ + ]    
    """)
    stderr.writelines(f"\n\n\n{option_text()}")

def run_banner():
    clear()
    time.sleep(0.3)
    stderr.writelines(f"""{Re}
         .-.    
       .'   `.          --------------------------------  
       :g g   :         |       GHOST - TRACKER -      |  
       : o    `.        |       @CODE BY AL-MARID      |  
      :         ``.     --------------------------------  
     :             `.    
    :  :         .   `.    
    :   :          ` . `.    
     `.. :            `. ``;    
        `:;             `:'    
           :              `.    
            `.              `.     .    
              `'`'`'`---..,___`;.-'  
        """)
    time.sleep(0.5)

def main():
    option()
    try:
        opt = int(input(f"{Wh}\n [ + ] {Re}Select Option : {Wh}"))
        execute_option(opt)
    except ValueError:
        print(f"{Re}[!] Please enter a number")
        time.sleep(1)
        main()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Re}[!] Exit")
        exit()
