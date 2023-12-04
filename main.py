from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x740+0+0")
        self.root.title("face recognization Sysytem")

        img=Image.open(r"D:\python face project\images\headimg.jpg")
        img=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()