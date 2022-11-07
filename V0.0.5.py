import os, platform, time
print('Checking Updates...')
time.sleep(2)
os.system('git pull')
os.system('xdg-open https://t.me/AWM_TEAMPRO')
time.sleep(2)
os.system('xdg-open https://facebook.com/groups/termux.command.awm/')
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    import Random
    Random()



