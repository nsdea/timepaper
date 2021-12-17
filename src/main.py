from configuration import *

import os
import time
import subprocess

hour = int(time.strftime('%H'))

image_list = sorted([int(x.split('.')[0]) for x in os.listdir(IMAGES)], reverse=True)

for i in image_list:
    if hour >= i:
        image = i
        break

if hour <= min(image_list):
    image = max(image_list)

def set_background(path: str):
    cmd = f'gsettings set org.gnome.desktop.background picture-uri file://{IMAGES}{image}.png'
    print(subprocess.check_output(cmd, shell=True).decode('utf-8').strip())

set_background(f'{IMAGES}{image}.png')

# cmd = f'gsettings set org.gnome.desktop.background picture-uri file://{IMAGES}{image}.png'
# print(f'[TIMEPAPER | INFO] Generated command: {cmd}')

# #ran = subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
# ran = os.system(cmd)

# print(f'[TIMEPAPER | INFO] Command output: {ran}')