from modules.functions.main import client, files
import sys, time
import modules.gui.gui as gui

###==========================================================================================================================###
#================================================== INITIALIZATION ============================================================#
###==========================================================================================================================###

#grabs current script's directory
current_dir=sys.path[0]

#grabs config file
data = eval(open(current_dir+'/config/settings.json', 'r').read())

#defines variable for each configuration
global serverConf, serverProperties
serverConf = data['serverConfig']
serverProperties = data['serverProperties']

#current setting=NULL
#curr={}


# for each config in config file, try to set it up
#for option_name in ['name', 'hostname', 'port', 'username','password', 'private_key']:
#    try:
#        curr[option_name] = serverConf[option_name]
#    except:
#        raise TypeError("Something bad happened trying to grab some config files.")


###==========================================================================================================================###
#================================================== APP HANDLER ===============================================================#
###==========================================================================================================================###
def update_config_files():
    data = eval(open(current_dir+'/config/settings.json', 'r').read())
    serverConf = data['serverConfig']
    serverProperties = data['serverProperties']
    return serverConf, serverProperties


#create main files
F=files.Files(current_dir+'/config', serverProperties, serverConf)
#F.editConfig(file=F.sshConfigurationDestination, old="server-ip", new="jejeje")
#Start App  
app=gui.Main(serverConf, F)
#server = client.Client(hostname=curr['hostname'], username=curr['username'], password=curr['password'], key_filename=curr['private_key'])
#server.Connect()
#print(server.close_ports(8080))
#print(server.ExecCommand("pwd"))

# Spawn infinite time the window
app.mainloop()
