from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3 


class StudentClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry('1200x480+60+170')
        self.root.config(bg='white')
        self.root.focus_force()
        # ==========Title============
        title=Label(self.root,text="Manage Student Details",font=('goudy old style',30,'bold'),bg='#033054',fg='white').place(x=10,y=15,width=1180,height=35)

        # =================Variables========================
        self.var_roll = StringVar()
        self.var_name = StringVar()
        self.var_email = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_adm_date = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pin = StringVar()
        self.var_contact = StringVar()
        self.var_course = StringVar()



        # =======================Widgets=======================
        
        # ==================  Column 1  ==========================
        lbl_roll = Label(self.root,text="Roll No.", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=60)
        lbl_name = Label(self.root,text="Name", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=100)
        lbl_email = Label(self.root,text="Email", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=140)
        lbl_gender = Label(self.root,text="Gender", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=180)
        
        lbl_state = Label(self.root,text="State", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=220)
        txt_state = Entry(self.root,textvariable=self.var_state,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=100,y=220,width=150)
        
        lbl_city = Label(self.root,text="City", font=("goudy old style",15,"bold"),bg='white').place(x=260,y=220)
        txt_city = Entry(self.root,textvariable=self.var_city,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=310,y=220,width=150)
        
        lbl_pin = Label(self.root,text="Pin Code", font=("goudy old style",15,"bold"),bg='white').place(x=470,y=220)
        txt_pin = Entry(self.root,textvariable=self.var_pin,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=560,y=220,width=130)



        lbl_address = Label(self.root,text="Address", font=("goudy old style",15,"bold"),bg='white').place(x=10,y=260)
        # ====================  Column 2  ==========================
        lbl_dob = Label(self.root,text="D.O.B(dd-mm-yyyy)", font=("goudy old style",15,"bold"),bg='white').place(x=320,y=60)
        lbl_contact = Label(self.root,text="Contact No.", font=("goudy old style",15,"bold"),bg='white').place(x=320,y=100)
        lbl_adm__date = Label(self.root,text="Admission Date", font=("goudy old style",15,"bold"),bg='white').place(x=320,y=140)
        lbl_course = Label(self.root,text="Select Course", font=("goudy old style",15,"bold"),bg='white').place(x=320,y=180)




        # =================Entry Fields ==================
        # =============  Column 1  =======================
        
        self.txt_roll = Entry(self.root,textvariable=self.var_roll,font=("goudy old style",15,"bold"),bg='lightyellow')
        self.txt_roll.place(x=100,y=60,width=200)
        txt_name = Entry(self.root,textvariable=self.var_name,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=100,y=100,width=200)
        txt_email = Entry(self.root,textvariable=self.var_email, font=("goudy old style",15,"bold"),bg='lightyellow').place(x=100,y=140,width=200)
        self.txt_gender = ttk.Combobox(self.root,textvariable=self.var_gender,values=('Select','Male','Female','Other') ,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_gender.place(x=100,y=180,width=200)
        self.txt_gender.current(0)
        

        
        # ==================  Text Address =====================
        self.txt_address = Text(self.root, font=("goudy old style",15,"bold"),bg='lightyellow')
        self.txt_address.place(x=100,y=260,width=590,height=120)
       
        # ====================== Column 2 ===================
        self.course_list = []
        # fxn call to update the list
        self.fetch_course()   #fetch fxn call
        self.txt_dob = Entry(self.root,textvariable=self.var_dob,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=490,y=60,width=200)
        txt_contact = Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=490,y=100,width=200)
        txt_admission = Entry(self.root,textvariable=self.var_adm_date, font=("goudy old style",15,"bold"),bg='lightyellow').place(x=490,y=140,width=200)
        self.txt_course = ttk.Combobox(self.root,textvariable=self.var_course,values=(self.course_list) ,font=("goudy old style",15,"bold"),state='readonly',justify=CENTER)
        self.txt_course.place(x=490,y=180,width=200)
        self.txt_course.set('Select Course')




        # =============== Buttons ===========================
        self.btn_add = Button(self.root,text='Saved',font=("goudy old style",15,"bold"),bg="#2196f3",fg='White',cursor='hand2',command=self.add)
        self.btn_add.place(x=150,y=400, width=110,height=40)
        self.btn_update = Button(self.root,text='Update',font=("goudy old style",15,"bold"),bg="#4caf50",fg='White',cursor='hand2',command=self.update)
        self.btn_update.place(x=270,y=400, width=110,height=40)
        self.btn_delete = Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="#f44336",fg='White',cursor='hand2',command=self.delete)
        self.btn_delete.place(x=390,y=400, width=110,height=40)
        self.btn_clear = Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="#607d8b",fg='White',cursor='hand2',command=self.clear)
        self.btn_clear.place(x=510,y=400, width=110,height=40)

        # ================Search panel =====================
        self.var_search = StringVar()
        lbl_search_roll = Label(self.root,text="Roll No", font=("goudy old style",15,"bold"),bg='white').place(x=720,y=60)
        txt_search_roll = Entry(self.root,textvariable=self.var_search,font=("goudy old style",15,"bold"),bg='lightyellow').place(x=870,y=60,width=180)
        btn_search = Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg='White',cursor='hand2',command=self.search).place(x=1070,y=60, width=120,height=28)

        # ================= Course Content =======================

        self.Course_Frame = Frame(self.root,bd=2,relief=RIDGE)
        self.Course_Frame.place(x=720,y=100,width=470,height=340)


        scrolly = Scrollbar(self.Course_Frame,orient=VERTICAL)
        scrollx = Scrollbar(self.Course_Frame,orient=HORIZONTAL)
        
        
        self.CourseTable = ttk.Treeview(self.Course_Frame,columns=('roll','name','email','gender','dob','contact','admission','course','state','city','pin','address'),xscrollcommand=scrollx.set,yscrollcommand=scrolly.set)

        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CourseTable.xview)
        scrolly.config(command=self.CourseTable.yview)
        

        # =============  Student Table headings ==================
        self.CourseTable.heading('roll',text='Roll No')
        self.CourseTable.heading('name',text='Name')
        self.CourseTable.heading('email',text='Email')
        self.CourseTable.heading('gender',text='Gender')
        self.CourseTable.heading('dob',text='D.O.B')
        self.CourseTable.heading('contact',text='Contact')
        self.CourseTable.heading('admission',text='Admission')
        self.CourseTable.heading('course',text='Course')

        self.CourseTable.heading('state',text='State')
        self.CourseTable.heading('city',text='City')
        self.CourseTable.heading('pin',text='Pin')
        self.CourseTable.heading('address',text='Address')
        
        self.CourseTable['show'] = 'headings'

        # ==========Student Table columns ======================
        self.CourseTable.column('roll',width=100)
        self.CourseTable.column('name',width=100)
        self.CourseTable.column('email',width=100)
        self.CourseTable.column('gender',width=100)
        self.CourseTable.column('dob',width=150)
        self.CourseTable.column('contact',width=100)
        self.CourseTable.column('admission',width=100)
        self.CourseTable.column('course',width=100)
        self.CourseTable.column('state',width=100)
        self.CourseTable.column('city',width=150)
        self.CourseTable.column('pin',width=100)
        self.CourseTable.column('address',width=100)

        self.CourseTable.pack(fill=BOTH,expand=1)
        self.CourseTable.bind("<ButtonRelease-1>",self.get_data)
        self.show()    # Show function call
        



    # ================== Clear ==============
    def clear(self):
        self.show()   #Show fxn call
        self.var_roll.set(""),
        self.var_name.set(""),
        self.var_email.set(""),
        self.var_gender.set("Select"),
        self.var_dob.set(""),
        self.var_contact.set(""),
        self.var_adm_date.set(""),
        self.var_course.set("Select"),
        self.var_state.set(""),
        self.var_city.set(""),
        self.var_pin.set(""),
        self.txt_address.delete("1.0",END)
        self.txt_roll.config(state=NORMAL)
        self.var_search.set("")


    def delete(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            if self.var_roll.get() =="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cursr.execute("select*from student where roll=?",(self.var_roll.get(),))
                row = cursr.fetchone()
                if row == None:
                    messagebox.showerror("Error","Plese Select student from the list first",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cursr.execute("delete from student where roll=?",(self.var_roll.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","Student deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")


# It show the data in fields when we select it in student table
    def get_data(self,event):
        self.txt_roll.config(state='readonly')
        r = self.CourseTable.focus()
        content = self.CourseTable.item(r)
        row = content["values"]
        self.var_roll.set(row[0]),
        self.var_name.set(row[1]),
        self.var_email.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_contact.set(row[5]),
        self.var_adm_date.set(row[6]),
        self.var_course.set(row[7]),
        self.var_state.set(row[8]),
        self.var_city.set(row[9]),
        self.var_pin.set(row[10]),
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[11])


        


    def add(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            if self.var_roll.get() =="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cursr.execute("select*from student where roll=?",(self.var_roll.get(),))
                row = cursr.fetchone()
                if row!= None:
                    messagebox.showerror("Error","Roll Number already present",parent=self.root)
                else:
                    cursr.execute("insert into student (roll,name,email,gender,dob,contact,admission,course,state,city,pin,address) values(?,?,?,?,?,?,?,?,?,?,?,?)",(

                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),

                        self.txt_address.get("1.0",END)
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student Added Successfully",parent=self.root)
                    self.show()    # show function call to display Course list
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")


    def update(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            if self.var_roll.get() =="":
                messagebox.showerror("Error","Roll Number should be required",parent=self.root)
            else:
                cursr.execute("select*from student where roll=?",(self.var_roll.get(),))
                row = cursr.fetchone()
                if row == None:
                    messagebox.showerror("Error","Select student from List",parent=self.root)
                else:
                    cursr.execute("update student set name=?,email=?,gender=?,dob=?,contact=?,admission=?,course=?,state=?,city=?,pin=?,address=? where roll=?",( 
                        self.var_name.get(),
                        self.var_email.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_contact.get(),
                        self.var_adm_date.get(),
                        self.var_course.get(),
                        self.var_state.get(),
                        self.var_city.get(),
                        self.var_pin.get(),
                        self.txt_address.get("1.0",END),
                        self.var_roll.get()
                    ))
                    con.commit()
                    messagebox.showinfo("Success","Student updated Successfully",parent=self.root)
                    self.show()    # show function call to display Course list
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")










    def show(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            cursr.execute("select*from student ")
            rows = cursr.fetchall()
            self.CourseTable.delete(*self.CourseTable.get_children())
            for row in rows:
                self.CourseTable.insert('',END,values=row)
                
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")

    # Fxn to fetch the course in student table
    def fetch_course(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            cursr.execute("select name from course ")
            rows = cursr.fetchall()
            if len(rows)>0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")


    def search(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            cursr.execute(f"select*from student where roll=?" ,(self.var_search.get(),))
            row = cursr.fetchone()
            if row!=None:
                self.CourseTable.delete(*self.CourseTable.get_children())
                self.CourseTable.insert('',END,values=row)
            else:
                messagebox.showerror("Error","No record found",parent=self.root)   
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")






if __name__=="__main__":
    root = Tk()
    obj = StudentClass(root)
    root.mainloop()

