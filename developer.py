from tkinter import*
from tkinter import ttk   # Contains Scrollbar
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import webbrowser

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Developer")
        self.root.wm_iconbitmap("images/icon.ico")
    
        title_lbl=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="white",fg="indigo")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        back_btn=Button(title_lbl,text="Back", command = root.destroy,width=8,font=("times new roman", 10,"bold"),bg="skyblue")
        back_btn.grid(row=0, column=0,pady=8,padx=10)
        
        img_top=Image.open(r"images/loginbg.jpg")
        img_top=img_top.resize((1530,720),Image.Resampling.LANCZOS)
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        f_lbl2=Label(self.root,image=self.photoimg_top)
        f_lbl2.place(x=0,y=55,width=1530,height=720)

        img_left=Image.open(r"images/developerBanner.jpg")
        img_left=img_left.resize((1480,600),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(f_lbl2,image=self.photoimg_left)
        f_lbl.place(x=25,y=35,width=1480,height=600)

           
       

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()        