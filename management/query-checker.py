#!/bin/python3
import subprocess, requests, sys, os

headers = {'Accept': 'application/json'}
url = f"https://api.mcsrvstat.us/2/{sys.argv[1]}"
resp = requests.get(url, headers=headers)
resp= resp.json()
ip={}
port={}
debug={}
motd={}
players={}
version={}
online={}
protocol={}
array=[]
_ON=False
for key in resp.keys():
        if key == "ip":
                ip=resp[key]
                array.append([key,ip])
        if key == "port":
                port=resp[key]
                array.append([key, port])
        if key == "debug":
                debug=resp[key]
                array.append([key, debug])
        if key == "motd":
                motd=resp[key]
                array.append([key, motd])
        if key == "players":
                players=resp[key]
                array.append([key, players])
        if key == "version":
                version=resp[key]
                array.append([key, version])
        if key == "online":
                online=resp[key]
                array.append([key, online])
                if online == False:
                        _ON=False
                else:
                        _ON=True
        if key == "protocol":
                protocol=resp[key]
                array.append([key, protocol])
while not _ON:
        print("[X] El servidor está offline.")
        print("[!] Reinicializando servidor...")
        result = subprocess.run(['screen', '-ls'], stdout=subprocess.PIPE)
        if 'No Sockets' in result.stdout.decode('utf-8'):
                subprocess.run('screen -S minecraft', shell=True, executable="/bin/bash")
        subprocess.run('screen -S minecraft -p 0 -X stuff "/home/tamipramos/forge/run.sh^M"',shell=True, executable="/bin/bash")
        os.system('/home/tamipramos/forge/logger.sh "Reinicializando servidor."')
        _ON=True
if _ON:
        print("[*] El servidor está online.")
        os.system('/home/tamipramos/forge/logger.sh "Servidor iniciado." status')




