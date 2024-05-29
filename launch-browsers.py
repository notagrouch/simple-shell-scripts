#!/usr/bin/env python3

import subprocess
import webbrowser
import os
from datetime import datetime

# Define log directory and file
LOG_DIR = "/var/log"
if not os.access(LOG_DIR, os.W_OK):
    LOG_DIR = os.path.expanduser("~/log")
LOG_FILE = os.path.join(LOG_DIR, "open_browsers.log")

# Ensure log directory exists
os.makedirs(LOG_DIR, exist_ok=True)

# Logging function
def log_message(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"{timestamp} - open_browsers.py - {message}\n"
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry)
    print(log_entry, end="")

# Get URL from user
url = input("Enter the URL: ").strip()

# Validate URL
if not url:
    log_message("No URL entered. Exiting.")
    exit(1)

log_message(f"URL set to {url}")

# Function to open URL in a browser
def open_browser(browser_name, command, options):
    log_message(f"Opening {url} with {browser_name} in private/incognito mode.")
    try:
        subprocess.Popen([command] + options + [url])
    except FileNotFoundError as e:
        log_message(f"Failed to open {browser_name}: {e}")
    except Exception as e:
        log_message(f"An error occurred while opening {browser_name}: {e}")

# Open URL in various browsers
browsers = [
    ("Google Chrome", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", ["--new", "--args", "-incognito"]),
    ("Firefox", "/Applications/Firefox.app/Contents/MacOS/firefox-bin", ["-private-window"]),
    ("Opera", "/Applications/Opera.app/Contents/MacOS/Opera", ["-private"]),
    ("Vivaldi", "/Applications/Vivaldi.app/Contents/MacOS/Vivaldi", ["--incognito"]),
    ("Brave", "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser", ["--incognito"]),
    ("Safari", "open", ["-na", "Safari", "--args", "-private"]),
    ("Microsoft Edge", "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge", ["--inprivate"])
]

for browser_name, command, options in browsers:
    open_browser(browser_name, command, options)

log_message("All browsers have been opened with the URL.")
