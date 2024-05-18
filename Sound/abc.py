from tkinter import*
from tkinter import ttk   # Contains Scrollbar
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

class Attendance :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("images/icon.ico")

        img=Image.open(r"images/banner.jpg")
        img=img.resize((1550,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=130)

        title_lbl=Label(self.root,text="AI TRAINING DATA SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="indigo")
        title_lbl.place(x=0,y=130,width=1530,height=52)

        back_btn=Button(title_lbl,text="Back", command = root.destroy,width=8,font=("times new roman", 10,"bold"),bg="skyblue")
        back_btn.grid(row=0, column=0,pady=8,padx=10)
        
        #left Image
        img_left=Image.open(r"images/facerecog.jpeg")
        img_left=img_left.resize((1550,600),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl1=Label(self.root,image=self.photoimg_left)
        f_lbl1.place(x=0,y=182,width=1550,height=600)
        
        #Button
        b1_1=Button(f_lbl1,text="Train Data",command="",cursor="hand2",font=("times new roman",23,"bold"),bg="green",fg="white")
        b1_1.place(x=640,y=250,width=250,height=70)

if __name__=="__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()          