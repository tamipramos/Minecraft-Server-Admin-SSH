'''
GRAPHIC HANDLER FOR THE APPLICATION
'''
import sys, os, math, requests, markdown, tkhtmlview
# getting the name of the directory where this file is present.
current = os.path.dirname(os.path.realpath(__file__))
# Getting the parent directory name where the current directory is present.
parent = os.path.dirname(current)
# adding the parent directory to the sys.path.
sys.path.append(parent)

import customtkinter, tkinter, tkinter.messagebox
from PIL import Image
from tkinter import filedialog
import functions.main.files as files
import functions.main.client as client
from gui.widgets.Custom_Widgets import Custom_Toplevel

#C:\Users\tamip\AppData\Local\Programs\Python\Python310\lib\site-packages\customtkinter\windows\widgets\theme THEMES
#C:\Users\tamip\AppData\Local\Programs\Python\Python310\Lib\site-packages\customtkinter\assets\themes THEMES

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue", custom_theme

class Main(customtkinter.CTk):
    '''
    Main Window of the program.
    [ARGS]\n
    * sshConfig = CURRENT SETTINGS
    '''
    def __init__(self, sshConfig, fileSystem):
        super().__init__()
        #Hide window on startup
        self.withdraw()
         # Event Closing
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(text="Would you like to close the administrator?")) 
        # Init
        self.sshConfig=sshConfig
        self.fileSystem=fileSystem
        self._SERVERNAME=(str(sshConfig['name']) + f" | " + str(sshConfig['hostname'] + ":" + str(sshConfig['port'])))
        self.title(self._SERVERNAME)
        self.server = client.Client(hostname=None,
                                   port=22,
                                   username=None, 
                                   password=None, 
                                   key_filename=None)
        self.url='https://raw.githubusercontent.com/tamipramos/tamipramos.github.io/main/README.md'
        self.patchNotes=requests.get(self.url)
        #print(markdown.markdown(text=self.patchNotes.content.decode('utf-8')))
        # Center window spawn
        self.w = 1100
        self.h = 580
        self.ws = self.winfo_screenwidth()
        self.hs = self.winfo_screenheight()
        self.x = (self.ws/2) - (self.w/2)
        self.y = (self.hs/2) - (self.h/2)
        self.background="#1a1a1a"
        # configure window
        self.geometry('%dx%d+%d+%d' % (self.w, self.h, self.x, self.y))

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


###==========================================================================================================================###
#================================================== NAVIGATION ================================================================#
###==========================================================================================================================###
        # create navigation frame
        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text=self._SERVERNAME,
                                                             compound="left", 
                                                             font=customtkinter.CTkFont(size=15, weight="bold"))
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)
        
        #indexes
        self.index_home=1
        self.index_configuration=2
        self.index_server_admin=3
        self.index_settings=26
        
        #Menus content arrays
        self.home_sub_nav_array=[]
        self.settings_sub_nav_array=[]
        self.server_admin_sub_nav_array=[]
        self.configuration_sub_nav_array=[]

        
#:::::::::::::::::::#        
#:::::::# HOME NAV
#:::::::::::::::::::#
        # HOME
        self.home_nav = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, 
                                                   border_spacing=10, text="Home",
                                                   border_color="#3B8ED0",
                                                   #fg_color="transparent", 
                                                   #text_color=("gray10", "gray90"), 
                                                   #hover_color=("#597807"),
                                                   anchor="w", command=self.home_button_event, 
                                                   state="normal")
        self.home_nav.grid(row=self.index_home, column=0, sticky="ew")
        
        ## HOME-MONITORING
        self.home_monitoring_nav = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, 
                                                   border_spacing=10, text="     Monitoring",
                                                   border_color="#3B8ED0",
                                                   #fg_color="transparent", 
                                                   #text_color=("gray10", "gray90"), 
                                                   #hover_color=("#597807"),
                                                   anchor="w", command=self.home_monitoring_button_event, 
                                                   state="normal")

#:::::::# HOME ARRAY
        self.home_sub_nav_array.append(self.home_monitoring_nav)
#:::::::::::::::::::#        
#:::::::# CONFIGURATION NAV
#:::::::::::::::::::#
        # CONFIGURATION
        self.configuration_nav = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, 
                                                      border_spacing=10, text="Configuration",
                                                      border_color="#3B8ED0",
                                                      #fg_color="transparent", 
                                                      #text_color=("gray10", "gray90"), 
                                                      #hover_color=("#597807"),
                                                      anchor="w", command=self.configuration_button_event, 
                                                      state="normal")
        
        self.configuration_nav.grid(row=self.index_configuration, column=0, sticky="ew")
        ## CONFIGURATION-SERVER CONFIG
        self.configuration_server_config_nav = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, 
                                                   border_spacing=10, text="     Server Configuration",
                                                   border_color="#3B8ED0",
                                                   #fg_color="transparent", 
                                                   #text_color=("gray10", "gray90"), 
                                                   #hover_color=("#597807"),
                                                   anchor="w", command=self.configuration_server_config_button_event, 
                                                   state="normal")

#:::::::# CONFIGURATION ARRAY
        self.configuration_sub_nav_array.append(self.configuration_server_config_nav)
#:::::::::::::::::::#        
#:::::::# SERVER ADMIN NAV
#:::::::::::::::::::#
        # SERVER ADMIN
        self.server_admin_nav = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, 
                                                      border_spacing=10, text="Server Administration",
                                                      border_color="#3B8ED0",
                                                      #fg_color="transparent", 
                                                      #text_color=("gray10", "gray90"), 
                                                      #hover_color=("#597807"),
                                                      anchor="w", command=self.server_admin_button_event, 
                                                      state="normal")
        
        self.server_admin_nav.grid(row=self.index_server_admin, column=0, sticky="ew")
#:::::::# SERVER ADMIN ARRAY
        #self.server_admin_sub_nav_array.append()
#:::::::::::::::::::#        
#:::::::# SETTINGS NAV
#:::::::::::::::::::#
        # SETTINGS
        self.settings_nav = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, 
                                                       border_spacing=10, text="Settings",
                                                      border_color="#3B8ED0",
                                                      #fg_color="transparent", 
                                                      #text_color=("gray10", "gray90"), 
                                                      #hover_color=("#597807"),
                                                      anchor="w", command=self.settings_button_event, 
                                                      state="normal")
        
        self.settings_nav.grid(row=self.index_settings, column=0, sticky="ew")
#:::::::# SETTINGS ARRAY
        #self.settings_sub_nav_array.append()
#:::::::::::::::::::#
###==========================================================================================================================###
#====================================================== FRAMES ================================================================#
###==========================================================================================================================###
        #############
        ### PATCH ###
        #############
        #PATCH NOTES
        self.patch_notes_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.patch_notes_frame.grid_rowconfigure(0, weight=1)
        self.patch_notes_text_box = tkhtmlview.HTMLLabel(master=self.patch_notes_frame, 
                                                         background=self.background, 
                                                         html=markdown.markdown(text=self.patchNotes.content.decode('utf-8'))
                                                         .replace("<p>", '<p style="color:white">')
                                                         .replace("<h1>", '<h1 style="color:white">')
                                                         .replace("<h2>", '<h2 style="color:white">')
                                                         .replace("<h3>", '<h3 style="color:white">'))
        
        self.patch_notes_text_box.pack(expand=1, fill="both", padx=20, pady=20)
        

        ############
        ### HOME ###
        ############
        
        #HOME
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid_columnconfigure(1, weight=1)
        self.home_frame.grid_rowconfigure(6, weight=1)
        self.home_frame_button_1 = customtkinter.CTkButton(self.home_frame, text="LANZAR ECHO", command=self.boton)
        self.home_frame_button_1.grid(row=0, column=2, padx=20, pady=20)
        
        ##HOME-MONITORING
        self.home_monitoring_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_monitoring_frame.grid_columnconfigure(1,weight=1)
        self.home_monitoring_frame.grid_rowconfigure(10, weight=1)
        self.home_monitoring_button = customtkinter.CTkButton(self.home_monitoring_frame, text="MODO MONITOR", command=lambda: print("MONITOR"))
        self.home_monitoring_button.grid(row=0, column=0, padx=20, pady=20)
        
        #######################
        ###  CONFIGURATION  ###
        #######################
        
        #CONFIGURATION
        self.configuration_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.configuration_frame.grid_columnconfigure(1, weight=1)
        self.configuration_frame.grid_rowconfigure(40, weight=1)
        self.configuration_frame_button_1 = customtkinter.CTkButton(self.configuration_frame, text="CONFIGURATION", command=self.boton)
        self.configuration_frame_button_1.grid(row=4, column=1, padx=20, pady=20)
        
        #CONFIGURATION-SERVER CONFIGURATION
        self.configuration_server_config_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.configuration_server_config_frame.grid_columnconfigure(1, weight=1)
        self.configuration_server_config_frame.grid_rowconfigure(40, weight=1)
        self.configuration_server_config_frame_button_1 = customtkinter.CTkButton(self.configuration_server_config_frame, text="SERVER CONFIGURATION", command=self.boton)
        self.configuration_server_config_frame_button_1.grid(row=10, column=1, padx=20, pady=20)
        
        ######################
        ###  SERVER ADMIN  ###
        ######################
        
        #SERVER ADMIN
        self.server_admin_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.server_admin_frame.grid_columnconfigure(1, weight=1)
        self.server_admin_frame.grid_rowconfigure(40, weight=1)
        self.server_admin_frame_button_1 = customtkinter.CTkButton(self.server_admin_frame, text="SERVER ADMIN", command=self.boton)
        self.server_admin_frame_button_1.grid(row=4, column=1, padx=20, pady=20)
        
        ################
        ### SETTINGS ###
        ################
        #SETTINGS
        self.settings_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        
        
        ################
        ### DEFAULT  ###
        ################
        self.select_frame_by_name("")

###==========================================================================================================================###
#================================================= NAV FUNCTIONS ==============================================================#
###==========================================================================================================================###

    def boton(self):
        print(self.server.ExecCommand("echo CONEXION DESDE EL SERVIDOR"))


    def select_frame_by_name(self, name):
        '''
        Selectes a frame to show by it's name.
        It changes the color of all dropdown menu.
        '''
        # set button color for selected button
        self.home_nav.configure(fg_color=("#3B8ED0","#3B8ED0") if name == "home" else "transparent")
        self.home_monitoring_nav.configure(fg_color=("#3B8ED0","#3B8ED0") if name == "monitoring" else "transparent")
        self.configuration_nav.configure(fg_color=("#3B8ED0","#3B8ED0") if name == "configuration" else "transparent")
        self.configuration_server_config_nav.configure(fg_color=("#3B8ED0","#3B8ED0") if name == "server_config" else "transparent")
        self.server_admin_nav.configure(fg_color=("#3B8ED0","#3B8ED0") if name == "server_admin" else "transparent")
        self.settings_nav.configure(fg_color=("#3B8ED0","#3B8ED0") if name == "settings" else "transparent")
        
        # show selected frame
        if name == "":
            self.login_screen()
            self.patch_notes_frame.grid(column=1, sticky="nsew")
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
            for show_nav_color in self.home_sub_nav_array:
                show_nav_color.configure(fg_color="#1F6AA5")
        else:
            self.home_frame.grid_forget()
        if name == "monitoring":
            self.home_monitoring_frame.grid(row=0, column=1, sticky="nsew")
            self.home_nav.configure(fg_color="#1F6AA5")
        else:
            self.home_monitoring_frame.grid_forget()
        if name == "configuration":
            self.configuration_frame.grid(row=0, column=1, sticky="nsew")
            for show_nav_color in self.configuration_sub_nav_array:
                show_nav_color.configure(fg_color="#1F6AA5")
        else:
            self.configuration_frame.grid_forget()
        if name == "server_config":
            self.configuration_server_config_frame.grid(row=0, column=1, sticky="nsew")
            self.configuration_nav.configure(fg_color="#1F6AA5")
        else:
            self.configuration_server_config_frame.grid_forget()
        if name == "server_admin":
            self.server_admin_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.server_admin_frame.grid_forget()
        if name == "settings":
            self.settings_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.settings_frame.grid_forget()

    def home_button_event(self):
        self.switch_category(navigation_element="home")
        self.select_frame_by_name("home")
        
    def home_monitoring_button_event(self):
        self.select_frame_by_name("monitoring")
        
    def configuration_button_event(self):
        self.switch_category(navigation_element="configuration")
        self.select_frame_by_name("configuration")
        
    def configuration_server_config_button_event(self):
        self.select_frame_by_name("server_config")

    def server_admin_button_event(self):
        self.switch_category(navigation_element="server_admin")
        self.select_frame_by_name("server_admin")

    def settings_button_event(self):
        self.switch_category(navigation_element="settings")
        self.select_frame_by_name("settings")
        
    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def update_nav(self,index_home=1, index_settings=26,index_configuration=2,index_server_admin=3, option="", amount=0):
        match option:
            case 'home':
                index=0
                for sub_nav in self.configuration_sub_nav_array:
                    sub_nav.grid_forget()
                self.configuration_nav.grid(row=index_configuration+amount, column=0, sticky="ew")
                self.server_admin_nav.grid(row=index_server_admin+amount, column=0, sticky="ew")
                for sub_nav_show in self.home_sub_nav_array:
                    sub_nav_show.grid(row=index_home+1+index, column=0, sticky="ew")
                    index+=1
                #for sub_nav in self.server_admin_sub_nav_array:
                #    sub_nav.grid_forget()
                #for sub_nav in self.settings_sub_nav_array:
                #    sub_nav.grid_forget()
            case 'configuration':
                index=0
                for sub_nav in self.home_sub_nav_array:
                    sub_nav.grid_forget()
                self.configuration_nav.grid(row=index_configuration, column=0, sticky="ew")
                self.server_admin_nav.grid(row=index_server_admin+amount, column=0, sticky="ew")
                for sub_nav_show in self.configuration_sub_nav_array:
                    sub_nav_show.grid(row=index_configuration+1+index, column=0, sticky="ew")
                    index+=1
                #for sub_nav in self.settings_sub_nav_array:
                #    sub_nav.grid_forget()
                #for sub_nav in self.server_admin_sub_nav_array:
                #    sub_nav.grid_forget()
            case 'server_admin':
                index=0
                #for sub_nav_show in self.server_admin_sub_nav_array:
                #    sub_nav_show.grid(row=index_home+1+index, column=0, sticky="ew")
                #    index+=1
                self.configuration_nav.grid(row=index_configuration, column=0, sticky="ew")
                self.server_admin_nav.grid(row=index_server_admin, column=0, sticky="ew")
                #for sub_nav in self.configuration_sub_nav_array:
                #    sub_nav.grid_forget()
                #for sub_nav in self.home_sub_nav_array:
                #    sub_nav.grid_forget()
                #for sub_nav in self.settings_sub_nav_array:
                #    sub_nav.grid_forget()
            case 'settings':
                index=0
                #for sub_nav_show in self.settings_sub_nav_array:
                #    sub_nav_show.grid(row=index_home+1+index, column=0, sticky="ew")
                #    index+=1
                self.configuration_nav.grid(row=index_configuration, column=0, sticky="ew")
                self.server_admin_nav.grid(row=index_server_admin, column=0, sticky="ew")
                for sub_nav in self.configuration_sub_nav_array:
                    sub_nav.grid_forget()
                #for sub_nav in self.server_admin_sub_nav_array:
                #    sub_nav.grid_forget()
                for sub_nav in self.home_sub_nav_array:
                    sub_nav.grid_forget()                
            case _:
                print('ERROR')
        
    
    def switch_category(self, navigation_element: str):
        match navigation_element:
            case 'home':
                        self.update_nav(option='home', amount=len(self.home_sub_nav_array))
            case 'configuration':
                        self.update_nav(option="configuration", amount=len(self.configuration_sub_nav_array))
            case 'server_admin':
                        self.update_nav(option='server_admin', amount=len(self.server_admin_sub_nav_array))
            case 'settings':        
                        self.update_nav(option='settings', amount=len(self.settings_sub_nav_array))


###==========================================================================================================================###
#=================================================== FUNCTIONS ================================================================#
###==========================================================================================================================###
        # Event On Clossing
    def on_closing(self, text):
        if tkinter.messagebox.askokcancel("Exit", text):
            self.destroy()

###==========================================================================================================================###
#=================================================== POP UP WINDOWS ===========================================================#
###==========================================================================================================================###

    ################
    ###  LOGIN   ###
    ################
    def login_screen(self):
        '''
        Auth screen to log into the SSH host
        '''

        # Unmap all views but Login view
        self.navigation_frame.grid_forget()
        
        
        ConfigParams=[]
        for key in self.sshConfig.keys():
            ConfigParams.append([key, self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key=key)])
        window = Custom_Toplevel(parent=self)

        window.resizable(False, False)
        w = 500
        h = 500
        x = (self.ws/2) - (w/4)
        y = (self.hs/2) - (h/4)
        window.geometry('%dx%d+%d+%d' % (w, h, x, y))
        window.title("SSH Tunneling Login")
        window.grab_set()
        window.grid_columnconfigure(0, weight=1)
        window.grid_rowconfigure(0,weight=1)
        
        # FUNCTIONS
        def searchFile():
                file = filedialog.askopenfilename(title="Search for RSA keys", 
                                                filetypes=[("Private Keys [.pem, .der, .ppk, .cer, .spc, .p7a, .p7b, .p7c, .pfx]", "*rsa* *host* *key* .key .pem .der .ppk .cer .spc .p7a .p7b .p7c .pfx"), 
                                                            ("All Extensions","*.*")], 
                                                initialdir=str(os.environ['USERPROFILE']+"/.ssh"))
                if file != "":
                    window_login_keypath_entry.delete(0, 100)
                    window_login_keypath_entry.insert(0, file)
                return file
            
        def onSubmit(*args, **kwargs):

            for config_param in ConfigParams:
                if config_param[0] == "hostname":
                    self.fileSystem.editConfig(file=self.fileSystem.sshConfigurationDestination, old=config_param[0], new=window_login_hostname_entry.get())
                if config_param[0] == "port":
                    self.fileSystem.editConfig(file=self.fileSystem.sshConfigurationDestination, old=config_param[0], new=window_login_port_entry.get())
                if config_param[0] == "username":
                    self.fileSystem.editConfig(file=self.fileSystem.sshConfigurationDestination, old=config_param[0], new=window_login_username_entry.get())
                if config_param[0] == "password" and window_login_password_checkbox.get() == 1:
                    self.fileSystem.editConfig(file=self.fileSystem.sshConfigurationDestination, old=config_param[0], new=window_login_password_entry.get())
                elif config_param[0] == "password" and window_login_password_checkbox.get() == 0:
                    self.fileSystem.editConfig(file=self.fileSystem.sshConfigurationDestination, old=config_param[0], new="")
                if config_param[0] == "private_key":
                    self.fileSystem.editConfig(file=self.fileSystem.sshConfigurationDestination, old=config_param[0], new=window_login_keypath_entry.get())
            self.server = client.Client(hostname=window_login_hostname_entry.get(),
                                   port=window_login_port_entry.get(),
                                   username=window_login_username_entry.get(), 
                                   password=window_login_password_entry.get(), 
                                   key_filename=window_login_keypath_entry.get())
            try:
                self.server.Connect()
                window.destroy()
                #Map the view again
                self.navigation_frame.grid(row=0, column=0, sticky="nsew")
                self.navigation_frame.grid_rowconfigure(25, weight=1)
                self.deiconify()
            except Exception as e:
                fail_login_label.configure(text=str(e).capitalize())
                fail_login_label.grid(row=1, column=0, padx=15, pady=(15,15))


        window.bind('<Return>', onSubmit)
        window.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(text="Would you like to quit the login?"))

        window_login_frame = customtkinter.CTkFrame(window, corner_radius=0, width=(w-50), height=(h-50))
        window_login_frame.grid(row=0, column=0)
        window_login_label = customtkinter.CTkLabel(window_login_frame, bg_color="transparent", text="Login", font=customtkinter.CTkFont(size=20, weight="bold"))
        window_login_label.grid(row=0, column=0, padx=15, pady=(15,15))
        fail_login_label = customtkinter.CTkLabel(window_login_frame, bg_color="transparent", font=customtkinter.CTkFont(size=12, weight="bold"), text_color='red')
        window_login_hostname_entry = customtkinter.CTkEntry(window_login_frame, width=250, placeholder_text="Hostname/IP")
        window_login_hostname_entry.grid(row=2, column=0, padx=30, pady=5, sticky="nw")
        if self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key="hostname") != "":
            window_login_hostname_entry.insert(0, self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key="hostname"))
        window_login_port_entry = customtkinter.CTkEntry(window_login_frame, width=250, placeholder_text="Port (Default:22)")
        window_login_port_entry.grid(row=3, column=0, padx=30, pady=5, sticky="nw")
        if self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key="port") != "":
            window_login_port_entry.insert(0, self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key="port"))
        window_login_username_entry = customtkinter.CTkEntry(window_login_frame, width=250, placeholder_text="Username")
        window_login_username_entry.grid(row=4, column=0, padx=30, pady=5, sticky="nw")
        if self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key="username") != "":
            window_login_username_entry.insert(0, self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key="username"))        
        window_login_password_entry = customtkinter.CTkEntry(window_login_frame, width=250, font=customtkinter.CTkFont(size=10), show="⛏", placeholder_text="Password")
        window_login_password_entry.grid(row=5, column=0, padx=30, pady=5, sticky="nw")
        window_login_password_checkbox = customtkinter.CTkCheckBox(window_login_frame, text="Remember?")
        window_login_password_checkbox.grid(row=5, column=1, sticky="w", padx=(0,30), ipadx=0)
        window_login_keypath_entry = customtkinter.CTkEntry(window_login_frame, width=250, placeholder_text="Path to the RSA key...")
        window_login_keypath_entry.grid(row=6, column=0, padx=(30,0), pady=5, sticky="nw")
        if self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key="private_key") != "":
            window_login_keypath_entry.insert(0, self.fileSystem.getConfig(file=self.fileSystem.sshConfigurationDestination, key="private_key"))
        window_login_keypath_button = customtkinter.CTkButton(window_login_frame, text="Search...", command=searchFile, width=50)
        window_login_keypath_button.grid(row=6, column=1,ipadx=0, padx=(5,20), pady=0, sticky="w")
        window_login_button = customtkinter.CTkButton(window_login_frame, text="Login", command=onSubmit, width=200)
        window_login_button.grid(row=7, column=0, padx=30, pady=(15, 15), sticky="nsew")
        #window.make_draggable(window)
        #window.make_no_draggable(window_login_frame)

   
        
        
        ################
        ###  TESTS   ###
        ################