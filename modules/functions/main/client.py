'''
CONNECTION HANDLER FOR THE APPLICATION
'''
import paramiko

class Client(object):
    '''
    Creates a client for the SSH connection with our target host.\n
    #[ARGS]\n
    * hostname = SERVER ADDRESS [*],\n
    * username = USER TO CONNECT WITH [opt],\n
    * password = USER PASSWORD FOR SSH [opt],\n
    * key_filename = IF ASYNC CONNECTION, GIVE KEY [opt],\n
    * port = 22 [DEFAULT]\n
    '''
    def __init__(self,
                 hostname:str,
                 username:str = None,
                 key_filename:str = None,
                 password:str = None,
                 port:int = 22,
                 ):
        self.username=username
        self.hostname=hostname
        self.key_filename=key_filename
        self.password=password
        self.port=port
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

###==========================================================================================================================###
#=============================================== SERVER PRIME SET UP ==========================================================#
###==========================================================================================================================###

    #Close/Disconnect from host
    def Close(self):
        '''
        Closes connection to server
        '''
        return self.client.close()

    #Connects to the host
    def Connect(self) -> object:
        '''
        Connects to server
        '''
        return self.client.connect(username=self.username, hostname=self.hostname, key_filename=self.key_filename, password=self.password)
            
    # Executes command
    def ExecCommand(self, command:str) -> str:
        '''
        Executes a remote command into SSH Host.
        '''
        out=[]
        if command == "":
            raise ValueError("No commands were given")
        stdin, stdout, stderr = self.client.exec_command(command, get_pty=True)
        if stdout.channel.recv_exit_status() == 0:
            for line in iter(stdout.readlines, ""):
                if line != []:
                    for i in line:
                        return f"{i}"
                else:
                    break
        else:
            print(f"ERROR DURING COMMAND EXECUTION: (StatusCode {stdout.channel.recv_exit_status()})\n")
            for line in iter(stdout.readlines, ""):
                if line != []:
                    for i in line:
                        return f"{i}"
                else:
                    break
                
###==========================================================================================================================###
#================================================= SERVER CONTROL =============================================================#
###==========================================================================================================================###
    
    def open_ports(self, port:int) -> str:
        '''
        Opens host given port
        '''
        try:  
            return self.ExecCommand(f"sudo ufw allow {port}/tcp")
        except:
            return (TypeError, "Error during opening ports.")

    def close_ports(self, port:int) -> str:
        '''
        Closes host given port
        '''
        try:  
            return self.ExecCommand(f"sudo ufw deny {port}/tcp")
        except:
            return (TypeError, "Error during opening ports.")
        
    def custom_command(self, command:str) -> str:
        '''
        Runs a custom command on host. \n
        For those cases a command is not defined.
        '''
        try:
            return self.ExecCommand(command)
        except:
            return (TypeError, "Error during command execution.")
