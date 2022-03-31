import tkinter as tk
from tkinter import filedialog
import os
from os import path
import json

setting={}
if path.exists('setting.json'):
    with open('setting.json') as f:
        try:
            setting=json.load(f)
        except:
            print('setting.json can\'t be parsing!')

if 'minecraft' not in setting or not path.exists(setting['minecraft']):
    root=tk.Tk()
    root.withdraw()
    launch=filedialog.askopenfilename(
        title='minecraft launcher profiles (json)',
        initialdir=path.join(os.getenv('APPDATA'),".minecraft"),
        initialfile="launcher_profiles.json"
    )
    setting['minecraft']=launch
else:
    launch=setting['minecraft']

with open('setting.json','w') as f:
    json.dump(setting,f)

client=path.dirname(launch)

data=json.loads(input('input modlist: '))
version=data['v']
mods=data['mods']
url="https://maven.minecraftforge.net/net/minecraftforge/forge/{0}/forge-{0}-installer.jar".format(version)

import requests
def download(url,filepath):
    res=requests.get(url,allow_redirects=True)
    open(filepath,'wb').write(res.content)

insfile=f'forge-{version}-installer.jar'
print(f'Downloading {insfile}')
download(url,insfile)
os.system(f'java -jar {insfile}')
if path.exists(path.join(client,'mods')):
    import shutil
    shutil.rmtree(path.join(client,'mods'))
os.mkdir(path.join(client,'mods'))

for mod in mods:
    print(f'Downloading {path.basename(mod)}')
    download(mod,path.join(client,'mods',path.basename(mod)))
print('Finish')
os.system('pause')
