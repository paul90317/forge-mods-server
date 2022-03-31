import os
from os import path
import json

client=path.join(os.getenv('APPDATA'),".minecraft")

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