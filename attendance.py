from tkinter import*
from tkinter import ttk   # Contains Scrollbar
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]
class Attendance :
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        self.root.wm_iconbitmap("images/icon.ico")
        #================Variables=================#
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

        #first image
        img=Image.open(r"images/banner.jpg")  #URL for Image
        img=img.resize((1550,130), Image.Resampling.LANCZOS) 
        self.photoimg=ImageTk.PhotoImage(img)
        
        f_lbl=Label(self.root, image=self.photoimg)
        f_lbl.place(x=0,y=0,width=1550,height=130)

        
        
        # background image
        img3=Image.open(r"images/loginbg.jpg")
        img3=img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130, width=1530, height=710)
        
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="indigo")
        title_lbl.place (x=0,y=0, width=1530,height=45) 

        back_btn=Button(title_lbl,text="Back",command = root.destroy,width=8,font=("times new roman", 10,"bold"),bg="skyblue")
        back_btn.grid(row=0, column=0,pady=5,padx=10)
        
        main_frame=Frame(bg_img,bd=2,bg="#c6f1f7")
        main_frame.place(x=20,y=55,width=1480,height=530)
 
        #left label frame
        LEFT_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="#c6f1f7")
        LEFT_frame.place(x=10,y=10,width=730,height=500)

        #Image
        img_left=Image.open(r"images/detail.jpg")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl2=Label(LEFT_frame,image=self.photoimg_left)
        f_lbl2.place(x=5,y=0,width=720,height=130)

        left_inside_frame=Frame(LEFT_frame,bd=2,relief=RIDGE,bg="#c6f1f7")
        left_inside_frame.place(x=2,y=135,width=720,height=340)

        #Labels and entry
        #attendance Id
        attendanceId_label=Label(left_inside_frame,text="Attendance Id:",font=("times new roman",13,"bold"),bg="skyblue")
        attendanceId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        attendanceID_entry=ttk.Entry(left_inside_frame,textvariable=self.var_atten_id,width=20,font=("times new roman",13,"bold"))
        attendanceID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Roll No
        rollLabel=Label(left_inside_frame,text="Roll: ",font="comicsansns 11 bold",bg="skyblue")
        rollLabel.grid(row=0, column=2, padx=4, pady=8)
        
        atten_roll=ttk.Entry(left_inside_frame,textvariable=self.var_atten_roll,width=22,font="comicsansns 11 bold")
        atten_roll.grid(row=0, column=3, pady=8)

        # Name
        nameLabel=Label(left_inside_frame, text="Name:",font="comicsansns 11 bold",bg="skyblue")
        nameLabel.grid(row=1, column=0)
        
        atten_name=ttk. Entry (left_inside_frame,textvariable=self.var_atten_name,width=22,font="comicsansns 11 bold")
        atten_name.grid(row=1, column=1,pady=8)

        # Department
        depLabel=Label(left_inside_frame, text="Department:",font="comicsansns 11 bold",bg="skyblue")
        depLabel.grid(row=1, column=2)
        atten_dep=ttk.Entry(left_inside_frame,textvariable=self.var_atten_dep,width=22,font="comicsansns 11 bold")
        atten_dep.grid(row=1, column=3, pady=8)

        # time
        timeLabel=Label(left_inside_frame,text="Time:",font="comicsansns 11 bold",bg="skyblue")
        timeLabel.grid(row=2,column=0)
        
        atten_time=ttk.Entry(left_inside_frame,textvariable=self.var_atten_time,width=22,font="comicsansns 11 bold")
        atten_time.grid(row=2, column=1, pady=8)

        # Date
        dateLabel=Label(left_inside_frame, text="Date:",font="comicsansns 11 bold",bg="skyblue")
        dateLabel.grid(row=2, column=2)
        atten_date=ttk.Entry(left_inside_frame,textvariable=self.var_atten_date,width=22,font="comicsansns 11 bold")
        atten_date.grid(row=2, column=3, pady=8)

        #Attendance
        attendanceLabel=Label(left_inside_frame,text="Attendance Status:",font="comicsansns 11 bold",bg="skyblue")
        attendanceLabel.grid(row=3,column=0)
        self.atten_status=ttk.Combobox (left_inside_frame,textvariable=self.var_atten_attendance,width=20,font="comicsansns 11 bold", state="readonly")
        self.atten_status["values"]=("Status", "Present", "Absent")
        self.atten_status.grid(row=3, column=1,pady=8)
        self.atten_status.current(0)

        #btn frame
        btn_frame=Frame(left_inside_frame,bd=2, relief=RIDGE,bg="#c6f1f7")
        btn_frame.place(x=0,y=300, width=715,height=35)

        importcsv_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=17,font=("times new roman", 13,"bold"),bg="skyblue")
        importcsv_btn.grid(row=0, column=0)
        
        export_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=17,font=("times new roman",13,"bold"),bg="skyblue")
        export_btn.grid(row=0, column=1)
        
        update_btn=Button(btn_frame, text="Update", width=17,command=self.update_data,font=("times new roman",13,"bold"), bg="skyblue")
        update_btn.grid(row=0, column=2)
        
        reset_btn=Button (btn_frame, text="Reset",command=self.reset_data,width=17,font=("times new roman", 13,"bold"), bg="skyblue",)
        reset_btn.grid(row=0, column=3)

        #Right Label Frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Attendance Details",font=("times new roman",12,"bold"),bg="#c6f1f7")
        Right_frame.place(x=750,y=10,width=720,height=500)

        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="#c6f1f7")
        table_frame.place(x=5,y=5,width=700,height=455)

        #========Scrollbar and Table=======
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.AttendanceReportTable=ttk.Treeview(table_frame,columns=("id","roll","name","department","time","date","attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id",text="Attendance ID")
        self.AttendanceReportTable.heading("roll",text="Roll")
        self.AttendanceReportTable.heading("name",text="Name")
        self.AttendanceReportTable.heading("department",text="Department")
        self.AttendanceReportTable.heading("time",text="Time")
        self.AttendanceReportTable.heading("date",text="Date")
        self.AttendanceReportTable.heading("attendance",text="Attendance")

        self.AttendanceReportTable["show"]="headings"
        
        self.AttendanceReportTable.column("id",width=100)
        self.AttendanceReportTable.column("name",width=100)
        self.AttendanceReportTable.column("roll",width=100)
        self.AttendanceReportTable.column("department",width=100)
        self.AttendanceReportTable.column("time",width=100)
        self.AttendanceReportTable.column("date",width=100)
        self.AttendanceReportTable.column("attendance",width=100)
        
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data_database()

    #Fetching data from database
    def fetch_data_database(self):
       conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
       my_cursor=conn.cursor()
       my_cursor.execute("Select * from attendance")
       data=my_cursor.fetchall()
       if len(data)!=0:
          self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
          for i in data:
             self.AttendanceReportTable.insert("",END,values=i)
          conn.commit()   
       conn.close()     

    #fetch data from csv
    def fetchData(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
           self.AttendanceReportTable.insert("",END,values=i)    

    #Update Function
    def update_data(self):
      if self.var_atten_id.get()=="" or self.var_atten_attendance.get()=="Status" or self.var_atten_roll.get()=="":
        messagebox.showerror("Error","All Credentials are Required",parent=self.root)
      else:
         try:
            Update=messagebox.askyesno("Update","Do You Want To Update Data",parent=self.root)
            if Update>0:
              conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
              my_cursor=conn.cursor()
              my_cursor.execute("update attendance set Attendance=%s where Id=%s and Time=%s",(
                      self.var_atten_attendance.get(),
                      self.var_atten_id.get(),
                      self.var_atten_time.get()
              ))
            else:
               if not Update:
                  return
            messagebox.showinfo("Success","Students Details Updated SuccessFully",parent=self.root)        
            conn.commit()
            self.fetch_data_database()
            conn.close()   
         except Exception as es: 
            messagebox.showerror("Error",f"Due To Update:{str(es)}",parent=self.root)        
        
    #import csv
    def importCsv(self):
        global mydata
        mydata.clear()
        #import os
        #import csv
        #from tkinter import filedialog                                                
        #*csv extension of CSV
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
        #getcwd()=get current working directory
        with open(fln) as myfile:           #By default it reads
            csvread=csv.reader(myfile,delimiter=",")    #Delimiter is used as separator
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)   

    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","No Data Found for Exporting",parent=self.root)
                return False
            
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*csv"),("All File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="") as myfile:        #Here open function writes
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export","Your Data Exported to "+os.path.basename(fln)+" Successfully",parent=self.root)
        except Exception as e:
            messagebox.showerror("Error",f"Due to :{str(e)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.AttendanceReportTable.focus()
        content=self.AttendanceReportTable.item(cursor_row)
        row=content['values']
        self.var_atten_id.set(row[0])
        self.var_atten_roll.set(row[1])
        self.var_atten_name.set(row[2])
        self.var_atten_dep.set(row[3])
        self.var_atten_time.set(row[4])
        self.var_atten_date.set(row[5])
        self.var_atten_attendance.set(row[6])        

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")     
        
       
if __name__ == "__main__":
    root=Tk()
    obj=Attendance(root)
    root.mainloop()
