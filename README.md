# forge-mods-server
## pre-task
[install curseforge](https://download.curseforge.com/)  
[install python3](https://www.python.org/downloads/)  
double-click on `pipenv-shell.bat` to open **virtual env**.  
## execute
### create server
create a modpack in curseforge, and play.  
in **virtual env**, key-in 
```cmd
python create_server.py
```
you will find the modpack you create.  
> `W`,`S` to move target, and `enter` to select.  

wait for a while, then a folder is opened.  
double-click `run-server.bat` inside it, and the server run  
### generate modlist
create a modpack in curseforge, and play.  
in **virtual env**, key-in 
```cmd
python generate_modlist.py
```
you will find the modpack you create.  
> `W`,`S` to move target, and `enter` to select.  

`modlist.json` generated, send it to your friend.  
### apply modlist
in **virtual env**, key-in  
```cmd
python apply_modlist.py
```
paste the content of `modlist.json`  
open minecraft launcher.  
