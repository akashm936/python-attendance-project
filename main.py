from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x740+0+0")
        self.root.title("face recognization Sysytem")



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()