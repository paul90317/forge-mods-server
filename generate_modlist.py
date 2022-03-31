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
    data=[d['installedFile']['downloadUrl'] for d in data['installedAddons']] 


import json
json.dump({'mods':data,'v':version},open('modlist.json','w'))