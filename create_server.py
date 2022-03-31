import tkinter as tk
from tkinter import filedialog
import os
from os import path
import json
import keyboard  # using module keyboard
setting={}
if path.exists('setting.json'):
    with open('setting.json') as f:
        try:
            setting=json.load(f)
        except:
            print('setting.json can\'t be parsing!')

server_script=open('run_server.py','r').read()

if 'curseforge' not in setting or not path.exists(setting['curseforge']):
    root=tk.Tk()
    root.withdraw()
    launch=filedialog.askopenfilename(
        title='curseforge launcher profiles (json)',
        initialdir=path.join(os.environ['USERPROFILE'],"curseforge\minecraft\Install"),
        initialfile="launcher_profiles.json"
    )
    setting['curseforge']=launch
else:
    launch=setting['curseforge']

with open('setting.json','w') as f:
    json.dump(setting,f)

with open(launch) as f:
    data=json.load(f)
    data=data['profiles']

tmp=[]
for key in data:
    if data[key]['type']=='custom':
        tmp+=[data[key]]
data=tmp
index=0
changed=True
while True:
    if changed:
        changed=False
        os.system('cls')
        for i in range(len(data)):
            if index==i:
                print('[*]',data[i]['name'])
            else:
                print('[ ]',data[i]['name'])
    if keyboard.is_pressed('w') and index>=1:
        index-=1
        changed=True
    if keyboard.is_pressed('s') and index<len(data)-1:
        index+=1
        changed=True
    if keyboard.is_pressed('\n'):
        gameDir=data[index]['gameDir']
        break

with open(path.join(gameDir,'minecraftinstance.json'),'r',encoding='utf-8') as f:
    data=json.load(f)

version=f"{data['gameVersion']}-{data['baseModLoader']['forgeVersion']}"
url="https://maven.minecraftforge.net/net/minecraftforge/forge/{0}/forge-{0}-installer.jar".format(version)

import requests
def download(url,filepath):
    res=requests.get(url,allow_redirects=True)
    open(filepath,'wb').write(res.content)

root=tk.Tk()
root.withdraw()
root.attributes('-topmost', True)
serverpath=filedialog.askdirectory()
print('Creating Server at',serverpath)

inspath=f"forge-{version}-installer.jar"
modspath_src=path.join(gameDir,'mods')
print('Downloading installer from',url)
os.chdir(serverpath)
download(url,inspath)
os.system(f'java -jar {inspath} --installServer')
import shutil
print('Copying Mods...')
shutil.copytree(modspath_src,'mods',dirs_exist_ok=True)
print('Creating server script (run_server.py)')
open('run_server.py','w').write(server_script)
print('finish')

import subprocess
subprocess.Popen('explorer .')

os.system('pause')
