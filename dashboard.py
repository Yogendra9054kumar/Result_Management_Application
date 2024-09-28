from tkinter import *
from PIL import Image,ImageTk
from course import CourseClass
from student import StudentClass
from result import resultClass
from view import reportClass





class RMS:
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry('1350x680+0+0')
        self.root.config(bg='white')

        # ==========Icons=============
        self.logo_dash = ImageTk.PhotoImage(file='images/logo.png')


        # ==========Title============
        title=Label(self.root,text="Student Result Management System",image=self.logo_dash,compound=LEFT,padx=10,font=('goudy old style',30,'bold'),bg='#033054',fg='white').place(x=0,y=0,relwidth=1,height=50)

        # ================ MENU ==================
        Menu_frame = LabelFrame(self.root,text="Menus",font=('times new roman',15),bg='white')
        Menu_frame.place(x=10,y=70,width=1252,height=80)


        btn_course = Button(Menu_frame,text='Course',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.add_course).place(x=20,y=5,width=185,height=40)
        btn_student = Button(Menu_frame,text='student',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.add_student).place(x=235,y=5,width=185,height=40)
        btn_result = Button(Menu_frame,text='result',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.add_result).place(x=430,y=5,width=185,height=40)
        btn_view = Button(Menu_frame,text='view',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2',command=self.add_view).place(x=635,y=5,width=185,height=40)
        btn_logout = Button(Menu_frame,text='logout',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2').place(x=840,y=5,width=185,height=40)
        btn_exit = Button(Menu_frame,text='exit',font=('goudy old style',15,'bold'),bg='#0b5377',fg='white',cursor='hand2')
        btn_exit.place(x=1045,y=5,width=185,height=40)



        # =====================   Content_Window   ====================
        self.bg_img = Image.open("images/ContentBackground.jpg")
        self.bg_img = self.bg_img.resize((880,350),Image.AFFINE)
        self.bg_img=ImageTk.PhotoImage(self.bg_img)
        
        self.lbl_bg = Label(self.root,image=self.bg_img).place(x=400,y=180,width=880,height=350)


        #====================== UPDTAE Details==================
        self.lbl_course = Label(self.root,text="Total Courses\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#e43b06",fg="White")
        self.lbl_course.place(x=400,y=530,width=283,height=100)
        self.lbl_student = Label(self.root,text="Total Students\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#0676ad",fg="White")
        self.lbl_student.place(x=693,y=530,width=283,height=100)
        self.lbl_result = Label(self.root,text="Total Results\n[0]",font=("goudy old style",20),bd=10,relief=RIDGE,bg="#038074",fg="White")
        self.lbl_result.place(x=986,y=530,width=283,height=100)

        


        # ========== Footer ============
        footer=Label(self.root,text="SRMS-Student Result Management System\nContact Us for any Technical Issues: 841XXXXX45",font=('goudy old style',12),bg='#262626',fg='white').pack(side=BOTTOM,fill=X)

    # when we click on Course btn it will click to the course Button
    def add_course(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_window)

    def add_student(self):
        self.new_window = Toplevel(self.root)
        self.new_obj = StudentClass(self.new_window)
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=resultClass(self.new_win)
    
    def add_view(self):
        self.new_win = Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)


if __name__=="__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()