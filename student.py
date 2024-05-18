from tkinter import*                #tkinter is used to create GUI Applications
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2              #importing open cv library it is open source computer vision library it contiains more than 1500 Algorithm
from tkcalendar import DateEntry
import re

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1550x800+0+0")
        self.root.title("Student")
        self.root.wm_iconbitmap("images/icon.ico") 
        #Variable
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()
        self.var_course=StringVar()

        #search variable
        self.var_searchBy=StringVar()
        self.var_data=StringVar()

        #First Image
        img=Image.open(r"images/banner.jpg")
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

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="indigo")
        title_lbl.place(x=0,y=0,width=1530,height=52)

        back_btn=Button(title_lbl,text="Back", command = root.destroy,width=8,font=("times new roman", 10,"bold"),bg="skyblue")
        back_btn.grid(row=0, column=0,pady=5,padx=10)

        main_frame=Frame(bg_img,bd=2,bg="#c6f1f7")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        LEFT_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"),bg="#c6f1f7")
        LEFT_frame.place(x=10,y=10,width=730,height=580)

        #Image
        img_left=Image.open(r"images/registeration.png")
        img_left=img_left.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl2=Label(LEFT_frame,image=self.photoimg_left)
        f_lbl2.place(x=5,y=0,width=720,height=130)

        #current course
        current_course_frame=LabelFrame(LEFT_frame,bd=2,relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"),bg="#c6f1f7")
        current_course_frame.place(x=5,y=135,width=715,height=110)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",13,"bold"),bg="skyblue")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)      #grid for Grid Layout

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",13,"bold"),width=20,state="readonly")
        dep_combo["values"]=("Select Deparment","Computer","IT","Civil","Mechnaical","Electrical")  #tuple
        dep_combo.current(0)            
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)  #sticky-west

        #course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",13,"bold"),bg="skyblue")
        course_label.grid(row=0,column=2,padx=10,sticky=W)      #grid for Grid Layout

        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("times new roman",13,"bold"),width=20,state="readonly")
        course_combo["values"]=("Select Course","Diploma","B-Tech","BSC-Comp","BCA-Comp")  #tuple
        course_combo.current(0)            
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #Year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="skyblue")
        year_label.grid(row=1,column=0,padx=10,sticky=W)      #grid for Grid Layout

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),width=20,state="readonly")
        year_combo["values"]=("Select Year","First","Second","Third","Fourth")  #tuple
        year_combo.current(0)            
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",13,"bold"),bg="skyblue")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)      #grid for Grid Layout

        semester_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("times new roman",13,"bold"),width=20,state="readonly")
        semester_combo["values"]=("Select Semester","First","Second","Third","Fourth","Fifth","Sixth","Seventh","Eight")  #tuple
        semester_combo.current(0)            
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #Class Student information
        class_Student_frame=LabelFrame(LEFT_frame,bd=2,relief=RIDGE,text="Class Student Information",font=("times new roman",12,"bold"),bg="#c6f1f7")
        class_Student_frame.place(x=5,y=250,width=715,height=300)

        #Student Id
        studentId_label=Label(class_Student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="skyblue")
        studentId_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_Student_frame,textvariable=self.var_std_id,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #Student Name
        studentName_label=Label(class_Student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="skyblue")
        studentName_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentName_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_std_name,font=("times new roman",13,"bold"))
        studentName_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #Class Division
        class_div_label=Label(class_Student_frame,text="Class Division:",font=("times new roman",13,"bold"),bg="skyblue")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),width=18,state="readonly")
        div_combo["values"]=("Select Division","A","B","C","D","E")  #tuple
        div_combo.current(0)            
        div_combo.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #Roll No
        roll_no_label=Label(class_Student_frame,text="Roll No:",font=("times new roman",13,"bold"),bg="skyblue")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_roll,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #Gender
        gender_label=Label(class_Student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="skyblue")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_Student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),width=18,state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Other")  #tuple
        gender_combo.current(0)            
        gender_combo.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_Student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="skyblue")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=DateEntry(class_Student_frame,selectmode='day',textvariable=self.var_dob,font=("times new roman",10,"bold"),width=23,heigth=15)
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #Email
        email_label=Label(class_Student_frame,text="Email:",font=("times new roman",13,"bold"),bg="skyblue")
        email_label.grid(row=3,column=0,padx=10,pady=3,sticky=W)

        email_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_email,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #Phone Number
        phone_label=Label(class_Student_frame,text="Phone No:",font=("times new roman",13,"bold"),bg="skyblue")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_phone,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        address_label=Label(class_Student_frame,text="Address:",font=("times new roman",13,"bold"),bg="skyblue")
        address_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        address_entry=ttk.Entry(class_Student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        address_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #Teacher
        teacher_label=Label(class_Student_frame,text="Teacher Name:",font=("times new roman",13,"bold"),bg="skyblue")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_Student_frame,width=20,textvariable=self.var_teacher,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #Radio Buttons
        self.var_radio1=StringVar()
        radiobtn1=Radiobutton(class_Student_frame,font=("times new roman",13,"bold"),bg="skyblue",activebackground="white",variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=6,column=0)

        #Radio Buttons
        radiobtn2=Radiobutton(class_Student_frame,font=("times new roman",13,"bold"),bg="skyblue",activebackground="white",variable=self.var_radio1,text="NO Photo Sample",value="No")
        radiobtn2.grid(row=6,column=1)

        #buttons frame
        btn_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="#c6f1f7")
        btn_frame.place(x=0,y=200,width=710,height=35)

        save_btn=Button(btn_frame,text="Save",command=self.add_data,font=("times new roman",13,"bold"),bg="skyblue",width=17)
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,font=("times new roman",13,"bold"),bg="skyblue",width=17)
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,font=("times new roman",13,"bold"),bg="skyblue",width=17)
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,font=("times new roman",13,"bold"),bg="skyblue",width=17)
        reset_btn.grid(row=0,column=3)

        btn1_frame=Frame(class_Student_frame,bd=2,relief=RIDGE,bg="white")
        btn1_frame.place(x=0,y=235,width=710,height=35)

        take_photo_btn=Button(btn1_frame,command=self.generate_dataset,text="Take Photo Sample",font=("times new roman",14,"bold"),bg="skyblue",width=70)
        take_photo_btn.grid(row=0,column=0)

        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,text="Get Student Details",font=("times new roman",12,"bold"),bg="#c6f1f7")
        Right_frame.place(x=750,y=10,width=720,height=580)

        img_right=Image.open(r"images/info.png")
        img_right=img_right.resize((720,130),Image.Resampling.LANCZOS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl2=Label(Right_frame,image=self.photoimg_right)
        f_lbl2.place(x=5,y=0,width=710,height=130)

        #SEarch System
        Search_frame=LabelFrame(Right_frame,bd=2,relief=RIDGE,text="Search System",font=("times new roman",12,"bold"),bg="#c6f1f7")
        Search_frame.place(x=5,y=150,width=710,height=70)

        search_label=Label(Search_frame,text="Search By",font=("times new roman",13,"bold"),bg="skyblue")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(Search_frame,font=("times new roman",13,"bold"),textvariable=self.var_searchBy,width=15,state="readonly")
        search_combo["values"]=("Select","Roll_NO","Phone_No")  #tuple
        search_combo.current(0)            
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(Search_frame,width=20,textvariable=self.var_data,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        serach_btn=Button(Search_frame,text="Search",font=("times new roman",12,"bold"),command=self.serach_data,bg="skyblue",width=10)
        serach_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(Search_frame,text="Show All",font=("times new roman",12,"bold"),command=self.fetch_data,bg="skyblue",width=10)
        showAll_btn.grid(row=0,column=4,padx=4)

        #TAble Frame
        table_frame=Frame(Right_frame,bd=2,relief=RIDGE,bg="#c6f1f7")
        table_frame.place(x=5,y=225,width=710,height=330)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("dep","course","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semester")
        self.student_table.heading("id",text="Student Id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll No")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="Photo Sample Status")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)          #Event Handing Action Performed Event
        self.fetch_data()

    
    #Function Declaration
    def add_data(self):
      if self.var_dep.get()=="Select Dapartment" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester":
         messagebox.showerror("Error","Please Enter Current Course Information...!!!",parent=self.root)
      elif self.var_std_id.get()=="" or (bool(re.match('^[0-9]+$',self.var_std_id.get())))==FALSE or self.var_std_name.get()=="" or (bool(re.match("^[a-zA-Z\sa-zA-Z]+$", self.var_std_name.get())))==FALSE:
         messagebox.showerror("Error","Please Enter the Correct Id And Full Name...!!!",parent=self.root)    
      elif self.var_div.get()=="Select Division" or self.var_gender.get()=="Select Gender" :
         messagebox.showerror("Error","Please Select the Division and Gender...!!!",parent=self.root) 
      elif self.var_roll.get()=="" or (bool(re.match('^[0-9]+$',self.var_roll.get())))==FALSE :
         messagebox.showerror("Error","Please Enter the Roll Number...!!!",parent=self.root) 
      elif self.var_email.get()=="" or  (bool(re.match("^\S+@\S+\.\S+$",self.var_email.get())))==FALSE:
         messagebox.showerror("Error","Please Enter the Correct Email Address...!!!",parent=self.root)  
      elif self.var_phone.get()=="" or  (bool(re.match("^[0-9]{10}",self.var_phone.get())))==FALSE : 
         messagebox.showerror("Error","Please Enter the 10 Digit Mobile Number ...!!!",parent=self.root)
      elif self.var_address.get()=="" or  self.var_teacher.get()=="" :    
         messagebox.showerror("Error","Please Enter the Address and Teacher Name...!!!",parent=self.root)    
      elif self.var_radio1.get()=="":
         messagebox.showerror("Error","Please Check the Radio Button...!!!",parent=self.root) 
      else:
         try:
          conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
          my_cursor=conn.cursor()
          my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
              self.var_dep.get(),
              self.var_course.get(),
              self.var_year.get(),
              self.var_semester.get(),
              self.var_std_id.get(),
              self.var_std_name.get(),
              self.var_div.get(),
              self.var_roll.get(),
              self.var_gender.get(),
              self.var_dob.get(),
              self.var_email.get(),
              self.var_phone.get(),
              self.var_address.get(),
              self.var_teacher.get(),
              self.var_radio1.get()

          ))
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success","Students Details Inserted Successfully..",parent=self.root)
         
         except Exception as es:
            messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

    #Fetch data
    def fetch_data(self):
       conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
       my_cursor=conn.cursor()
       my_cursor.execute("Select * from student")
       data=my_cursor.fetchall()
       if len(data)!=0:
          self.student_table.delete(*self.student_table.get_children())
          for i in data:
             self.student_table.insert("",END,values=i)
          conn.commit()   
       conn.close() 

    #get cursor   
    def get_cursor(self,event):
       cursor_focus=self.student_table.focus()
       content=self.student_table.item(cursor_focus)
       data=content["values"]

       self.var_dep.set(data[0])
       self.var_course.set(data[1])
       self.var_year.set(data[2])
       self.var_semester.set(data[3])
       self.var_std_id.set(data[4])
       self.var_std_name.set(data[5])
       self.var_div.set(data[6])
       self.var_roll.set(data[7])
       self.var_gender.set(data[8])
       self.var_dob.set(data[9])
       self.var_email.set(data[10])
       self.var_phone.set(data[11])
       self.var_address.set(data[12])
       self.var_teacher.set(data[13])
       self.var_radio1.set(data[14])

    #Update Function
    def update_data(self):
      if self.var_dep.get()=="Select Dapartment" or self.var_course.get()=="Select Course" or self.var_year.get()=="Select Year" or self.var_semester.get()=="Select Semester":
         messagebox.showerror("Error","Please Enter Current Course Information...!!!",parent=self.root)
      elif self.var_std_id.get()=="" or (bool(re.match('^[0-9]+$',self.var_std_id.get())))==FALSE or self.var_std_name.get()=="" or (bool(re.match("^[a-zA-Z\sa-zA-Z]+$", self.var_std_name.get())))==FALSE:
         messagebox.showerror("Error","Please Enter the Correct Id And Full Name...!!!",parent=self.root)    
      elif self.var_div.get()=="Select Division" or self.var_gender.get()=="Select Gender" :
         messagebox.showerror("Error","Please Select the Division and Gender...!!!",parent=self.root) 
      elif self.var_roll.get()=="" or (bool(re.match('^[0-9]+$',self.var_roll.get())))==FALSE :
         messagebox.showerror("Error","Please Enter the Roll Number...!!!",parent=self.root) 
      elif self.var_email.get()=="" or  (bool(re.match("^\S+@\S+\.\S+$",self.var_email.get())))==FALSE:
         messagebox.showerror("Error","Please Enter the Correct Email Address...!!!",parent=self.root)  
      elif self.var_phone.get()=="" or  (bool(re.match("^[0-9]{10}",self.var_phone.get())))==FALSE : 
         messagebox.showerror("Error","Please Enter the 10 Digit Mobile Number ...!!!",parent=self.root)
      elif self.var_address.get()=="" or  self.var_teacher.get()=="" :    
         messagebox.showerror("Error","Please Enter the Address and Teacher Name...!!!",parent=self.root)    
      elif self.var_radio1.get()=="":
         messagebox.showerror("Error","Please Check the Radio Button...!!!",parent=self.root) 
      else:
         try:
            Update=messagebox.askyesno("Update","Do You Want To Update Data",parent=self.root)
            if Update>0:
              conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
              my_cursor=conn.cursor()
              my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                      self.var_dep.get(),
                      self.var_course.get(),
                      self.var_year.get(),
                      self.var_semester.get(),
                      self.var_std_name.get(),
                      self.var_div.get(),
                      self.var_roll.get(),
                      self.var_gender.get(),
                      self.var_dob.get(),
                      self.var_email.get(),
                      self.var_phone.get(),
                      self.var_address.get(),
                      self.var_teacher.get(),
                      self.var_radio1.get(),
                      self.var_std_id.get()
              ))
            else:
               if not Update:
                  return
            messagebox.showinfo("Success","Students Details Updated SuccessFully",parent=self.root)        
            conn.commit()
            self.fetch_data()
            conn.close()   
         except Exception as es: 
            messagebox.showerror("Error",f"Due To Update:{str(es)}",parent=self.root)   

    #Delete Function
    def delete_data(self):
       if self.var_std_id.get()=="":
          messagebox.showerror("Error","Enter the Student Id",parent=self.root)
       else:
          try:
             delete=messagebox.askyesno("Delele","Do You want Delete this Student",parent=self.root)
             if delete>0:
                conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
                my_cursor=conn.cursor()
                sql="delete from student where Student_id=%s"
                val=(self.var_std_id.get(),)
                my_cursor.execute(sql,val)
             else:
                if not delete:
                   return
                    
             conn.commit()
             self.fetch_data()
             conn.close()   
             messagebox.showinfo("Success","Students Details Deleted SuccessFully",parent=self.root) 
          except Exception as es: 
            messagebox.showerror("Error",f"Due To Delete:{str(es)}",parent=self.root)     

    #reset Function
    def reset_data(self):
       self.var_dep.set("Select Department") 
       self.var_course.set("Select Course")
       self.var_year.set("Select Year")
       self.var_semester.set("Select Semester")
       self.var_std_id.set("")
       self.var_std_name.set("")
       self.var_div.set("Select Division")
       self.var_roll.set("")
       self.var_gender.set("Select Gender")
       self.var_dob.set("")
       self.var_email.set("")
       self.var_phone.set("")
       self.var_address.set("")
       self.var_teacher.set("")
       self.var_radio1.set("")   
       
    #Generate data set or take photo samples
    def generate_dataset(self):
       if self.var_dep.get()=="Select Dapartment" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
        messagebox.showerror("Error","All Credentials are Required",parent=self.root)
       else:
         try:
            conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from student")
            myresult=my_cursor.fetchall()
            id=0        #to count number of images
            for x in myresult:
               id+=1
            my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                      self.var_dep.get(),
                      self.var_course.get(),
                      self.var_year.get(),
                      self.var_semester.get(),
                      self.var_std_name.get(),
                      self.var_div.get(),
                      self.var_roll.get(),
                      self.var_gender.get(),
                      self.var_dob.get(),
                      self.var_email.get(),
                      self.var_phone.get(),
                      self.var_address.get(),
                      self.var_teacher.get(),
                      self.var_radio1.get(),
                      self.var_std_id.get()==id+1
              ))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            conn.close()

            #Haar Cascades Algorithm is machine learning approach to identiy the object from data using video this is use for face detection
            
            #load predefined data on face frontals from opencv
            face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

            def face_cropped(img):
               gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)          # to Convert the RGB color image to Gray Image
               faces=face_classifier.detectMultiScale(gray,1.3,5)
               #Scaling Factor=1.3
               #minimum Neighbour=5

               for(x,y,w,h) in faces:
                  face_cropped=img[y:y+h,x:x+w]
                  return face_cropped
            #url="https://192.168.1.2/video"   
            #cap=cv2.VideoCapture(url)
            cap=cv2.VideoCapture(0, cv2.CAP_DSHOW)          #to open the camera 0=webcam of Laptop,1=for other camera,we can also pass url t open any camera
            img_id=0   
            while True:
               ret,my_frame=cap.read()
               if face_cropped(my_frame) is not None:
                  img_id+=1
                  face=cv2.resize(face_cropped(my_frame),(450,450))   
                  face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY) 
                  file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                  cv2.imwrite(file_name_path,face)
                  cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)  #Scale=2,rgb color=(0,255,0),thickness=2
                  cv2.imshow("Cropped Face",face)      #To Show Camera

               if cv2.waitKey(1)==13 or int(img_id)==100:     #waitKey(1)==13 is for enter to close
                  break
            cap.release()
            cv2.destroyAllWindows()
            messagebox.showinfo("Result","Generating data sets Completed SuccessFully!!!")

         except Exception as es: 
            messagebox.showerror("Error",f"Due in opencv function:{str(es)}",parent=self.root)  

    def serach_data(self):
       if self.var_searchBy.get()=="Select" or self.var_data.get()=="":
        messagebox.showerror("Error","All Credentials are Required",parent=self.root)
       else:
         try:
            conn= mysql.connector.connect(host="localhost",username="root",password="Samarth123@",database="capstone")
            my_cursor=conn.cursor()
            if self.var_searchBy.get()=="Roll_NO":
               r=self.var_data.get()
               my_cursor.execute("Select * from student where Roll=%s",( r,
               ))
               data=my_cursor.fetchall()
               if data==[]:
                  messagebox.showerror("Not Found","Student Not Found!!!",parent=self.root)
                  self.student_table.delete(*self.student_table.get_children())
               if len(data)!=0:
                  self.student_table.delete(*self.student_table.get_children())
                  for i in data:
                     self.student_table.insert("",END,values=i)
                  conn.commit()      
               conn.close()
            elif self.var_searchBy.get()=="Phone_No":   
               my_cursor.execute("Select * from student where Phone=%s",(str(self.var_data.get()),))
               data=my_cursor.fetchall()
               if data==[]:
                  messagebox.showerror("Not Found","Student Not Found!!!",parent=self.root)
                  self.student_table.delete(*self.student_table.get_children())
               if len(data)!=0:
                  self.student_table.delete(*self.student_table.get_children())
                  for i in data:
                     self.student_table.insert("",END,values=i)
                  conn.commit()   
               conn.close()
            else:
             messagebox.showerror("Not Found","Student Not Found!!!",parent=self.root)    
         except Exception as es: 
            messagebox.showerror("Error",f"Due in search function:{str(es)}",parent=self.root)   

if __name__=="__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()        