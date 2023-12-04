from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1400x740+0+0")
        self.root.title("face recognization Sysytem")
# this is first img
        img=Image.open(r"D:\python face project\images\headimg.jpg")
        img=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
# this is second img

        img1=Image.open(r"D:\python face project\images\headimg.jpg")
        img1=img1.resize((500,130),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

# this is third img
        img2=Image.open(r"D:\python face project\images\headimg.jpg")
        img2=img2.resize((500,130),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)
        

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()