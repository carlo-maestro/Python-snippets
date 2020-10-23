from tkinter import *

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        Label(self, text="Root Word").grid(row=0, column = 1)
        Label(self, text="Definition").grid(row=0, column = 2)
        Label(self, text="Example").grid(row=0, column = 3)
        #self.i = 2
        for self.i in  range(25):
            Label(self, text=str(1+(self.i))).grid(row=int(1+(self.i)), column = 0)
            self.i = self.i + 1
        for i in range(25):
            setattr(self, 'a'+str(i), Entry(self))
            i = i + 1
        #### FIND A WAY TO GRID ALL ENTRY BOXES HERE ####
root = Tk()
root.title("English")
root.geometry("1000x1000")
app = Application(root)
root.mainloop()