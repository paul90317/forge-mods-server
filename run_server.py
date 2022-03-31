import os
from os import path
import re

flag=False
if path.exists('eula.txt'):
    with open('eula.txt','r') as f:
        data=f.read()
        try:
            if data.index('true'):
                flag=True
        except:
            flag=False
if not flag:
    with open('eula.txt','w') as f:
        f.write('eula=true')

dir=[filename for filename in os.listdir('.') if path.exists(filename)]
for filename in dir:
    if re.match('forge-\d+\.\d+\.\d+-\d+\.\d+\.\d+\.jar',filename) != None:
        server=filename
        break

def load_env(filename:str):
    data=open(filename,'r').readlines()
    ret={}
    for line in data:
        key,val=line.replace('\n','').split('=')
        ret[key]=val
    return ret
def dump_env(m:dict,filename:str):
    with open(filename,'w') as f:
        for key in m:
            f.write(f'{key}={m[key]}\n')
if path.exists('env.txt'):
    try:    
        envjson=load_env('env.txt')
        javapath=envjson['java']
        mem=envjson['mem']
    except:
        print('env.txt can\'t be parse!')
        javapath='java'
        mem=4
        dump_env({'java':javapath,'mem':mem},'env.txt')
else:
    javapath='java'
    mem=4
    dump_env({'java':javapath,'mem':mem},'env.txt')

os.system(javapath+f" -Xmx{mem}G -Xms{mem}G -jar {server} nogui")
os.system('pause')