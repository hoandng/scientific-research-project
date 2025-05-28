from PIL import Image, ImageTk,ImageDraw
from tkinter import *
from tkinter import ttk
import PIL.Image ,PIL.ImageDraw
from datetime import *
import time
from time import strftime
from math import *
import mysql.connector
from tkinter import messagebox
from main import Face_Recognition_System
from main import new_print

class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Đăng nhập")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        today = strftime("%d-%m-%Y")  # time_today

        # =============variable============
        self.var_email = StringVar()
        self.var_password = StringVar()

        left_lbl=Label(self.root,bg="#08A3D2",bd=0)
        left_lbl.place(x=0,y=0,relheight=1,width=600)

        right_lbl = Label(self.root, bg="#031F3C", bd=0)
        right_lbl.place(x=600, y=0, relheight=1, relwidth=1)

        #===========Frame============
        login_frame=Frame(self.root,bg="white")
        login_frame.place(x=250,y=100,width=800,height=500)
        #===========style_ttk.tentry===========
        self.estyle = ttk.Style()
        self.estyle.configure("EntryStyle.TEntry", background='black')

        title=Label(login_frame,text="Đăng nhập ",font=("times new roman",30,"bold"),bg="white",fg="#08A3D2").place(x=250,y=40)

        email = Label(login_frame, text="Email", font=("times new roman", 18, "bold"), bg="white",
                      fg="gray").place(x=250, y=130)
        self.txtuser=ttk.Entry(login_frame,textvariable=self.var_email, font=("times new roman", 15))
        self.txtuser.place(x=250, y=160,height=35,width=350)

        pass_word = Label(login_frame, text="Mật khẩu", font=("times new roman", 18, "bold"), bg="white",
                      fg="gray").place(x=250, y=220)
        self.txtpass = ttk.Entry(login_frame, textvariable=self.var_password,font=("times new roman", 15), background="black" ,show="*")
        self.txtpass.place(x=250, y=250,height=35,width=350)

        # =============check_button=============
        self.varcheck = IntVar()
        checkbtn = Checkbutton(login_frame, variable=self.varcheck, text="Đăng nhập bằng tài khoản Admin",
                               font=("times new roman", 12), onvalue=1, offvalue=0)
        checkbtn.place(x=250, y=320)



        btn_login = Button(login_frame, text="Đăng nhập", command=self.login,font=("times new roman", 17,"bold"), fg="white", bd=0,
                            bg="#B00857",cursor="hand2").place(x=250, y=400,width=220,height=40)



    def reset(self):
        self.var_email.set("")
        self.var_password.set("")
        self.varcheck.set(0)
    def working(self):
        h=datetime.now().time().hour
        m = datetime.now().time().minute
        s = datetime.now().time().second

        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360

        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file= "ImageFaceDetect\clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Lỗi !!","Vui lòng nhập đầy đủ thông tin")
        elif(self.varcheck.get()==1) :
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='face_recognizer',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select * from admin where Account=%s and Password=%s", (
                self.var_email.get(),
                self.var_password.get()
            ))
            row = my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Lỗi", "Sai tên đăng nhập, mật khẩu hoặc quyền đăng nhập")
            else:
                new_print(str(0))
                # # self.root.destroy()
                # # import home
                self.reset()
                messagebox.showinfo("Thông báo","Bạn đã đăng nhập thành công với quyền Admin")
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()
        else:
            conn = mysql.connector.connect(host='localhost', user='root', password='', database='face_recognizer',
                                           port='3306')
            my_cursor = conn.cursor()
            my_cursor.execute("select Teacher_id from teacher where Email=%s and Password=%s",(
                                    self.var_email.get(),
                                    self.var_password.get()
            ))
            row=my_cursor.fetchone()

            # print(row[0])
            if row==None:
                messagebox.showerror("Lỗi", "Sai tên đăng nhập hoặc mật khẩu")
            else:
                new_print(str(row[0]))
                # self.root.destroy()
                # import home
                self.reset()
                self.new_window = Toplevel(self.root)
                self.app = Face_Recognition_System(self.new_window)
            conn.commit()
            conn.close()
if __name__=="__main__":
    root=Tk() #khoi tao cua so va gan root vao
    obj=Login_Window(root)
    root.mainloop()# cua so hien len