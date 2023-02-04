'''
CUSTOM BORDERLESS TOPLEVEL
'''
import customtkinter, tkinter, tkinter.messagebox

class Custom_Toplevel(customtkinter.CTkToplevel):
    def __init__(self, parent):
        super().__init__()
        self.parent=parent
        self.lastClickX=0
        self.lastClickY=0
        self.overrideredirect(False)
        #self.attributes('-topmost', True)

        
        
    def SaveLastClickPos(self, event):
        global lastClickX, lastClickY
        lastClickX = event.x
        lastClickY = event.y
        return lastClickX, lastClickY


    def Dragging(self, event):
        cx, cy =event.x-lastClickX+self.winfo_x(), event.y-lastClickY+self.winfo_y()
        #print("cx: ",cx,"cy: ", cy, "event.x: ", abs(event.x), "event.y: ", abs(event.y), "LCX:", lastClickX, "LCY: ", lastClickY)
        self.geometry("+%s+%s" % (cx , cy))
    
    def make_draggable(self, widget):
        widget.bind('<Button-1>', self.SaveLastClickPos)
        widget.bind('<B1-Motion>', self.Dragging)
    def make_no_draggable(self, widget):
        widget.unbind('<Button-1>')
        widget.unbind('<B1-Motion>')
            
 # Events handler
        def on_closing():
            asking=tkinter.messagebox.askyesno("Exit", "You need to log in before continue, are you sure you want to exit?")
            self.withdraw()
            if asking:
                self.destroy()
                self.parent.destroy()
            else:
                self.deiconify()

        # Events
        self.protocol("WM_DELETE_WINDOW", on_closing)