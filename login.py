from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from main import Face_Recognition_System

def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self,root):
      self.root=root
      self.root.title("Login")
      self.root.geometry("1550x800+0+0")
      self.root.wm_iconbitmap("images/icon.ico")

      self.bg=ImageTk.PhotoImage(file=r"images/loginbg.jpg")
      lbl_bg=Label(self.root,image=self.bg)
      lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

      frame=Frame(self.root,bg="skyblue",highlightbackground="black", highlightthickness=1)
      frame.place(x=610,y=170,width=340,height=450)
      

      img1=Image.open(r"images/loginavatar1.png")
      img1=img1.resize((100,100),Image.Resampling.LANCZOS)  
      self.photoimage1=ImageTk.PhotoImage(img1)
      lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
      lblimg1.place(x=730,y=175,width=100,height=90)
      
      get_str=Label(frame,text="Get Started",font=("times new roman",20,"bold"),fg="indigo",bg="skyblue")
      get_str.place(x=95,y=100)

      #UserName
      username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="indigo",bg="skyblue")
      username.place(x=70,y=155)

      self.txtuser =ttk.Entry(frame,font=("times new roman",15,"bold"))
      self.txtuser.place(x=40,y=180,width=270)

      #Password
      password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="indigo",bg="skyblue")
      password.place(x=70,y=225)

      self.txtpass =ttk.Entry(frame,font=("times new roman",15,"bold"),show="*",)
      self.txtpass.place(x=40,y=250,width=270)

      #IconImages
      img2=Image.open(r"images/username1.jpeg")
      img2=img2.resize((25,25),Image.Resampling.LANCZOS)  
      self.photoimage2=ImageTk.PhotoImage(img2)
      lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
      lblimg1.place(x=650,y=323,width=25,height=25)

      img3=Image.open(r"images/pass.jpeg")
      img3=img3.resize((25,25),Image.Resampling.LANCZOS)  
      self.photoimage3=ImageTk.PhotoImage(img3)
      lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
      lblimg1.place(x=650,y=393,width=25,height=25)

      #loginbtn
      loginbtn=Button(frame,command=self.login,text="Login",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="black")
      loginbtn.place(x=110,y=300,width=120,height=35)

      #registerbtn
      registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="indigo",bg="skyblue",activebackground="skyblue",activeforeground="white")
      registerbtn.place(x=15,y=350,width=160)

      #forgotpassbtn
      forgotbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="indigo",bg="skyblue",activebackground="skyblue",activeforeground="white")
      forgotbtn.place(x=10,y=370,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)

       

    def login(self):
         if self.txtuser.get()=="" or self.txtpass.get()=="":
             messagebox.showerror("Error","Enter All Credentials Required")
         elif self.txtuser.get()=="Admin" and self.txtpass.get()=="Admin":
             messagebox.showinfo("Success","Login SucccessFully")
         else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Samarth123@",database="capstone")
            my_cursor=conn.cursor()   
            my_cursor.execute("select * from register where email=%s and password=%s",(
                self.txtuser.get(),
                self.txtpass.get()
            ))
            row=my_cursor.fetchall()
            if row==None:
                messagebox.showerror("Error","Invalid UserName and Password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only Admin")
                if open_main>0:
                         self.new_window=Toplevel(self.root)
                         self.app=Face_Recognition_System(self.new_window)                                                       #insert here the project file 
                else:
                    if not open_main:
                        return
            conn.commit()      
            conn.close()

    #reset Password
    def reset_pass(self):
        if self.combo_security_Q.get()=="Select":
            messagebox.showerror("Error","Select The Security Question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.new_password.get()=="":
            messagebox.showerror("Error","Please Enter New Password",parent=self.root2)    
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Samarth123@",database="capstone")
            my_cursor=conn.cursor() 
            qury=("select * from register where email=%s and securityQ=%s and securityA=%s")
            val=(self.txtuser.get(),self.combo_security_Q.get(),self.txt_security.get(),)
            my_cursor.execute(qury,val)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.new_password.get(),self.txtuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your Password has been Reset & Please Login with new Password",parent=self.root2)
                self.root2.destroy()

    #forgot Password Window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please enter the Email to reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Samarth123@",database="capstone")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.txtuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter Correct Email")
            else:
                conn.close()
                self.root2=Toplevel()    
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")     

                l=Label(self.root2,text="Forgot Password",font=("times new roman",20,"bold"),fg="white",bg="skyblue")     
                l.place(x=0,y=10,relwidth=1)
                
                security_Q =Label(self.root2,text="Select Security Question",font=("times new roman",15,"bold"),bg="skyblue")
                security_Q.place(x=50,y=80)

                self.combo_security_Q=ttk.Combobox(self.root2,font=("times new roman",15,"bold"),state="readonly")
                self.combo_security_Q["values"]=("Select","Your Birth Place","Your School name","Your Nick Name")
                self.combo_security_Q.place(x=50,y=110,width=250)
                self.combo_security_Q.current(0)

                security_A =Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="skyblue")
                security_A.place(x=50,y=150)
                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.txt_security.place(x=50,y=180,width=250)

                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="skyblue")
                new_password.place(x=50,y=220)
                self.new_password=ttk.Entry(self.root2,font=("times new roman",15,"bold"))
                self.new_password.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset Password",command=self.reset_pass,font=("times new roman",15,"bold"),bg="skyblue")
                btn.place(x=100,y=290)



class Register:
    def __init__(self,root) :
        self.root=root
        self.root.title("Register")
        self.root.geometry("1550x800+0+0")

        #Variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_SecurityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
       

        #background Image
        self.bg=ImageTk.PhotoImage(file=r"images/loginbg.jpg")
        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)            #relwidth & relheight adjust the size of the image according to the window


        #Left side Image
        self.bg1=ImageTk.PhotoImage(file=r"images/registerfi.png")
        left_bg=Label(self.root,image=self.bg1)
        left_bg.place(x=50,y=100,width=470,height=550)

        

        #mainframe            frame is in tkinter package
        frame = Frame(self.root,bg="skyblue")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="Register Here",font=("times new roman",25,"bold"),fg="indigo",bg="skyblue")
        register_lbl.place(x=250,y=20) 

        #Label and entry(textfield)

        #row 1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="skyblue")
        fname.place(x=50,y=100)
        fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        fname_entry.place(x=50,y=130,width=250)

        lname =Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="skyblue")
        lname.place(x=370,y=100)
        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15,"bold"))
        self.txt_lname.place(x=370,y=130,width=250)

        #row2
        contact =Label(frame,text="Contact Number",font=("times new roman",15,"bold"),bg="skyblue")
        contact.place(x=50,y=170)
        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15,"bold"))
        self.txt_contact.place(x=50,y=200,width=250)

        email =Label(frame,text="Email",font=("times new roman",15,"bold"),bg="skyblue")
        email.place(x=370,y=170)
        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15,"bold"))
        self.txt_email.place(x=370,y=200,width=250)

        #row3
        security_Q =Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="skyblue")
        security_Q.place(x=50,y=240)
        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times new roman",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("Select","Your Birth Place","Your School name","Your Nick Name")
        self.combo_security_Q.place(x=50,y=270,width=250)
        self.combo_security_Q.current(0)

        security_A =Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="skyblue")
        security_A.place(x=370,y=240)
        self.txt_security=ttk.Entry(frame,textvariable=self.var_SecurityA,font=("times new roman",15,"bold"))
        self.txt_security.place(x=370,y=270,width=250)

        #row4
        pswd =Label(frame,text="Password",font=("times new roman",15,"bold"),bg="skyblue")
        pswd.place(x=50,y=310)
        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"),show="*")
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd =Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="skyblue")
        confirm_pswd.place(x=370,y=310)
        self.txt_confirm_pswd=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"),show="*")
        self.txt_confirm_pswd.place(x=370,y=340,width=250)

        #checkbutton(checkbox)
        self.var_check=IntVar()
        checkbtn=Checkbutton(frame,variable=self.var_check,text="I Agree the Terms & Conditions",font=("times new roman",12,"bold"),bg="skyblue",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=380)

        #buttons
        #1.Register
        img=Image.open(r"images/registerlogo.jpg")
        img=img.resize((200,50),Image.Resampling.LANCZOS)                    #Resampling.LANCZOS=convert the high quality image to low Quality
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",bg="skyblue",activebackground="skyblue",activeforeground="white")
        b1.place(x=10,y=420,width=300)

        #2.login
        img1=Image.open(r"images/login.jpg")
        img1=img1.resize((200,50),Image.Resampling.LANCZOS)                    #Resampling.LANCZOS=convert the high quality image to low Quality
        self.photoimage1=ImageTk.PhotoImage(img1)
        b2=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",bg="skyblue",activebackground="skyblue",activeforeground="white")
        b2.place(x=330,y=420,width=300)



    #Function declaration
    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All Credentials are Required....",parent=self.root)
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","Password & Confirm Password must be same",parent=self.root)
        elif self.var_check.get()==0:       
            messagebox.showwarning("Error","Please Agree Terms & Conditions!!",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="Samarth123@",database="capstone")
            my_cursor=conn.cursor()
            query=("select * from register where email =%s")        #---%s=email is primary so it should not duplicate
            value=(self.var_email.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User Already Exist & Please try another email")
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                   self.var_fname.get(),
                   self.var_lname.get(),
                   self.var_contact.get(),
                   self.var_email.get(),
                   self.var_securityQ.get(),
                   self.var_SecurityA.get(),
                   self.var_pass.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Registered Successfully")    
    
    def return_login(self):
        self.root.destroy()

if __name__ == "__main__":
    main()   
    