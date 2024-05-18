from tkinter import*                #tkinter is used to create GUI Applications
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2              #importing open cv library it is open source computer vision library it contiains more than 1500 Algorithm
import os
import numpy as np

class Train:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Train Data")
        self.root.wm_iconbitmap("images/icon.ico")
        
        img=Image.open(r"images/banner.jpg")
        img=img.resize((1550,130),Image.Resampling.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=130)

        title_lbl=Label(self.root,text="AI TRAINING DATA SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="indigo")
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
        b1_1=Button(f_lbl1,text="Train Data",command=self.train_classifier,cursor="hand2",font=("times new roman",23,"bold"),bg="green",fg="white")
        b1_1.place(x=640,y=250,width=250,height=70)

        
        
        #LBPH Local Binary patern histogram Alogrithm is use for face Recognition and  invented in 1996
        #Local Binary Pattern (LBP) is a simple yet very efficient texture operator which labels the pixels 
        #   of an image by thresholding the neighborhood of each pixel and considers the result as a binary number.
        #We use LBPH because it is esay and it can represent local feature in imageand it is possible to get great result
        # and it best for gray scale image and it is of opencv provided by opencv

    def train_classifier(self):
        data_dir=("data")           #Folder name
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]        #list comphrensive    
        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')          # L for Gray Scale
            imageNp=np.array(img,'uint8')               #uint8 is data type
            id=int(os.path.split(image)[1].split('.')[1])

            #images/data\user.1.1.jpg
            #-------index 0---////index1///

            faces.append(imageNp)
            ids.append(id)
            cv2.moveWindow("Training",500,220)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13              #13 for enter to close

        ids=np.array(ids)           #we are using numpy for converting to array which increase performance by 88%

        #Train the classifier and save
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("REsult","AI Training Data Sets Completed!!",parent=self.root)





if __name__=="__main__":
    root=Tk()
    obj=Train(root)
    root.mainloop()          