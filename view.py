from tkinter import *
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3 


class reportClass:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry('1200x480+60+170')
        self.root.config(bg='white')
        self.root.focus_force()
        # ==========Title============
        title=Label(self.root,text="View Student results",font=('goudy old style',30,'bold'),bg='orange',fg='#262626').place(x=10,y=15,width=1180,height=50)

    #    ==========SErach ==================
        self.var_search=StringVar()
        self.var_rid=""

        lbl_search = Label(self.root,text="Search By Roll No.", font=("goudy old style",15,"bold"),bg='white').place(x=200,y=110)
        lbl_search = Entry(self.root,textvariable=self.var_search, font=("goudy old style",20,),bg='lightyellow').place(x=380,y=110,width=170)

        btn_search = Button(self.root,text='Search',font=("goudy old style",15,"bold"),bg="#03a9f4",fg='White',cursor='hand2',command=self.search).place(x=565,y=110, width=150,height=35)
        btn_clear = Button(self.root,text='Clear',font=("goudy old style",15,"bold"),bg="gray",fg='White',cursor='hand2',command=self.clear).place(x=735,y=110, width=150,height=35)

# ================  Result Labels ======================
        lbl_roll =Label(self.root,text='Roll No',font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=150,y=230,width=150,height=50)
        lbl_name =Label(self.root,text='Name',font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=300,y=230,width=150,height=50)
        lbl_course =Label(self.root,text='Course',font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=450,y=230,width=150,height=50)
        lbl_mark_obt =Label(self.root,text='Marks Obtained',font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=600,y=230,width=150,height=50)
        lbl_mark_total =Label(self.root,text='Total Marks',font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=750,y=230,width=150,height=50)
        lbl_per =Label(self.root,text='Percentage',font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE).place(x=900,y=230,width=150,height=50)

        self.roll =Label(self.root,font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.roll.place(x=150,y=280,width=150,height=50)
        self.name =Label(self.root,font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.name.place(x=300,y=280,width=150,height=50)
        self.course =Label(self.root,font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.course.place(x=450,y=280,width=150,height=50)
        self.mark_obt =Label(self.root,font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.mark_obt.place(x=600,y=280,width=150,height=50)
        self.mark_total =Label(self.root,font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.mark_total.place(x=750,y=280,width=150,height=50)
        self.per =Label(self.root,font=('goudy old style',15,'bold'),bg='white',bd=2,relief=GROOVE)
        self.per.place(x=900,y=280,width=150,height=50)


# =============  Button Delete  ====================
        btn_delete = Button(self.root,text='Delete',font=("goudy old style",15,"bold"),bg="red",fg='White',cursor='hand2',command=self.delete).place(x=530,y=350, width=150,height=40)
       

# ================  SEARCH  ===================
    def search(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            if self.var_search.get()=='':
                messagebox.showerror('Error','Roll No should be required',parent=self.root)
            else:
                cursr.execute('select * from result where roll=?',(self.var_search.get(),))
                row= cursr.fetchone()
                if row!=None:
                    self.var_id=row[0]
                    self.roll.config(text=row[1])
                    self.name.config(text=row[2])
                    self.course.config(text=row[3])
                    self.mark_obt.config(text=row[4])
                    self.mark_total.config(text=row[5])
                    self.per.config(text=row[6])
                else:
                    messagebox.showerror('Error','No rocord found',parent=self.root)
        except Exception as ex:
            messagebox.showerror('Error',f'Error due to {str(ex)}')

# ========  Clear function ======
    def clear(self):
        self.var_id==''
        self.roll.config(text='')
        self.name.config(text='')
        self.course.config(text='')
        self.mark_obt.config(text='')
        self.mark_total.config(text='')
        self.per.config(text='')
        self.var_search.set('')
    
# ========  Delete Function  ============
    def delete(self):
        con = sqlite3.connect(database='rms.db')
        cursr = con.cursor()
        try:
            if self.var_id=="":
                messagebox.showerror("Error","Search Student result first",parent=self.root)
            else:
                cursr.execute("select*from result where rid=?",(self.var_id,))
                row = cursr.fetchone()
                if row == None:
                    messagebox.showerror("Error","Invalid Student result",parent=self.root)
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete ?",parent=self.root)
                    if op==True:
                        cursr.execute("delete from result where rid=?",(self.var_id,))
                        con.commit()
                        messagebox.showinfo("Delete","Result deleted Successfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Eroor",f"Error due to {str(ex)}")




if __name__=="__main__":
    root = Tk()
    obj = reportClass(root)
    root.mainloop()
