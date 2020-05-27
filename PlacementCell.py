from tkinter import *
from tkinter import ttk
from tkinter.simpledialog import askinteger,askstring
import  pymysql 
large_font=("Verdana",12)
class Student:
    def __init__(self,window):
        self.window=window
        self.window.title("Placement Cell")
        self.window.geometry("1350x550+0+0")
        
        title=Label(self.window,text="Placement Cell",bd=10,relief=GROOVE,
        font=("times new roman",50,"italic"),bg="light slate blue")
        title.pack(side=TOP,fill=X)
        #=====variables======
        self.roll_var=StringVar()
        self.back_var=StringVar()
#----------------HR FRAME------------------
        stdFrame=Frame(self.window,bd=4,relief=RIDGE,bg="light slate blue")
        stdFrame.place(x=15,y=120,width=400,height=420)
        s_title=Label(stdFrame,text="HR Query",bg="light slate blue",font=("times new roman",35,"italic"))
        s_title.grid(row=0,columnspan=2,pady=20)
        rollno=Label(stdFrame,text="Roll No.(4-digit)",bg="light slate blue",font=("times new roman",18,"italic"))
        rollno.grid(row=2,column=0,pady=10,padx=20,sticky="w")
        self.roll_val=Entry(stdFrame,textvariable=self.roll_var,font=("times new roman",10,"italic"),
        bd=5,relief=GROOVE)
        self.roll_val.grid(row=2,column=1,pady=10,padx=20,sticky="w")
        backlogs=Label(stdFrame,text="No. of backlogs",bg="light slate blue",font=("times new roman",18,"italic"))
        backlogs.grid(row=5,column=0,pady=10,padx=20,sticky="w")
        self.back_val=Entry(stdFrame,textvariable=self.back_var,font=("times new roman",10,"italic"),
        bd=5,relief=GROOVE)
        self.back_val.grid(row=5,column=1,pady=10,padx=20,sticky="w")


#------------buttons---------------------


        btn_Frame=Frame(stdFrame,bd=4,relief=RIDGE,bg="light slate blue")
        btn_Frame.place(x=10,y=240,width=370)
        submitbtn=Button(btn_Frame,text="Submit",command=self.fetch_data, width=13,height=1).grid(row=0,column=0,padx=10,
        pady=10)
        continuebtn=Button(btn_Frame,text="Clear",command=self.Continue,width=13,height=1).grid(row=0,
        column=1,padx=10,pady=10)
        closebtn=Button(btn_Frame,text="Close",width=13,height=1,command=self.closeWindow).grid(row=0,
        column=2,padx=10,pady=10)
        #txt=Label(stdFrame,text="enter allowed number of backlogs",bg="pink",
        # font=("times new roman",15,"italic"),fg="black")
        #txt.grid(row=7,column=0,pady=10,padx=20)

#----------------------------Student details frame---------------
        
        detailsFrame=Frame(self.window,bd=4,relief=RIDGE,bg="light slate blue")
        detailsFrame.place(x=410,y=120,width=600,height=420)
        d_title=Label(detailsFrame,text="Student Data",bg="light slate blue",
        font=("times new roman",35,"italic"))
        d_title.grid(row=0,columnspan=3,pady=20,padx=120)
#---------------------eligible student table---------------------
        self.tableFrame=Frame(detailsFrame,bd=4,relief=RIDGE,bg="light slate blue")
        self.tableFrame.place(x=5,y=75,width=580,height=338)
        #xscroll=Scrollbar(tableFrame,orient=HORIZONTAL)
        #yscroll=Scrollbar(tableFrame,orient=VERTICAL)
        #s_table=ttk.Treeview(tableFrame,rows=("r","n","e"),
        # xscrollcommand=xscroll.set,yscrollcommand=yscroll.set)
        #xscroll.pack(side=BOTTOM,fill=X)
        #yscroll.pack(side=RIGHT,fill=Y)
        #xscroll.config(command=s_table.xview)
        #yscroll.config(command=s_table.yview)
    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="12345",database="placement")
        cur=con.cursor()
        print("connected")
        count=cur.execute("select roll_no from student where roll_no=%s and backlogs<=%s",
        (self.roll_var.get(),self.back_var.get()))
        if count==0:
            self.note=Label(self.tableFrame,text="THE STUDENT IS NOT ELIGIBLE!",bd=1,font=("verdana",20,"italic")
            ,bg="light slate blue",fg="red")
            self.note.grid(row=6,column=5)
            self.flag=1
        else:
            cur.execute("select roll_no from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.rno=Label(self.tableFrame,text="Roll_no",bd=1,font=("times new roman",12,"bold")
            ,bg="light slate blue")
            self.rno.grid(row=5,column=3,sticky="w")
        #============displaing roll number======
            for row in cur:
                self.rno_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic")
                ,bg="light slate blue",fg="white")
                self.rno_val.grid(row=5,column=4,sticky="w")
            #print(row)
            cur.execute("select name from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.name=Label(self.tableFrame,text="Name",bd=1,font=("times new roman",12,"bold")
            ,bg="light slate blue")
            self.name.grid(row=6,column=3,sticky="w")
        #====================displaying name====================
            for row in cur:
                self.name_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.name_val.grid(row=6,column=4,sticky="w")
            cur.execute("select father_name from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.father_name=Label(self.tableFrame,text="Father Name",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.father_name.grid(row=7,column=3,sticky="w")
        #====================displaying father name====================
            for row in cur:
                self.father_name_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.father_name_val.grid(row=7,column=4,sticky="w")
            cur.execute("select dob from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.dob=Label(self.tableFrame,text="DOB",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.dob.grid(row=8,column=3,sticky="w")
        #====================displaying dob====================
            for row in cur:
                self.dob_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.dob_val.grid(row=8,column=4,sticky="w")
            cur.execute("select branch from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.branch=Label(self.tableFrame,text="Branch",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.branch.grid(row=9,column=3,sticky="w")
            #====================displaying branch====================
            for row in cur:
                self.branch_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.branch_val.grid(row=9,column=4,sticky="w")
            cur.execute("select 10th_percentage from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.p1=Label(self.tableFrame,text="10th_Percentage",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.p1.grid(row=10,column=3,sticky="w")
        #====================displaying 10th %====================
            for row in cur:
                self.p1_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.p1_val.grid(row=10,column=4,sticky="w")
            cur.execute("select 12th_percentage from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.p2=Label(self.tableFrame,text="12th_Percentage",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.p2.grid(row=11,column=3,sticky="w")
        #====================displaying 12th %===================
            for row in cur:
                self.p2_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.p2_val.grid(row=11,column=4,sticky="w")
            cur.execute("select be_percentage from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.p3=Label(self.tableFrame,text="BE_Percentage",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.p3.grid(row=12,column=3,sticky="w")
        #====================displaying be%====================
            for row in cur:
                self.p3_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.p3_val.grid(row=12,column=4,sticky="w")
            cur.execute("select college_name from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.clg=Label(self.tableFrame,text="College name",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.clg.grid(row=13,rowspan=2,column=3,sticky="w")
        #====================displaying college name====================
            for row in cur:
                self.clg_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.clg_val.grid(row=13,rowspan=2,column=4,sticky="w")
            cur.execute("select university from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.uni=Label(self.tableFrame,text="University",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.uni.grid(row=15,column=3,sticky="w")
        #====================displaying university====================
            for row in cur:
                self.uni_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.uni_val.grid(row=15,column=4,sticky="w")
            cur.execute("select contact from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.ph=Label(self.tableFrame,text="Phone Number",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.ph.grid(row=16,column=3,sticky="w")
        #====================displaying phone number====================
            for row in cur:
                self.ph_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.ph_val.grid(row=16,column=4,sticky="w")
            cur.execute("select email from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.email=Label(self.tableFrame,text="Email",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.email.grid(row=17,column=3,sticky="w")
        #====================displaying email====================
            for row in cur:
                self.email_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.email_val.grid(row=17,column=4,sticky="w")
            cur.execute("select hobbies from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.hby=Label(self.tableFrame,text="Hobbies",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.hby.grid(row=18,column=3,sticky="w")
        #====================displaying hobbies====================
            for row in cur:
                self.hby_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.hby_val.grid(row=18,column=4,sticky="w")
            cur.execute("select technical_skills from student where roll_no=%s and backlogs<=%s",(self.roll_var.get(),self.back_var.get()))
            self.tch=Label(self.tableFrame,text="Technical Skills",bd=1,font=("times new roman",12,"bold"),
            bg="light slate blue")
            self.tch.grid(row=19,column=3,sticky="w")
        #====================displaying technical skills====================
            for row in cur:
                self.tch_val=Label(self.tableFrame,text=row,bd=1,font=("verdana",10,"italic"),
                bg="light slate blue",fg="white")
                self.tch_val.grid(row=19,column=4,sticky="w")
            self.flag=0
            con.commit()
            con.close()
    def closeWindow(self):
        window.destroy()
    def Continue(self):
        if self.flag==1:
            self.note.config(text="")
        else:
            self.rno_val.config(text="")
            self.name_val.config(text="")
            self.father_name_val.config(text="")
            self.dob_val.config(text="")
            self.branch_val.config(text="")
            self.p1_val.config(text="")
            self.p2_val.config(text="")
            self.p3_val.config(text="")
            self.clg_val.config(text="")
            self.uni_val.config(text="")
            self.ph_val.config(text="")
            self.email_val.config(text="")
            self.hby_val.config(text="")
            self.tch_val.config(text="")
            self.branch.config(text="")
            self.dob.config(text="")
            self.rno.config(text="")
            self.name.config(text="")
            self.father_name.config(text="")
            self.p1.config(text="")
            self.p2.config(text="")
            self.p3.config(text="")
            self.clg.config(text="")
            self.uni.config(text="")
            self.ph.config(text="")
            self.email.config(text="")
            self.hby.config(text="")
            self.tch.config(text="")
        
window=Tk()
s=Student(window)
#window.configure(bg="red")
window.mainloop()
