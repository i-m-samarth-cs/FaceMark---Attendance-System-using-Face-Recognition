from tkinter import*                #tkinter is used to create GUI Applications
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from student import Student
import os
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime

class Face_Recognition_System:
    def __init__(self,root):
        
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("images/icon.ico")
        #First Image
        img=Image.open(r"images\banner.jpg")
        img=img.resize((1550,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=130)

        

        #background Image
        img3=Image.open(r"images/loginbg.jpg")
        img3=img3.resize((1530,710),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="purple")
        title_lbl.place(x=0,y=0,width=1530,height=55)

        # Timer Code
        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        lbl = Label(title_lbl, font= ('times new roman', 14, 'bold'), background='white',foreground='black')
        lbl.place(x=0,y=0, width=110,height=50)
        time()

        #Student Button
        img4=Image.open(r"images/student.jpg")
        img4=img4.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,command=self.student_details,image=self.photoimg4,cursor="hand2",bd=3,bg="black")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,command=self.student_details,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="indigo",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face Button
        img5=Image.open(r"images/attend.jpg")
        img5=img5.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,cursor="hand2",command=self.face_data,bd=3,bg="black")
        b1.place(x=500,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Take Attendance",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="indigo",fg="white")
        b1_1.place(x=500,y=300,width=220,height=40)

        #Attendance Button
        img6=Image.open(r"images/attendancelogo.jpg")
        img6=img6.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.photoimg6,cursor="hand2",command=self.attendence_data,bd=3,bg="black")
        b1.place(x=800,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Attendance",cursor="hand2",command=self.attendence_data,font=("times new roman",15,"bold"),bg="indigo",fg="white")
        b1_1.place(x=800,y=300,width=220,height=40)
        
        #Help Button
        img7=Image.open(r"images/helpdesk.png")
        img7=img7.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data,bd=3,bg="black")
        b1.place(x=1100,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="indigo",fg="white")
        b1_1.place(x=1100,y=300,width=220,height=40)

        #Train face Button
        img8=Image.open(r"images/traindata.jpg")
        img8=img8.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.photoimg8,command=self.train_data,cursor="hand2",bd=3,bg="black")
        b1.place(x=200,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="indigo",fg="white")
        b1_1.place(x=200,y=580,width=220,height=40)

        #Photos Button
        img9=Image.open(r"images/photo.jpg")
        img9=img9.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.open_img,bd=3,bg="black")
        b1.place(x=500,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="indigo",fg="white")
        b1_1.place(x=500,y=580,width=220,height=40)

        #Developer Button
        img10=Image.open(r"images/developer.jpg")
        img10=img10.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data,bd=3,bg="black")
        b1.place(x=800,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="indigo",fg="white")
        b1_1.place(x=800,y=580,width=220,height=40)
        
        #Exit Button
        img11=Image.open(r"images/exit.jpg")
        img11=img11.resize((220,220),Image.Resampling.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit,bd=3,bg="black")
        b1.place(x=1100,y=380,width=220,height=220)

        b1_1=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="indigo",fg="white")
        b1_1.place(x=1100,y=580,width=220,height=40)

    def open_img(self):
        os.startfile("data")            #name of the folder


    #Function Buttons
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window) 

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendence_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)   

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window) 

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)  

    def iExit(self):
        self.iExit=messagebox.askyesno("Face Recognition","Are you Sure?",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return               
       



if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()