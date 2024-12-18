#!/data/data/com.termux/files/usr/bin/env python

'''
#************************************************************#
#                         Wallpaper                          #
#                            by                              #
#                         Khoj AI                            #
#------------------------------------------------------------#
#     Generate Wallpaper based on Weather, User Activities   #
#------------------------------------------------------------#
#        KHOJ_API_KEY=<your_key> python Wallpaper.py         #
#------------------------------------------------------------#
#         Khoj will generate a personalized wallpaper        #
#       using local weather, moon phase and your notes       #
#************************************************************#
'''

# Import libraries
# ----------------
import platform
import sys
import os
from os.path import expanduser
import subprocess
from datetime import datetime
import requests
import urllib.parse


# Initialize Variables
# ----------------
# Environment
# Khoj server URL
khoj_host = os.getenv("KHOJ_HOST", "https://app.khoj.dev")
# Khoj API Key used to access the Khoj API to generate wallpaper
khoj_api_key = os.getenv("KHOJ_API_KEY")
# Only generate wallpaper when KHOJ_GENERATE_WALLPAPER is set to true
khoj_should_generate_wallpaper = os.getenv("KHOJ_GENERATE_WALLPAPER", "true").lower() == "true"
# Only generate info notification when KHOJ_INFO_NOTIFY is set not set to true
khoj_info_notify = os.getenv("KHOJ_INFO_NOTIFY", "true").lower() == "true"

# General
chat_name = "Paint"
current_time = datetime.now().strftime("%H:%M")
default_prompt = f"""
Create a personalized painting using the local weather and my recent experiences.
The time is {current_time}.
- Search online for the current weather here (in SI units).
- If it is night, search online for the moon phase here.
- Search my personal notes for ONLY my experiences from the last 2 days and nothing else (use date filters).
- Do NOT perform any weather, moon phase related search in my notes or documents.

Use the above information to create a hyper-local, deeply personal painting for me. I'll use it as my phone's wallpaper.
""".strip()
standard_wallpaper_path = expanduser("/tmp/khoj_wallpaper.png")

# Platform
# Android Termux variables
termux_wallpaper_path = expanduser(os.getenv("WALLPAPER_PATH", standard_wallpaper_path.lower()))
termux_wallpaper_update = "termux-wallpaper -f \"{0}\"; termux-wallpaper -l -f \"{0}\";"
termux_notification = "termux-toast \"{}\""
# Mac variables
mac_wallpaper_path = expanduser(os.getenv("WALLPAPER_PATH", standard_wallpaper_path))
# Note: ensure mac wallpaper settings have "show on all spaces" enabled to update wallpaper on all desktops
mac_wallpaper_update = "osascript -e 'tell application \"System Events\" to tell every desktop to set picture to \"{}\" as POSIX file'"
mac_kill_wallpaper_agent = f"cp \"{os.path.dirname(os.path.realpath(__file__))}/KhojWallpaper.plist\" \"{expanduser('~/Library/Application Support/com.apple.wallpaper/Store/Index.plist')}\"; killall WallpaperAgent;"
mac_notification = "osascript -e 'display notification \"{}\" with title \"🏕️ Khoj\"'"


# Create Functions
# ----------------
def get_platform():
    "Get platform the script is running on"
    os = platform.system().lower()
    if os == "darwin":
        return "mac"
    elif os == "linux" and 'com.termux' in expanduser("~/"):
        return "android"
    elif os == "linux":
        return "linux"
    elif os == "windows":
        return "windows"
    else:
        return "unknown"

def get_platform_commands():
    "Get platform specific commands"
    platform = get_platform()
    if platform == "mac":
        return mac_notification, mac_wallpaper_update, mac_wallpaper_path
    elif platform == "android":
        return termux_notification, termux_wallpaper_update, termux_wallpaper_path
    else:
        return None, None, None

def generate_image(prompt):
    "Ask Khoj to generate image"
    question = urllib.parse.quote(prompt)
    headers = {'Authorization': f'Bearer {khoj_api_key}'}

    # Get Location Details
    city, region, country = get_location()

    # Construct URL with prompt and location
    url = f'{khoj_host}/api/chat'
    json = {
        "q": question,
        "title": chat_name,
        "city": city,
        "region": region,
        "country": country,
    }
    print(f"Request: {url}, {json}")

    # Ask Khoj to generate image from prompt
    response = requests.post(url, headers=headers, json=json)
    print(f"Response: {response.text}")

    # Extract URL of Generated Image from Chat Response
    data = response.json()
    return data["images"][0] if len(data.get("images", [])) > 0 else None

def run(command):
    "Run command in shell"
    return subprocess.check_output(command, shell=True)

def get_location():
    "Get my current location based on I.P"
    # Get my current location from I.P
    headers = {'User-Agent': 'Mozilla/5.0 (Android)'}
    response = requests.get("https://ipapi.co/json", headers=headers)

    # Check if the request was successful
    if response.status_code != 200:
        notification, _, _ = get_platform_commands()
        run(notification.format("🏕️ Khoj Wallpaper: Could not get location"))
        return None, None, None

    # Parse the JSON response
    data = response.json()

    # Extract the desired fields
    city = data['city']
    region = data['region']
    country = data['country_name']
    return city, region, country

# Main Function: Generate Image from Prompt & render as Wallpaper
def update_wallpaper(prompt):
    "Generate and set wallpaper"
    # Get Platform Specific Variables, Commands
    notification, wallpaper_update, wallpaper_path = get_platform_commands()

    if khoj_should_generate_wallpaper:
        # Generate Image from Prompt
        print(f"1. Generating Wallpaper from Prompt: {prompt}")
        if khoj_info_notify:
            run(notification.format(f"🏕️ Khoj Painting Wallpaper"))
        image_url = generate_image(prompt)
        if not image_url: return

        # Download Generated Wallpaper
        print(f"2. Downloading generated Image at: {image_url}")
        img_response = requests.get(image_url)
        if not img_response: return
        with open(wallpaper_path, "wb") as f:
            f.write(img_response.content)

    # Set Wallpaper on Device
    print(f"3. Set New Wallpaper at: {wallpaper_path}")
    if get_platform() == "mac":
        if wallpaper_path != standard_wallpaper_path: run(f"cp {wallpaper_path} {standard_wallpaper_path}")
        run(wallpaper_update.format(standard_wallpaper_path))
        run(mac_kill_wallpaper_agent)
    else:
        run(wallpaper_update.format(wallpaper_path))
    if khoj_info_notify:
        run(notification.format(f"🏕️ Khoj Pasted Wallpaper on Screen"))

def generate():
    "Main entrypoint for the script"
    prompt = default_prompt if len(sys.argv) != 2 else sys.argv[1]
    update_wallpaper(prompt)


# Run the main function
# ---------------------
if __name__ == "__main__":
    generate()
