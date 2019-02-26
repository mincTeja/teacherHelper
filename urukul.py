import tkinter as tk
from tkinter import *
from pymongo import MongoClient

cli=MongoClient(port=27017)
db=cli.student1

main_page=tk.Tk()

database="var"

l1=Label(main_page, text='Pass ')
l2=Label(main_page, text='SSN  ')
name=StringVar()
ssn=IntVar()
e1 = Entry(main_page,show="*",textvariable=name) 
e2 = Entry(main_page,textvariable=ssn)
l1.grid(row=1,sticky=E)
l2.grid(row=0,sticky=E)
e1.grid(row=1, column=1) 
e2.grid(row=0, column=1)
c=Checkbutton(main_page,text="keep me logged in")
c.grid(columnspan=2)



def new_entry():
    top1=Toplevel()
    la1=Label(top1, text='Name ')
    la2=Label(top1, text='USN  ')
    la3=Label(top1, text='MSE1 ')
    la4=Label(top1, text='MSE2 ')
    nname=StringVar()
    nusn=StringVar()
    nmse1=IntVar()
    nmse2=IntVar()
    en1 = Entry(top1,textvariable=nname) 
    en2 = Entry(top1,textvariable=nusn)
    en3 = Entry(top1,textvariable=nmse1)
    en4 = Entry(top1,textvariable=nmse2)
    la1.grid(row=0,sticky=E)
    la2.grid(row=1,sticky=E)
    la3.grid(row=2,sticky=E)
    la4.grid(row=3,sticky=E)
    en1.grid(row=0, column=1) 
    en2.grid(row=1, column=1)
    en3.grid(row=2, column=1)
    en4.grid(row=3, column=1)
    def insertion():
        li=[]
        s=db[database].find()
        for i in s:
            li.append(i)
        liusn=[]
        for j in li:
            liusn.append(j['usn'])

        if nusn.get() not in liusn:

            if len(nusn.get())==10:
                d={"usn":nusn.get(),'name': nname.get(),'mse1': nmse1.get(),'mse2': nmse2.get(),'avg':(nmse1.get()+nmse2.get())/2}
                db[str(database)].insert(d)
                ad={"usn":nusn.get(),"present":0,"absent":0}
                db[database+"attendence"].insert(ad)
                top1.destroy()
            else:
                
                yerr=Toplevel()
                head=Label(yerr,text="Usn not correct..!!").pack()
                
        else:
            entryerr=Toplevel()
            head=Label(entryerr,text="The student already exists..!!").pack()
        
            

    work=Button(top1,text="submit",command=insertion).place(x=120,y=100)
    top1.geometry('300x300')


def u_name():
    up1=Toplevel()
    la1=Label(up1, text='Name ')
    la2=Label(up1, text='USN  ')
    uname=StringVar()
    uusn=StringVar()
    en1 = Entry(up1,textvariable=uname)
    en2 = Entry(up1,textvariable=uusn)
    la1.grid(row=1,sticky=E)
    la2.grid(row=0,sticky=E)
    en1.grid(row=1, column=1)
    en2.grid(row=0, column=1)
    def update_name():
        db[database].update({'usn':uusn.get()},{'$set':{'name':uname.get()}})
        up1.destroy()
    
    work=Button(up1,text="update",command=update_name).place(x=120,y=100)
    up1.geometry('200x200')
    


def u_mse1():
    up2=Toplevel()
    la1=Label(up2, text='MSE1 ')
    la2=Label(up2, text='USN  ')
    umse1=IntVar()
    uusn=StringVar()
    en1 = Entry(up2,textvariable=umse1)
    en2 = Entry(up2,textvariable=uusn)
    la1.grid(row=1,sticky=E)
    la2.grid(row=0,sticky=E)
    en1.grid(row=1, column=1)
    en2.grid(row=0, column=1)
    def update_mse1():
        db[database].update({'usn':uusn.get()},{'$set':{'mse1':umse1.get()}})
        up2.destroy()
    
    work=Button(up2,text="update",command=update_mse1).place(x=120,y=100)
    up2.geometry('200x200')

def u_mse2():
    up3=Toplevel()
    la1=Label(up3, text='MSE2 ')
    la2=Label(up3, text='USN  ')
    umse2=IntVar()
    uusn=StringVar()
    en1 = Entry(up3,textvariable=umse2)
    en2 = Entry(up3,textvariable=uusn)
    la1.grid(row=1,sticky=E)
    la2.grid(row=0,sticky=E)
    en1.grid(row=1, column=1)
    en2.grid(row=0, column=1)

    def update_mse2():
        db[database].update({'usn':uusn.get()},{'$set':{'mse2':umse2.get()}})
        up3.destroy()
    
    work=Button(up3,text="update",command=update_mse2).place(x=120,y=100)
    up3.geometry('200x200')


def update_entry():
    top2=Toplevel()
    frame=Frame(top2)
    
    b1=Button(top2,text="Name",command=u_name)
    b3=Button(top2,text="MSE1",command=u_mse1)
    b4=Button(top2,text="MSE2",command=u_mse2)
    b1.pack(side=LEFT)
    b3.pack(side=LEFT)
    b4.pack(side=LEFT)
    frame.pack()


def delete_entry():
    u1=Toplevel()
    la2=Label(u1, text='USN  ')
    dusn=StringVar()
    en2 = Entry(u1,textvariable=dusn)
    la2.grid(row=0,sticky=E)
    en2.grid(row=0, column=1)
    def remove():
        db[database].remove({"usn":dusn.get()})
        db[database+"attendence"].remove({"usn":dusn.get()})
        u1.destroy()
    
    work=Button(u1,text="delete",command=remove).place(x=80,y=50)
    u1.geometry('200x200')
def show_db():
    
    u11=Toplevel()
    la2=Label(u11, text='USN  ')
    susn=StringVar()
    en2 = Entry(u11,textvariable=susn)
    la2.grid(row=0,sticky=E)
    en2.grid(row=0, column=1)

    def find():
        a=[]
        s=db[database].find({"usn":susn.get()},{"usn":1,"name":1,"mse1":1,"mse2":1})
        for i in s:
            a.append(i)

        li=[]
        ss=db[database+"attendence"].find({"usn":susn.get()},{"usn":1,"present":1,"absent":1})
        for j in ss:
            li.append(j)

        
        try:
            print(a[0])
            disp=Toplevel()
            label1=Label(disp,text="NAME :").place(x=70,y=90)
            label2=Label(disp,text=a[0]['name']).place(x=130,y=90)
            label1=Label(disp,text="USN :").place(x=70,y=120)
            label2=Label(disp,text=a[0]['usn']).place(x=130,y=120)
            label1=Label(disp,text="MSE1 :").place(x=70,y=150)
            label2=Label(disp,text=a[0]['mse1']).place(x=130,y=150)
            label1=Label(disp,text="MSE2 :").place(x=70,y=180)
            label2=Label(disp,text=a[0]['mse2']).place(x=130,y=180)
            avg=( a[0]['mse1'] + a[0]['mse2'])/2
            label1=Label(disp,text="average :").place(x=70,y=210)
            label2=Label(disp,text=avg).place(x=130,y=210)

            label1=Label(disp,text="present :").place(x=70,y=240)
            label2=Label(disp,text=li[0]['present']).place(x=130,y=240)
            label1=Label(disp,text="absent :").place(x=70,y=270)
            label2=Label(disp,text=li[0]['absent']).place(x=130,y=270)

            total= li[0]['present'] + li[0]['absent']

            label1=Label(disp,text="attendence :").place(x=70,y=300)
            label2=Label(disp,text=(li[0]['present']/total)*100).place(x=130,y=300)

            disp.geometry('280x400')
        except:
            err=Toplevel()
            label1=Label(err,text="Check entered usn..!!").place(x=30,y=30)
            err.geometry('200x100')
        
    
    work=Button(u11,text="show",command=find).place(x=80,y=50)
    u11.geometry('200x200')

def attend():
    atten=Toplevel()

    auusn=Label(atten, text='USN ')
    pres=Label(atten, text='present ')
    absen=Label(atten, text='absent  ')
    ausn=StringVar()
    pre=IntVar()
    abse=IntVar()
    ent1 = Entry(atten,textvariable=ausn)
    ent2 = Entry(atten,textvariable=pre) 
    ent3 = Entry(atten,textvariable=abse)
    auusn.grid(row=0,sticky=E)
    pres.grid(row=1,sticky=E)
    absen.grid(row=2,sticky=E)
    ent1.grid(row=0, column=1) 
    ent2.grid(row=1, column=1)
    ent3.grid(row=2, column=1)

    def status():
        
        b=[]
        sb=db[database+'attendence'].find({"usn":ausn.get()},{"usn":1,"present":1,"absent":1})
        for i in sb:
            b.append(i)

        try:
            print(b[0]['usn'])
            db[database+'attendence'].update({'usn':ausn.get()},{'$inc':{'present':pre.get(),'absent':abse.get()}})
            atten.destroy()
        except:
            atterr=Toplevel()
            head=Label(atterr,text="The details are wrong..!!").pack()
            
    
    wo=Button(atten,text="done",command=status).place(x=60,y=100)

    atten.geometry('200x200')

def failed():
    failedmore=Toplevel()

    def one_mse():
        
        mse_failed=[]
        fin=db[database].find({ "$or": [ { "mse1":{"$lt":12}}, { "mse2": { "$lt": 12 } } ] },{"usn":1,'mse1':1,'mse2':1})
        if fin:
            for j in fin:
                d={}
                d['usn']=j['usn']
                d['mse1']=j['mse1']
                d['mse2']=j['mse2']
                mse_failed.append(d)
        print(mse_failed)
        #failshow=Toplevel()
        if mse_failed:
            roott=Toplevel()
            to = Text(roott)
            for i in mse_failed:
                to.insert(END, "usn: "+str(i['usn'])+" mse1: "+str(i['mse1'])+" mse2: "+str(i['mse2']) + '\n')
            to.pack()
        
    def avg_mse():
       
        mse_failed=[]
        
        fin=db[database].find(  { "avg":{"$lt":12}} ,{"usn":1,'mse1':1,'mse2':1,'avg':1})
        if fin:
            for j in fin:
                d={}
                d['usn']=j['usn']
                d['mse1']=j['mse1']
                d['mse2']=j['mse2']
                d['avg']=j['avg']
                mse_failed.append(d)
        print(mse_failed)
        failshow=Toplevel()
        if mse_failed:
            roott=Toplevel()
            to = Text(roott)
            for i in mse_failed:
                to.insert(END, "usn: "+str(i['usn'])+" mse1: "+str(i['mse1'])+" mse2: "+str(i['mse2']) + " avg :"+str(i['avg'])+'\n')
            to.pack()

    b1=Button(failedmore,text="failed in any mse",command=one_mse)
    b2=Button(failedmore,text="failed by avg",command=avg_mse)
    b1.pack(side=LEFT)
    b2.pack(side=LEFT)


        
                
def full_attendence():
    enusn=Toplevel()
    l1=Label(enusn,text="USN ")
    tryusn=StringVar()

    entry=Entry(enusn,textvariable=tryusn)

    l1.grid(row=0,sticky=E)
    entry.grid(row=0, column=1)

    def fatten():
        if len(tryusn.get()) == 10:
          
            a=[]
            b=[]
            s=db.teacher.find()
            for i in s:
                a.append(i)
            for j in a:
                b.append(str(j['name'])+"attendence")
            print(b)
            present=[]
            absent=[]
            usn=[]
            coll=[]
            for v in b:
                fin=db[v].find({ "usn":tryusn.get()}, {"usn":1,"present":1,"absent":1})
                for i in fin:
                    di={}
                    di['attof']=v
                    di['usn']=i['usn']
                    di['present']=i['present']
                    di['absent']=i['absent']
                    coll.append(di)
            print(coll)
            if coll:
                roo=Toplevel()
                tt = Text(roo)
                for i in coll:
                    tt.insert(END, "teacher: "+str(i['attof'])+" usn: "+str(i['usn'])+" present: "+str(i['present']) +" absent:"+str(i["absent"]) +'\n')
                tt.pack()
        else:
            faerr=Toplevel()
            head=Label(faerr,text="The usn is wrong..!!").pack()

    def irr():
        
        
        coll=[]
        
        fin=db[database+"attendence"].find({'$where':"this.absent>this.present"}, {"usn":1,"present":1,"absent":1})
        for i in fin:
            di={}
            
            di['usn']=i['usn']
            di['present']=i['present']
            di['absent']=i['absent']
            coll.append(di)
        print(coll)
        if coll:
            roo=Toplevel()
            tt = Text(roo)
            for i in coll:
                tt.insert(END, " usn: "+str(i['usn'])+" present: "+str(i['present']) +" absent:"+str(i["absent"]) +'\n')
            tt.pack()
        
    
       
    show_attend=Button(enusn,text="enter",command=fatten).place(x=60,y=50)
    show_attend1=Button(enusn,text="irregular",command=irr).place(x=100,y=50)
    
    enusn.geometry("200x200")
    
    


def more():
    nt=Toplevel()
    b1=Button(nt,text="failed",command=failed)
    b3=Button(nt,text="full attendence",command=full_attendence)
    b1.pack(side=LEFT)
    b3.pack(side=LEFT)


def do_it():
    
    x=[]
    s=db.teacher.find({"ssn":ssn.get()},{"name":1,"ssn":1,"pass":1})
    for i in s:
        x.append(i)
    name_check=x[0]['pass']
    if name_check==name.get():

        global database
        database=str(x[0]['name'])
        print(database)
        
        top=Toplevel()
        heading=Label(top,text="Welcome to urukul",font={"arial",35},fg="steelblue").pack()
        frame=Frame(top)
        
        b1=Button(top,text="New",command=new_entry)
        b2=Button(top,text="update",command=update_entry)
        b3=Button(top,text="delete",command=delete_entry)
        b4=Button(top,text="attendence",command=attend)
        b5=Button(top,text="show",command=show_db)
        b6=Button(top,text="more",command=more)
        b1.pack(side=LEFT)
        b2.pack(side=LEFT)
        b3.pack(side=LEFT)
        b4.pack(side=LEFT)
        b5.pack(side=LEFT)
        b6.pack(side=LEFT)
        frame.pack()
    else:
        error=Toplevel()
        head=Label(error,text="The details are wrong..!!").pack()

def sup():
    neww=Toplevel()
    lab1=Label(neww,text="NAME : ")
    lab2=Label(neww,text="SSN  : ")
    lab3=Label(neww,text="pass  : ")
    lab4=Label(neww,text="re-pass  : ")
    tname=StringVar()
    tssn=IntVar()
    tpass=StringVar()
    trepass=StringVar()
    el1=Entry(neww,textvariable=tname)
    el2=Entry(neww,textvariable=tssn)
    el3=Entry(neww,textvariable=tpass)
    el4=Entry(neww,textvariable=trepass)
    lab2.grid(row=0,sticky=E)
    el2.grid(row=0, column=1)
    lab1.grid(row=1,sticky=E)
    el1.grid(row=1, column=1)
    lab3.grid(row=2,sticky=E)
    el3.grid(row=2, column=1)
    lab4.grid(row=3,sticky=E)
    el4.grid(row=3, column=1)
    def createid():
        if tpass.get()==trepass.get():
            
            data={'name': tname.get(),'ssn': tssn.get(),'pass':tpass.get()}
            db.teacher.insert(data)
            neww.destroy()
        else:
            passerr=Toplevel()
            head=Label(passerr,text="Password does not match..!!").pack()
        
    create=Button(neww,text="create",command=createid).place(x=60,y=100)
    neww.geometry("300x300")

work=Button(main_page,text="log in",command=do_it).place(x=60,y=100)
signin=Button(main_page,text="sign up",command=sup).place(x=110,y=100)
main_page.geometry("300x300")
main_page.mainloop()

