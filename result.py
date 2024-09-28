from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3 



class resultClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry('1200x480+60+170')
        self.root.config(bg='white')
        self.root.focus_force()
        # ==========Title============
        title=Label(self.root,text="Add Student Results",font=('goudy old style',30,'bold'),bg='orange',fg='#262626').place(x=10,y=15,width=1180,height=50)

        # ===========  Widgets  ===========================
        # ========= Variables ================
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_mark_obt = StringVar()
        self.var_full_mark = StringVar()
        self.roll_list = []
        self.fetch_roll()





        lbl_select = Label(self.root,text="Select Student", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=110)
        lbl_name = Label(self.root,text="Name", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=160)
        lbl_course = Label(self.root,text="Course", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=210)
        lbl_mark_obt = Label(self.root,text="Marks Obtained", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=260)
        lbl_full_marks = Label(self.root,text="Full Marks", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=310)
       
        # ============= Entry =============

        self.txt_select = ttk.Combobox(self.root,textvariable=self.var_roll,values=(self.roll_list) ,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_select.place(x=240,y=110,width=180)
        self.txt_select.set('Select Student')
        btn_search = Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg='White',cursor='hand2',command=self.search).place(x=440,y=110, width=130,height=28)

        # txt_select = Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=100,y=60,width=200)
        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg='lightyellow',state='readonly').place(x=240,y=160,width=330)
        txt_course = Entry(self.root,textvariable=self.var_course, font=("goudy old style",15,"bold"),bg='lightyellow',state='readonly').place(x=240,y=210,width=330)
        txt_mark_obt = Entry(self.root,textvariable=self.var_mark_obt,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=240,y=260,width=330)
        txt_full_mark = Entry(self.root,textvariable=self.var_full_mark,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=240,y=310,width=330)        

        # ================  Buttons ============
        btn_submit = Button(self.root,text='Submit',font=("times new roman",15),bg="lightgreen",activebackground='lightgreen',cursor='hand2',command=self.add).place(x=270,y=390, width=110,height=40)
        btn_clear = Button(self.root,text='Clear',font=("times new roman",15),bg="lightgray",activebackground='lightgray',cursor='hand2',command=self.clear).place(x=420,y=390, width=110,height=40)


        # ======= Result Image ================
        self.bg_img = Image.open("images/result.jpg")
        self.bg_img = self.bg_img.resize((550,350),Image.AFFINE)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg = Label(self.root,image=self.bg_img).place(x=620,y=100)



        # Fxn to fetch the course in student table
    def fetch_roll(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            cursr.execute("select roll from student ")
            rows = cursr.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.roll_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")



# ================  SEARCH  ===================
    def search(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            cursr.execute('select name,course from student where roll=?',(self.var_roll.get(),))
            row= cursr.fetchone()
            if row!=None:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror('Error','No rocord found',parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}')



    def add(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            if self.var_name.get() =="":
                messagebox.showerror("Error","Please first search student record",parent=self.root)
            else:
                cursr.execute("select*from result where roll=? and course=?",(self.var_roll.get(),self.var_course.get()))
                row = cursr.fetchone()
                if row!= None:
                    messagebox.showerror("Error","Result  already present",parent=self.root)
                else:
                    per=(int(self.var_mark_obt.get())*100)/int(self.var_full_mark.get())
                    cursr.execute("insert into result (roll,name,course ,mark_obt,full_mark,per) values(?,?,?,?,?,?)",(

                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_course.get(),
                        self.var_mark_obt.get(),
                        self.var_full_mark.get(),
                        str(per)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Result Added Successfully",parent=self.root)
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")


    # Clear Function======================
    def clear(self):
        self.var_roll.set("Select"),
        self.var_name.set(""),
        self.var_course.set(""),
        self.var_mark_obt.set(""),
        self.var_full_mark.set("")


if __name__=="__main__":
    root = Tk()
    obj = resultClass(root)
    root.mainloop()