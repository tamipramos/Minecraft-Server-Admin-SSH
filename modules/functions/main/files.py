'''
FILES HANDLER POR THE APPLICATION
'''
import os, sys, re, json, string

class Files():
    '''
    Administrates all files within the server.\n
    [ARGS]\n
    installLocation = where is this script located,\n
    settings = User settings file,\n
    serverSettings = Default settings file,\n 
    '''
    def __init__(self, installLocation, serverSettings, sshConfig):
        # Defines install location
        self.installLocation=installLocation
        # Defines where is the properties file 
        self.serverPropertiesDestination=self.installLocation+"/server.properties"
        # Defines SSH Destination
        self.sshConfigurationDestination=self.installLocation+"/settings.json"
        # Defines user's settings
        self.settings={}
        # Defines SSH config
        self.sshConfiguration=sshConfig
        # Defines default settings
        self.serverSettings=serverSettings
        
        # Variables
        ## Array to convert json inputs into Minecraft-type config syntax 
        self.dictAppend=[]
        ## Defines current config
        self.curr={}
      
    def createSettings(self):
        '''
        Creates a Minecraft-Readable config file with the given information.
        '''
        # Opens/Creates "server.properties"
        f = open(self.serverPropertiesDestination, "w")
        # Writes it blank
        f.write("")
        f.close()
        # Appends to "server.properties" the current config
        f = open(self.serverPropertiesDestination, "a")
        # For KEY in all keys in default settings config, do:
        for key_name in self.serverSettings.keys():
            # Tries to set the config we have configured previously
            try:
                self.curr[key_name] = self.settings[key_name]
            # When no key if found in the settings, take the value in the default config.
            except:
                self.curr[key_name] = self.serverSettings[key_name]
            # After each cicle, appends the "curr" value and it's key to the "dictAppend"
            finally:
                self.dictAppend.append(str(key_name)+"="+str(self.curr[key_name])+"\n")
        # For each entry in "dictAppend", writes in our file "server.properties" the whole line
        for line in self.dictAppend:
            f.write(line)
            
    def editConfig(self, file:str, old:str|int, new:str|int):
        '''
        Edits the configuration files of the server.
        '''
        # Read in the file
        with open(file, 'r') as f :
            filedata = f.read()
            # Split the lines
            for line in filedata.split("\n"):
                # Search for the required string
                if re.search(fr'\"\b{old}\b\"', line):
                    x = re.search(rf'\"\b{old}\b\"', line)
        # Replace the target string
        try:
            # Minecraft file
            # Splits the content in two fields like "FIELD" = "FIELD" to grab the minecraft conf file
            # and threat it as plain text.
            if "=" in filedata:
                # if the value is a string... (avoid INT problem: no .lower() function)
                if type(new) == str:
                    # normalize the booleans as strings
                    if new.lower() == "true" or new.lower() == "false":
                        new=new.lower()
                # Replace in the variable "filedata" the found value asociated to the key we searched before (old variable)
                # and fix the code to make it fit with the minecraft manager like "KEY"="VALUE"
                filedata = filedata.replace(x.string, f'{x.string.split("=")[0]}={new}')
            else:
                # If something went wrong, redirect the work flow to the "except"
                raise Exception
        except:
            try:
                
            # JSON
            # Splits the content in two fields like "FIELD" : "FIELD" to grab the json
            # and threat it as plain text.
                if ":" in filedata:
                    # if the value is a string... (avoid INT problem: no .lower() function)
                    if type(new) == str:
                        # normalize the booleans as strings [To keep the synergy of the code]
                        if new.lower() == "true" or new.lower() == "false":
                            # [lower case] add a pair of quotation marks and comma to the string to avoid type errors
                            new=str('"'+new.lower()+'"'+",")  
                        elif not string.digits in new:
                            # [insensitive] if there are no numbers, add quotation marks and comma
                            new=str('"'+new+'",')
                    else:
                        # if INT, just add a last comma
                        new=str(new)+","
                # Replace in the variable "filedata" the found value asociated to the key we searched before (old variable)
                # like "KEY":"VALUE"
                    filedata = filedata.replace(x.string, f'{x.string.split(":")[0]}:{new}')
            except:
                # When the both options fails, raise error
                raise TypeError("Couldnt modify the config files.")
        
        # Write the file out again and save "filedata" variable
        with open(file, 'w') as f:
            f.write(filedata)

    def getConfig(self, file:str, key:str|int):
        '''
        Get the configuration files of the server.
        '''
        # Read in the file
        with open(file, 'r') as f :
            filedata = f.read()
            # Split the lines
            for line in filedata.split("\n"):
                # Search for the required string
                if re.search(fr'\"\b{key}\b\"', line):
                    x = re.search(fr'\"\b{key}\b\"', line)
        # Replace the target string
        try:
            # Minecraft file
            if "=" in filedata:
                # if not empty
                if not "":
                    try:
                        # split the found string and take the "value" field. Then split the quotations marks and commas
                        # to clean the output.
                        return x.string.split("=")[1].split('"')[1].split(",")[0]
                    except:
                        try:
                            # if there are no commas or quotations marks, just split the equals sign.
                            return x.string.split("=")[1]
                        except:
                            # if something fails, raise error and continue the working flow to the except.
                            raise TypeError("Something went wrong.")
                else:
                    # if empty, return empty
                    return ""
            else:
                # if not "=" in our string
                raise Exception
        except:
            try:
            # JSON
                if ":" in filedata:
                    # if not empty
                    if not "":
                        try:
                                # split the found string and take the "value" field. Then split the quotations marks and commas
                                # to clean the output. We will match only the first coincidence. => directory problems 
                                # ("KEY" : "C:/.../.../") if we dont put delimitations, output will be "C", and not "C:/.../.../"
                                return x.string.split(":",1)[1].split('"')[1].split(",")[0]
                        except:
                            try:
                                    # if there are no quotation marks, split without
                                    return  x.string.split(":",1)[1].split(",")[0]
                            except:
                                # if something fails continue the workflow
                                raise TypeError("Something went wrong.")
                    else: 
                        # if empty, return empty
                        return ""
            except:
                # if all fail, raise error
                raise TypeError("Couldnt access the config files.")
    def create_startup_file():
        settings='''
{
    "serverConfig":
        {
            "name": "",
            "hostname":"",
            "username":"",
            "port":"",
            "password":"",
            "private_key":"",
        },
        
    "serverProperties":
        {
            "enable-jmx-monitoring":"false",
            "rcon.port":25575,
            "level-seed":1234567890,
            "gamemode":"survival",
            "enable-command-block":"false",
            "enable-query":"false",
            "generator-settings":{},
            "enforce-secure-profile":"true",
            "level-name":"world",
            "motd":"Hola2",
            "query.port":"false",
            "pvp":"false",
            "generate-structures":"true",
            "max-chained-neighbor-updates":1000000,
            "difficulty":"easy",
            "network-compression-threshold":256,
            "max-tick-time":60000,
            "require-resource-pack":"false",
            "use-native-transport":"false",
            "max-players":20,
            "online-mode":"true",
            "enable-status":"true",
            "allow-flight":"false",
            "initial-disabled-packs":"",
            "broadcast-rcon-to-ops":"true",
            "view-distance":10,
            "server-ip":"jejeje",
            "resource-pack-prompt":"",
            "allow-nether":"true",
            "server-port":25565,
            "enable-rcon":"false",
            "sync-chunk-writes":"true",
            "op-permission-level":4,
            "prevent-proxy-connections":"false",
            "hide-online-players":"false",
            "resource-pack":"",
            "entity-broadcast-range-percentage":100,
            "simulation-distance":10,
            "rcon.password":"",
            "player-idle-timeout":0,
            "force-gamemode":"false",
            "rate-limit":0,
            "debug":"false",
            "hardcore":"false",
            "white-list":"false",
            "broadcast-console-to-ops":"true",
            "spawn-npcs":"true",
            "spawn-animals":"true",
            "function-permission-level":2,
            "initial-enabled-packs":"vanilla",
            "level-type":"minecraft\\\\:normal",
            "text-filtering-config":"",
            "spawn-monsters":"true",
            "enforce-whitelist":"false",
            "spawn-protection":16,
            "resource-pack-sha1":"",
            "max-world-size":29999984
        }
        
}
'''
        f = open('./config/settings.json', 'w')
        f.write(settings)
        f.close()