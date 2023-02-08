from mcstatus import JavaServer

server = JavaServer.lookup("34.175.27.8")
status = server.status()
print(f"The server has {status.players.online} players and replied in {status.latency} ms")
latency = server.ping()
print(f"The server replied in {latency} ms")
query = server.query()
gameType=query.raw['gametype']
gameVersion=query.raw['version']
maxNumPlayers=query.raw['maxplayers']
numPlayers=query.raw['numplayers']
motdServer=query.raw['hostname']
mapName=query.raw['map']
pluginsInstalled=', '.join(query.raw['plugins'])
onlinePlayers=', '.join(query.players.names)
#query keys
#(['hostname', 'gametype', 'game_id', 'version', 'plugins', 'map', 'numplayers', 'maxplayers', 'hostport', 'hostip'])
