import json
import time
from datetime import datetime as dt

# open settings.json file with read permission only
settings = json.load( open( "settings.json", "r" ) )

# import settings from settings.json file
test_host = "hosts"

hosts_path = settings["hosts_path"]
redirect = settings["redirect"]
block = tuple(settings["blocked_websites"])

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 18, 20) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 7):
        print("Working time")
        
        with open(hosts_path, "r+") as file:
            content = file.read()
            for website in block:
                if website in content:
                    pass
                else:
                    file.write(f"{redirect} {website}\n")
    else:
        print("fun time")
        with open(hosts_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block):
                    file.write(line)
            file.truncate()
    time.sleep(5)