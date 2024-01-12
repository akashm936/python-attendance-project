from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk




class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1280x720+0+0")
        self.root.title("face recognization Sysytem")
# this is first img
        img=Image.open(r"D:\python face project\images\headimg.jpg")
        img=img.resize((320,130),Image.ADAPTIVE)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=320,height=130)
# this is second img

        img1=Image.open(r"D:\python face project\images\headimg2.png")
        img1=img1.resize((320,130),Image.ADAPTIVE)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=320,y=0,width=320,height=130)

# this is third img
        img2=Image.open(r"D:\python face project\images\headimg.jpg")
        img2=img2.resize((320,130),Image.ADAPTIVE)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=640,y=0,width=320,height=130)
        
        # bg img 
        img3=Image.open(r"D:\python face project\images\bgimg.png")
        img3=img3.resize((1280,720),Image.ADAPTIVE)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img3=Label(self.root,image=self.photoimg3)
        bg_img3.place(x=0,y=130,width=1280,height=720)

# title
        title_lbl=Label(bg_img3,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkviolet")
        title_lbl.place(x=0,y=0,width=1280,height=45)

        main_frame=Frame(bg_img3,bd=2,bg="white")
        main_frame.place(x=0,y=50,width=1280,height=600)

        #left label frame 
        Left_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_Frame.place(x=10,y=10,width=650,height=480)

        img_left=Image.open(r"D:\python face project\images\headimg.jpg")
        img_left=img_left.resize((630,130),Image.ADAPTIVE)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(Left_Frame,image=self.photoimg_left)
        f_lbl.place(x=5,y=0,width=630,height=130)
         

        #current course
        Current_Course_Frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Current course",font=("times new roman",12,"bold"))
        Current_Course_Frame.place(x=5,y=135,width=630,height=120)

        #Courseartment
        dep_Label=Label(Current_Course_Frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_Label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(Current_Course_Frame,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Department","Computer","IT","Machanical","Civil")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #course
        Course_Label=Label(Current_Course_Frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        Course_Label.grid(row=0,column=2,padx=10)

        Course_combo=ttk.Combobox(Current_Course_Frame,font=("times new roman",12,"bold"),state="read only")
        Course_combo["values"]=("Select FE","SE","TE","B.Tech")
        Course_combo.current(0)
        Course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


          #year
        Year_Label=Label(Current_Course_Frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        Year_Label.grid(row=1,column=0,padx=10)

        Year_combo=ttk.Combobox(Current_Course_Frame,font=("times new roman",12,"bold"),state="read only")
        Year_combo["values"]=("Select 2019","2020","2021","2022","2023","2024")
        Year_combo.current(0)
        Year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

           #year
        Semester_Label=Label(Current_Course_Frame,text="Sem",font=("times new roman",12,"bold"),bg="white")
        Semester_Label.grid(row=1,column=2,padx=10)

        Semester_combo=ttk.Combobox(Current_Course_Frame,font=("times new roman",12,"bold"),state="read only")
        Semester_combo["values"]=("Select Sem-1","Sem-2","Sem-3","Sem-4","Sem-5","Sem-6")
        Semester_combo.current(0)
        Semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


             #Student Information
        Class_Student_Frame=LabelFrame(Left_Frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",12,"bold"))
        Class_Student_Frame.place(x=5,y=260,width=630,height=200)


  #right label frame 
        Right_Frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Details",font=("times new roman",12,"bold"))
        Right_Frame.place(x=670,y=10,width=600,height=480)


        
if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()