from tkinter import*                #tkinter is used to create GUI Applications
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2              #importing open cv library it is open source computer vision library it contiains more than 1500 Algorithm
import os
import numpy as np
from time import strftime
from datetime import datetime
from playsound import playsound
import winsound
from twilio.rest import Client
import pandas as pd
import smtplib



class Face_Recognition:
    count=0
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Face Recognition")
        self.root.wm_iconbitmap("images/icon.ico")

        img=Image.open(r"images/banner.jpg")
        img=img.resize((1550,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=130)

        title_lbl=Label(self.root,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="indigo")
        title_lbl.place(x=0,y=130,width=1530,height=52)

        back_btn=Button(title_lbl,text="Back", command = root.destroy,width=8,font=("times new roman", 10,"bold"),bg="skyblue")
        back_btn.grid(row=0, column=0,pady=8,padx=10)
        
        #left Image
        img_left=Image.open(r"images/facerecog.jpeg")
        img_left=img_left.resize((1550,600),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl1=Label(self.root,image=self.photoimg_left)
        f_lbl1.place(x=0,y=182,width=1550,height=600)

       

        #Button
        b1_1=Button(f_lbl1,text="Take Attendance",command=self.face_recog,cursor="hand2",font=("times new roman",23,"bold"),bg="green",fg="white")
        b1_1.place(x=640,y=250,width=250,height=70)

    #Atendance
    def mark_attendance(self,i,r,n,d,name):  
                #i,r,n,d are arguments of cv2.putText(img,f"ID:{i},{r},{n},{d}
        
        with open(name,"r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                # used for non repetative attendance
                # from Data and time use => from time import strftime
                # from datetime import datetime
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")   # used for date month and Year     
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

                #Attendance data store in database
                try:
                    conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into attendance values(%s,%s,%s,%s,%s,%s,%s)",(
                        i,
                        r,
                        n,
                        d,
                        dtString,
                        d1,
                        "Present"

                    ))
                    conn.commit()
                    conn.close()
                except Exception as es:
                        messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
                self.make_sound()        


    def make_sound(self):
       # playsound("C:/Capstone/Sound/sample.mp3")
       
        freq=2000
        dura=300
        
        self.count=self.count+1
        winsound.Beep(freq,dura)


    
    #Face Recognition
    def face_recog(self):
        
        def draw_boundary(img,classifier,scaleFactor,minNeighbours,color,text,clf,name):     #inner Function
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbours)

            coord=[]

            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
                my_cursor=conn.cursor()
                

                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

              
                i=str(id)
                i="+".join(i)


                if confidence>77:           #Percentage of Matching
                    cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d,name)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]
            return coord        

        def recognize(img,clf,faceCascade,name):

            coord=draw_boundary(img,faceCascade,1.1,10,(255,255,255),"Face",clf,name)
            return img
        
        now=datetime.now()
        d1=now.strftime("%d_%m_%Y")   # used for date month and Year     
        dtString=now.strftime("%H_%M_%S")
        name="C:/Capstone/Attendance_csv"+"/attendance."+d1+"."+dtString+".csv"
        csvfile=name
        f = open(name, "w+")

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")          #train data is read

        video_cap=cv2.VideoCapture(0)
        
        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade,name)
            cv2.moveWindow("Welcome to Face Recognition Attendance System",500,220)
            cv2.imshow("Welcome to Face Recognition",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        self.sendsms()
        cv2.destroyAllWindows()

    def sendsms(self):
        try:
            conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
            my_cursor=conn.cursor()
            my_cursor.execute("SELECT COUNT(Student_id) FROM student")
            cnt=my_cursor.fetchall()
            
            conn.commit()
            conn.close()
        except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

        
        percentage=(int(self.count)/int(cnt[0][0]))*100
        absent=int(cnt[0][0])-int(self.count)

        msg="Number of Student Present: "+str(self.count)+"   Percentage of Student Present : "+str(percentage)+"%"+"      Number of Student Absent"+str(absent)
        client=Client("AC883b6031ffe02e196c6c4450abd79f1c","969b407afe2d379384f320d3672bf668")
        client.messages.create(to =["+918767950663"],from_= "+15177818442",body=msg)
        print(percentage)
        percentage=0
        self.count=0







if __name__=="__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()