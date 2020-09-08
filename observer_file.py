#!/usr/bin/env python3
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import re
import getkey as getkey

import os
import json
import time
import getpass

list_of_roz = ['mp4', 'mp3', 'jpg', 'png', 'pdf', 'xlsx', 'docx', 'jpeg']

class MyHandler(FileSystemEventHandler):

    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            try: 
                roz = re.findall("\.([a-zA-Z0-9]+)$",filename)[0]
                if roz in list_of_roz:
                    src = folder_to_track + "/" + filename
                    new_destination = folder_destination + roz + "/" + filename
                    os.rename(src,new_destination)
            except:
                pass


user = getpass.getuser()
folder_to_track = "/Users/{}/Desktop/dow".format(user)
folder_destination = "/Users/{}/Desktop/dow/download_".format(user)

if False == os.path.exists(folder_to_track):
    os.mkdir(folder_to_track)

for roz in list_of_roz:
    if False == os.path.exists(folder_destination + roz):
        os.mkdir(folder_destination + roz)

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler,folder_to_track, recursive = True)
observer.start()

try:
    while True:
        time.sleep(10)

except KeyboardInterrupt:
    observer.stop()
observer.join()