from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk



class Face_Recognization_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x710+0+0")
        self.root.title("face recognization Sysytem")
# this is first img
        img=Image.open(r"D:\python face project\images\headimg.jpg")
        img=img.resize((500,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)
# this is second img

        img1=Image.open(r"D:\python face project\images\headimg2.png")
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
        
# bg img 
        img3=Image.open(r"D:\python face project\images\bgimg.jpg")
        img3=img3.resize((1500,710),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img3=Label(self.root,image=self.photoimg3)
        bg_img3.place(x=0,y=130,width=1500,height=710)

# title
        title_lbl=Label(bg_img3,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="darkviolet")
        title_lbl.place(x=0,y=0,width=1530,height=45)

# button 1

        img4=Image.open(r"D:\python face project\images\student.png")
        img4=img4.resize((200,200),Image.ADAPTIVE)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img3,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1=Button(bg_img3,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=200,y=300,width=200,height=40)

# button 2

        img5=Image.open(r"D:\python face project\images\faced.png")
        img5=img5.resize((200,200),Image.ADAPTIVE)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img3,image=self.photoimg5,cursor="hand2")
        b1.place(x=500,y=100,width=200,height=200)

        b1=Button(bg_img3,text="Face detect",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=500,y=300,width=200,height=40)

# button 3

        img6=Image.open(r"D:\python face project\images\attend.png")
        img6=img6.resize((200,200),Image.ADAPTIVE)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img3,image=self.photoimg6,cursor="hand2")
        b1.place(x=800,y=100,width=200,height=200)

        b1=Button(bg_img3,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=800,y=300,width=200,height=40)


# button 4

        img7=Image.open(r"D:\python face project\images\help.jpg")
        img7=img7.resize((200,200),Image.ADAPTIVE)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img3,image=self.photoimg7,cursor="hand2")
        b1.place(x=1100,y=100,width=200,height=200)

        b1=Button(bg_img3,text="Help",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=1100,y=300,width=200,height=40)
# button 5

        img8=Image.open(r"D:\python face project\images\train.png")
        img8=img8.resize((200,200),Image.ADAPTIVE)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img3,image=self.photoimg8,cursor="hand2")
        b1.place(x=200,y=400,width=200,height=200)

        b1=Button(bg_img3,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=200,y=400,width=200,height=40)
# button 6 
    

        img9=Image.open(r"D:\python face project\images\photos.png")
        img9=img9.resize((200,200),Image.ADAPTIVE)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img3,image=self.photoimg9,cursor="hand2")
        b1.place(x=500,y=400,width=200,height=200)

        b1=Button(bg_img3,text="photos",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=500,y=400,width=200,height=40)
# button 7

        img10=Image.open(r"D:\python face project\images\developer.jpg")
        img10=img10.resize((200,200),Image.ADAPTIVE)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img3,image=self.photoimg10,cursor="hand2")
        b1.place(x=800,y=400,width=200,height=200)

        b1=Button(bg_img3,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=800,y=400,width=200,height=40)
# button 8

        img11=Image.open(r"D:\python face project\images\exit.png")
        img11=img11.resize((200,200),Image.ADAPTIVE)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img3,image=self.photoimg11,cursor="hand2")
        b1.place(x=1100,y=400,width=200,height=200)

        b1=Button(bg_img3,text="exit",cursor="hand2",font=("times new roman",15,"bold"),bg="blue",fg="white")
        b1.place(x=1100,y=400,width=200,height=40)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognization_System(root)
    root.mainloop()