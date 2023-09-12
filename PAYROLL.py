import sys
from tkinter import *
from tkinter import messagebox
import datetime
import pymysql
import random
import re
conn=pymysql.connect(host='localhost',user='root',password='1409')
c1=conn.cursor()

c1.execute('use payroll')
def main():
    root=Tk()
    root.geometry('250x250')
    root.title('Login')
    root.resizable(False,False)

    Operating_ID=0
    def EXCEPTION():
        root_pay_ex=Tk()
        root_pay_ex.title('Payroll Exception')
        root_pay_ex.geometry('500x500')
        root_pay_ex.resizable(False,False)

        L_ID=Label(root_pay_ex,text='ID:')
        L_ID.place(x=100,y=100)

        E_ID=Entry(root_pay_ex)
        E_ID.place(x=250,y=100)

        Month=StringVar()
        Month.set("January")

        lab_month=Label(root_pay_ex,text='Month:')
        lab_month.place(x=100,y=150)

        lab_year=Label(root_pay_ex,text='Year:')
        lab_year.place(x=100,y=200)

        E_year=Entry(root_pay_ex)
        E_year.place(x=250,y=200)

        drop=OptionMenu(root_pay_ex,Month,"January","February","March","April","May","June","July","August","September","October","November","December")
        drop.place(x=250,y=150)
        def pay_process_EX(ID,MONTH,YEAR):
            def input_timesheet(ID,MONTH,YEAR):
                s='select * from TIMESHEET where MONTH="%s" and year=%s and id=%s and STATUS_AD="%s" '%(MONTH,YEAR,ID,'ACCEPTED')
                c1.execute(s)
                p=c1.fetchall()
                a='select * from emp where id=%s'%(ID)
                c1.execute(a)
                g=c1.fetchall()
                calc_fetch(g,p,MONTH,YEAR)       
            def taxation(Basic):
                sal=Basic*12
                if sal<=250000:
                    tax=0
                    return tax/12
                elif sal>=250001 and sal<=500000:
                    tax=sal*0.05
                    return tax/12
                elif sal>=500001 and sal<=750000:
                    tax=12500+(sal-500000)*0.1
                    return tax/12
                elif sal>=750001 and sal<=1000000:
                    tax=37500+(sal-750000)*0.15
                    return tax/12
                elif sal>=1000001 and sal<=1250000:
                    tax=75000+(sal-1000000)*0.2
                    return tax/12
                elif sal>=1250001 and sal<=1500000:
                    tax=12500+(sal-1250000)*0.25
                    return tax/12
                elif sal>1500000:
                    tax=187500+(sal-1500000)*0.3
                    return tax/12
            def pay_emp(Basic,HRA,SA,PF,CLUB,DAYS):
                def month_div():
                    date=datetime.datetime.now()
                    month=date.strftime('%B')
                    month=str(month)
                    year=date.strftime('%Y')
                    year=int(year)
                    month=month.upper()
                    L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
                    L2=[31,29,31,30,31,30,31,31,30,31,30,31]
                    L3=[31,28,31,30,31,30,31,31,30,31,30,31]
                    if year==2021:
                        for i in range(len(L)):
                            if L[i]==month:
                                return L3[i]
                    elif year==2020:
                        for i in range(len(L)):
                            if L[i]==month:
                                return L2[i]
                def month_now():
                    date=datetime.datetime.now()
                    month=date.strftime('%B')
                    month=str(month)
                    year=date.strftime('%Y')
                    year=int(year)
                    month=month.upper()
                    L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
                    if year==2020:
                        L2=[23,20,22,22,21,22,23,21,22,22,21,23]
                        for i in range(len(L)):
                            if L[i]==month:
                                return L2[i]
                    elif year==2021:
                        L2=[21,20,23,22,21,22,22,22,22,21,22,23]
                        for i in range(len(L)):
                            if L[i]==month:
                                return L2[i]
                Mand_days=month_now()
                Div=month_div()
                D_basic=Basic/Div
                if DAYS<Mand_days:
                    D_not_worked=Mand_days-DAYS
                    SUB=D_basic*D_not_worked
                    S_basic=Basic-SUB
                    HRA=0.4*S_basic
                    SA=0.5*S_basic
                    tax_basic=S_basic+HRA+SA
                    tax=taxation(tax_basic)
                    total=S_basic+HRA+SA-PF-tax-CLUB
                    return [tax,total]
                elif DAYS>Mand_days:
                    D_extra=DAYS-Mand_days
                    ADD=D_basic*D_extra
                    S_basic=Basic+ADD
                    HRA=0.4*S_basic
                    SA=0.5*S_basic
                    tax_basic=S_basic+HRA+SA
                    tax=taxation(tax_basic)
                    total=S_basic+HRA+SA-PF-tax-CLUB
                    return [tax,total]
                elif DAYS==Mand_days:
                    S_basic=Basic
                    HRA=0.4*S_basic
                    SA=0.5*S_basic
                    tax_basic=S_basic+HRA+SA
                    tax=taxation(tax_basic)
                    total=S_basic+HRA+SA-PF-tax-CLUB
                    return [tax,total]
            def pay_contract(DR,CLUB,DAYS):
                def month_div():
                    date=datetime.datetime.now()
                    month=date.strftime('%B')
                    month=str(month)
                    year=date.strftime('%Y')
                    year=int(year)
                    month=month.upper()
                    L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
                    L2=[31,29,31,30,31,30,31,31,30,31,30,31]
                    L3=[31,28,31,30,31,30,31,31,30,31,30,31]
                    if year==2021:
                        for i in range(len(L)):
                            if L[i]==month:
                                return L3[i]
                    elif year==2020:
                        for i in range(len(L)):
                            if L[i]==month:

                                return L2[i]
                def month_now():
                    date=datetime.datetime.now()
                    month=date.strftime('%B')
                    month=str(month)
                    year=date.strftime('%Y')
                    year=int(year)
                    month=month.upper()
                    L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
                    if year==2020:
                        L2=[23,20,22,22,21,22,23,21,22,22,21,23]
                        for i in range(len(L)):
                            if L[i]==month:
                                return L2[i]
                    elif year==2021:
                        L2=[21,20,23,22,21,22,22,22,22,21,22,23]
                        for i in range(len(L)):
                            if L[i]==month:
                                return L2[i]
                Mand_days=month_now()
                Div=month_div()

                if DAYS>Mand_days:
                    E_days=DAYS-Mand_days
                    E_pay=500*E_days # 500 units of bonus for overtime            
                    net_pay=DR*Mand_days+E_pay-CLUB
                    return net_pay
                else:
                    net_pay=DR*DAYS-CLUB
                    return net_pay
            def calc_fetch(record,record_time,month,year):
                record=record[0]
                record_time=record_time[0]
                ID=record[0]
                Basic=record[8]
                HRA=record[9]
                SA=record[10]
                PF=record[11]
                CLUB=record[12]
                DR=record[14]
                TYPE=record[17]
                TYPE=TYPE.upper()
                No_days=record_time[1]
                if TYPE=='CONTRACT':
                    L=pay_contract(DR,CLUB,No_days)
                    payslip_contract(ID,L,month,year)
                elif TYPE=='PERMANENT':
                    L=pay_emp(Basic,HRA,SA,PF,CLUB,No_days)
                    net_pay=L[1]
                    tax=L[0]
                    payslip_emp(ID,net_pay,tax,month,year)
            def payslip_emp(ID,netpay,tax,month,year):
                s='insert into payslip values(%s,%s,%s,"%s",%s,NULL)'%(ID,netpay,tax,month,year)
                c1.execute(s)
                conn.commit()
            def payslip_contract(ID,net,month,year):
                s='insert into payslip values(%s,%s,NULL,"%s",%s,NULL)'%(ID,net,month,year)
                c1.execute(s)
                conn.commit()
            input_timesheet(ID,MONTH,YEAR)

        def time_sheet(ID,Month,Year):
            def timesheet(ID,IO_REF,MONTH,YEAR):
                root_ts=Tk()
                root_ts.title('timesheet')
                root_ts.geometry('500x500')
                root_ts.resizable(False,False)

                lab_nodays=Label(root_ts,text='Number of days worked:')
                lab_nodays.place(x=100,y=50)

                e_nodays=Entry(root_ts)
                e_nodays.place(x=250,y=50)

                b_button=Button(root_ts,text='Submit',command=lambda:[date(ID,IO_REF,e_nodays.get(),MONTH,YEAR)])
                b_button.place(x=175,y=130)

                b_back=Button(root_ts,text='Back',command=lambda:[root_ts.destroy(),admin()])
                b_back.place(x=250,y=130)

                def date(ID,IO_REF,NO_DAYS,MONTH,YEAR):
                    now=datetime.datetime.now()
                    year=now.strftime('%Y')
                    year=int(year)
                    month_no=now.strftime('%m')
                    month_no=int(month_no)
                    month=now.strftime('%B')
                    day=now.strftime('%d')
                    day=int(day)

                    L=[1,2,3,4,5,6,7,8,9,10,11,12]
                    L2=[31,28,31,30,31,30,31,31,30,31,30,31]
                    for i in range(len(L)):
                        if L[i]==month_no:
                            if L2[i]==day:
                                check_day(ID,IO_REF,NO_DAYS,MONTH,YEAR,L2[i])
                            else:
                                check_day(ID,IO_REF,NO_DAYS,MONTH,YEAR,L2[i])
                def add_time(ID,IO_REF,NO_DAYS,MONTH,YEAR):
                    s='insert into timesheet(ID,NO_DAYS,IO_REF_CODE,MONTH,YEAR,STATUS_AD) values(%s,%s,%s,"%s",%s,"ACCEPTED")'%(ID,NO_DAYS,IO_REF,MONTH,YEAR)
                    c1.execute(s)
                    conn.commit()
                    respone=messagebox.showinfo('Done','Timesheet added.')
                    pay_process_EX(ID,MONTH,YEAR)
                    respone=messagebox.showinfo('Done','Payslip Generated.')
                    root_ts.destroy()
                    admin()
                    

                def check_day(ID,IO_REF,NO_DAYS,MONTH,YEAR,MAX):
                    NO_DAYS=int(NO_DAYS)
                    p=type(NO_DAYS)
                    if p==int:
                        if NO_DAYS<=0:
                            response=messagebox.showerror('Error','Invalid input')
                        elif NO_DAYS>MAX:
                            response=messagebox.showerror('Error','Invalid input')
                        else:
                            verify_run(ID,IO_REF,NO_DAYS,MONTH,YEAR)
                    else:
                        response=messagebox.showerror('Error','Invalid input')

                def verify_run(ID,IO_REF,NO_DAYS,MONTH,YEAR):
                    s='select * from timesheet where month="%s" and year=%s and ID="%s" '%(MONTH,YEAR,ID)
                    a=c1.execute(s)
                    k=c1.fetchall()
                    if a==0:
                        add_time(ID,IO_REF,NO_DAYS,MONTH,YEAR)
                    else:
                        d='delete from timesheet where month="%s" and year=%s and ID="%s"'%(MONTH,YEAR,ID)
                        c1.execute(d)
                        add_time(ID,IO_REF,NO_DAYS,MONTH,YEAR)
            def IO_ref_get(ID,MONTH,YEAR):
                s='select IO_REF_CODE from emp where id="%s"'%(ID)
                c1.execute(s)
                p=c1.fetchall()
                IO=p[0][0]
                timesheet(ID,IO,MONTH,YEAR)
            IO_ref_get(ID,Month,Year)

        def check_emp(ID,month,year):
            if len(year)==0:
                response=messagebox.showerror('Error','You left the year field empty.')
            elif len(ID)==0:
                response=messagebox.showerror('Error','You left the ID field empty.')
            else:
                if ID.isdigit() and year.isdigit():
                    global Operating_ID
                    if ID==Operating_ID:
                        response=messagebox.showinfo('Not Allowed.',"Cannot generate exception payslip for self. Please contact another administartor.")
                    else:
                        s='select id from emp'
                        c1.execute(s)
                        k=c1.fetchall()
                        for i in k:
                            r=i[0]
                            r=int(r)
                            if r==int(ID):
                                check(ID,month,year)
                                break
                        else:
                            response=messagebox.showinfo('Not Found',"The entered employee doesn't exist.")
                else:
                    response=messagebox.showerror('Error',"Invalid input.")
        def check(ID,month,year):
            def check_joining(ID,month,year):
                s='select DOJ from emp where id=%s'%(ID)
                c1.execute(s)
                k=c1.fetchall()
                l=k[0][0]
                year_chk=l.strftime('%Y')
                year_chk=int(year_chk)
                month_chk=l.strftime('%m')
                month_chk=int(month_chk)
                year=int(year)
                date_tod=datetime.datetime.now()
                mon_now=date_tod.strftime('%m')
                mon_now=int(mon_now)
                year_n=date_tod.strftime('%Y')
                year_n=int(year_n)
                L1=["January","February","March","April","May","June","July","August","September","October","November","December"]
                L2=[1,2,3,4,5,6,7,8,9,10,11,12]
                for i in range(len(L1)):
                    k=L1[i]
                    k=k.lower()
                    h=month.lower()
                    if h==k:
                        month_ent=L2[i]
                        break
                if year==year_chk:
                    if month_ent<=month_chk:
                        return False
                    elif month_ent>=mon_now:
                        return 'gst'
                    else:
                        return True
                elif year>year_chk:
                    if month_ent<month_chk:
                        return True
                    elif month_ent>=mon_now:
                        return 'gst'
                    else:
                        return True                    
                elif year>year_n:
                    return 'asd'
                else:
                    return False
            t='select id from payslip where month="%s" and year="%s" '%(month,year)
            c1.execute(t)
            l=c1.fetchall()
            join=check_joining(ID,month,year)
            if  join==False:
                response=messagebox.showerror('Error',"Can't generate payslip for date before joining.")
            elif join=='gst':
                response=messagebox.showerror('Error',"Can't generate payslip for future months.")
            elif join=='asd':
                response=messagebox.showerror('Error',"Can't generate payslip for next year.")
            else:
                for i in l:
                    j=i[0]
                    j=int(j)
                    if j==int(ID):
                        response=messagebox.showerror('Error','Payslip already generated.')
                        break
                else:
                    root_pay_ex.destroy()
                    time_sheet(ID,month,year)
        b_submit=Button(root_pay_ex,text='Submit',command=lambda:[check_emp(E_ID.get(),Month.get(),E_year.get())])
        b_submit.place(x=150,y=300)

        b_back=Button(root_pay_ex,text='Back',command=lambda:[root_pay_ex.destroy(),admin()],padx=5)
        b_back.place(x=250,y=300)
        mainloop()

    def update():
        def submit_query():
            root_update=Tk()
            root_update.geometry('500x200')
            root_update.title('Update')
            root_update.resizable(False,False)
            def clicked():
                def chk_type(str1):
                    if len(str1)==0:
                        response=messagebox.showerror('Error','You left a field empty.')
                        return False
                    elif str1.isdigit():
                        return int(str1)
                    else:
                        response=messagebox.showerror('Error','Invalid Input.')
                        return False
                p=e_ask.get()
                p=chk_type(p)
                global Operating_ID
                if p==False:
                    pass
                elif int(p)==int(Operating_ID):
                    response=messagebox.showerror('Error','Cannot update self. Please contact another admin.')
                    pass
                else:
                    s='select * from emp where id = %s'%(p)
                    t=c1.execute(s)
                    q=c1.fetchall()  
                    if t==0:
                        respones=messagebox.showerror('Error','No employee found.')
                    else:
                        b=q[0]
                        s='select type from emp where id=%s'%(p)
                        c1.execute(s)
                        t=c1.fetchall()
                        r=t[0][0]
                        r=r.upper()
                        if r=='PERMANENT':
                            root_update.destroy()
                            update_emp(b,p)
                        elif r=='CONTRACT':
                            root_update.destroy()
                            update_contract(b,p)
            lab_ask=Label(root_update,text='Enter employee id of employee you want to update:')
            lab_ask.place(x=40,y=50)

            e_ask=Entry(root_update)
            e_ask.place(x=320,y=50)

            b_but=Button(root_update,text='Submit',command=clicked)
            b_but.place(x=175,y=100)

            b_back=Button(root_update,text='Back',command=lambda:[root_update.destroy(),admin()])
            b_back.place(x=275,y=100)

        def update_contract(record,empid):
            def type_chk(a):
                for i in a:
                    if a.isdigit():
                        pass
                    else:
                        return False
                else:
                    return True
            def type_chk_list(L):
                for i in L:
                    chk=type_chk(i)
                    if chk==True:
                        pass
                    elif chk==False:
                        response=messagebox.showerror('Error','Incorrect input')
                        return False
                else:
                    return True
            
            def chk_acc(Acc,O_acc):
                s='select Acc_no from emp'
                c1.execute(s)
                p=c1.fetchall()
                k=str(Acc)
                LENGTH_acc=len(Acc)
                g=k[0]
                if int(g)==0:
                    response=messagebox.showerror('Error','Incorrect input for Acccount.')
                    return False
                else:
                    for i in Acc:
                        if i .isdigit():
                            pass
                        else:
                            response=messagebox.showerror('Error','Incorrect input for Acccount.')
                            return False
                    else:
                        if Acc==O_acc:
                            if LENGTH_acc==12:
                                return True
                            else:
                                if len(Acc)<12:
                                    response=messagebox.showerror('Error','Acccount number cannot be less than 12 digits.')
                                    return False                        
                        for i in p:
                            r=i[0]
                            if r==O_acc:
                                pass
                            elif r==k:
                                response=messagebox.showerror('Error','Account entered already exists.')
                                return False
                        else:
                            if LENGTH_acc==12:
                                return True
                            else:
                                if len(Acc)<12:
                                    response=messagebox.showerror('Error','Acccount number cannot be less than 12 digits.')
                                    return False
            root_add_emp=Tk()
            root_add_emp.geometry('950x600')
            root_add_emp.title('Update Employee')
            root_add_emp.resizable(False,False)

            R_1=StringVar()
            R_2=StringVar()

            Radiobutton(root_add_emp,text='Admin',variable=R_1,value='ADMIN').place(x=150,y=200)
            Radiobutton(root_add_emp,text='General',variable=R_1,value='EMPLOYEE').place(x=250,y=200)

            Radiobutton(root_add_emp,text='Active',variable=R_2,value='ACTIVE').place(x=750,y=200)
            Radiobutton(root_add_emp,text='Inactive',variable=R_2,value='INACTIVE').place(x=850,y=200)
            
            DES=StringVar()
            DES.set(record[13])

            DEPT=IntVar()
            DEPT.set(record[4])
            
            label=Label(root_add_emp,text='Please enter the following details to update the employee.').place(x=300,y=20)

            lab_Empid=Label(root_add_emp,text='Employee ID:')
            lab_Empid.place(x=50,y=100)
            
            lab_Fname=Label(root_add_emp,text='First name:')
            lab_Fname.place(x=350,y=100)

            lab_Lname=Label(root_add_emp,text='Last name:')
            lab_Lname.place(x=650,y=100)

            lab_Address=Label(root_add_emp,text='Address:')
            lab_Address.place(x=50,y=150)

            lab_Dept_id=Label(root_add_emp,text='Department ID:')
            lab_Dept_id.place(x=350,y=150)

            lab_IO_ref_code=Label(root_add_emp,text='IO reference code:')
            lab_IO_ref_code.place(x=650,y=150)

            lab_Acc=Label(root_add_emp,text='Account number:')
            lab_Acc.place(x=500,y=350)

            lab_Bank=Label(root_add_emp,text='Bank:').place(x=250,y=350)

            lab_Daily=Label(root_add_emp,text='Daily rate:')
            lab_Daily.place(x=250,y=400)

            lab_Club=Label(root_add_emp,text='Club Contribution:')
            lab_Club.place(x=500,y=400)

            lab_Des=Label(root_add_emp,text='Designation:')
            lab_Des.place(x=350,y=200)

            lab_RIGHTS=Label(root_add_emp,text='Rights:')
            lab_RIGHTS.place(x=50,y=200)

            lab_Status=Label(root_add_emp,text='Status:')
            lab_Status.place(x=650,y=200)

            lab_Show_ID=Label(root_add_emp,text=empid)
            lab_Show_ID.place(x=150,y=100)

            lab_SHOW_BANK=Label(root_add_emp,text=record[7])
            lab_SHOW_BANK.place(x=350,y=350)

            e_Fname=Entry(root_add_emp)
            e_Fname.place(x=450,y=100)
            e_Fname.insert(0,record[1])

            e_Lname=Entry(root_add_emp)
            e_Lname.place(x=750,y=100)
            e_Lname.insert(0,record[2])

            e_Address=Entry(root_add_emp)
            e_Address.place(x=150,y=150)
            e_Address.insert(0,record[3])

            Drop_DeptID=OptionMenu(root_add_emp,DEPT,101,102,103)
            Drop_DeptID.place(x=450,y=150)

            e_IO_ref=Entry(root_add_emp)
            e_IO_ref.place(x=750,y=150)
            e_IO_ref.insert(0,record[5])

            e_Acc_no=Entry(root_add_emp)
            e_Acc_no.place(x=620,y=350)
            e_Acc_no.insert(0,record[6])

            e_DR=Entry(root_add_emp)
            e_DR.place(x=350,y=400)
            e_DR.insert(0,record[14])

            e_CLUB=Entry(root_add_emp)
            e_CLUB.place(x=620,y=400)
            e_CLUB.insert(0,record[12])

            Drop_DES=OptionMenu(root_add_emp,DES,"CEO","CFO","Sr Project Manager","Project Manager","Associate VP","VP","CIO")
            Drop_DES.place(x=450,y=200)        
            def sumbit(ID,record):
                def check_IO_ref_new(f):
                    t=c1.execute('select ID from emp')
                    r=c1.fetchall()
                    check=0
                    for i in r:
                        if int(f) in i:
                            return True
                    else:
                        return False      

                qu=c1.execute('select ID from emp')
                t=c1.fetchall()
                a=ID
                b=e_Fname.get()
                c=e_Lname.get()
                d=e_Address.get()
                e=DEPT.get()# DEPARTMENT
                f=e_IO_ref.get()
                g=e_Acc_no.get()
                h='HDFC Bank'
                i=e_DR.get()
                m=e_CLUB.get()
                n=DES.get()# DESIGNATION
                o=record[15]#DOJ
                s=record[18]# PASSWORD
                u=R_1.get()#  RIGHTS
                Status=R_2.get()#   STATUS
                L=[b,c,d,f,g,h,i,m]
                L1=[b,c,d,f,g,h,i,m]
                L2=[20,20,50,5,12,25,5,4]
                L_S=[m,i,f]
                ty=type_chk_list(L_S)
                for v in L:
                    if len(v)==0:
                        response=messagebox.showerror('Error','You left one of the fields empty.')
                        break
                else:
                    if ty==True:
                        check_id=int(a)
                        check_IO=int(f)
                        for tup in t:
                            if check_id in tup:
                                pass
                        else:
                            check_io_ref=check_IO_ref_new(f)
                            if check_io_ref==False:
                                response=messagebox.showerror('Error',"Entered IO refer code doesn't exist")
                            else:
                                L3=[f,g,i,m]
                                check=0
                                for v in L3:
                                    if check==0:
                                        for char in v:
                                            if char.isdigit():
                                                continue
                                            else:
                                                response_add=messagebox.showerror('Error','Incorrect input.')
                                                check=1
                                                break
                                    else:
                                        break
                                else:
                                    for v in range(len(L1)):
                                        a=len(L1[v])
                                        if a>L2[v]:
                                            response_add=messagebox.showerror('Error','Data entered in one of the fields exceeds limit.')
                                            break
                                    else:
                                        chks=chk_acc(g,record[6])
                                        if chks==False:
                                            pass
                                        else:
                                            u=u.upper()
                                            if a==e:
                                                response_add=messagebox.showerror('Error','ID and IO refer code cannot be same.')
                                            elif u=='' or Status=='':
                                                response=messagebox.showerror('Error','You have not selected a radiobutton.')
                                            else:
                                                a=ID
                                                b=e_Fname.get()
                                                c=e_Lname.get()
                                                d=e_Address.get()
                                                e=DEPT.get()
                                                f=e_IO_ref.get()
                                                g=e_Acc_no.get()
                                                h='HDFC Bank'
                                                i=e_DR.get()
                                                m=e_CLUB.get()
                                                n=DES.get()
                                                o=record[15]#DOJ
                                                s=record[18]# PASSWORD
                                                u=R_1.get()#  RIGHTS
                                                Status=R_2.get()#   STATUS
                                                a=int(a)
                                                e=int(e)
                                                f=int(f)
                                                g=str(g)
                                                i=int(i)
                                                m=int(m)
                                                del_id=int(a)
                                                delete='delete from emp where id=%s'%(del_id)
                                                c1.execute(delete)
                                                insert='insert into emp VALUES(%s,"%s","%s","%s",%s,%s,"%s","HDFC Bank",NULL,NULL,NULL,NULL,%s,"%s",%s,"%s",NULL,"CONTRACT","%s","%s","%s")'%(a,b,c,d,e,f,g,m,n,i,o,s,u,Status)
                                                c1.execute(insert)
                                                conn.commit()
                                                response=messagebox.showinfo('Done','Employee updated.')
                                                root_add_emp.destroy()
                                                admin()
            b_submit=Button(root_add_emp,text='Sumbit',command=lambda:[sumbit(empid,record)])
            b_submit.place(x=375,y=275)

            b_end=Button(root_add_emp,text='Back',command=lambda:[root_add_emp.destroy(),admin()],padx=10)
            b_end.place(x=500,y=275)
                
            mainloop()
        
        def update_emp(record,p):
            def chk_acc(Acc,PF, O_acc,O_PF):
                s='select Acc_no,PF_acc from emp'
                c1.execute(s)
                p=c1.fetchall()
                k=str(Acc)
                m=str(PF)
                LENGTH_acc=len(Acc)
                LENGTH_PF=len(PF)
                g=k[0]
                t=m[0]
                if int(g)==0:
                    response=messagebox.showerror('Error','Incorrect input for Account')
                    return False
                elif int(t)==0:
                    response=messagebox.showerror('Error','Incorrect input for PF Account')
                    return False
                else:
                    for i in Acc:
                        if i.isdigit() :
                            pass
                        else:
                            response=messagebox.showerror('Error','Incorrect input for Account')
                            return False
                    else:
                        for j in PF:
                            if j.isdigit():
                                pass
                            else:
                                response=messagebox.showerror('Error','Incorrect input for PF Account')
                                return False
                        else:
                            if O_acc==Acc and O_PF==PF:
                                if LENGTH_acc==12 and LENGTH_PF==12:
                                    return True
                                else:
                                    if len(Acc)<12:
                                        response=messagebox.showerror('Error','Acccount number cannot be less than 12 digits.')
                                        return False
                                    elif len(PF)<12:
                                        response=messagebox.showerror('Error','PF Acccount cannot be less than 12 digits.')
                                        return False
                            else:                   
                                for i in p:
                                    r=i[0]
                                    t=i[1]
                                    if r==O_acc:
                                        pass
                                    elif t==O_PF:
                                        pass
                                    elif r==k:
                                        response=messagebox.showerror('Error','Account entered already exists.')
                                        return False
                                    elif m==t:
                                        response=messagebox.showerror('Error','PF Account entered already exists.')
                                        return False
                                else:
                                    if LENGTH_acc==12 and LENGTH_PF==12:
                                        return True
                                    elif Acc==PF:
                                        response=messagebox.showerror('Error','Account and PF account number are same.')
                                        return False
                                    else:
                                        if len(Acc)<12:
                                            response=messagebox.showerror('Error','Acccount number cannot be less than 12 digits.')
                                            return False
                                        elif len(PF)<12:
                                            response=messagebox.showerror('Error','PF Acccount cannot be less than 12 digits.')
                                            return False
            root_add_emp=Tk()
            root_add_emp.geometry('950x500')
            root_add_emp.title('Update Employee:')
            root_add_emp.resizable(False,False)

            R_1=StringVar()
            R_2=StringVar()

            Radiobutton(root_add_emp,text='Admin',variable=R_1,value='ADMIN').place(x=150,y=200)
            Radiobutton(root_add_emp,text='General',variable=R_1,value='EMPLOYEE').place(x=250,y=200)

            Radiobutton(root_add_emp,text='Active',variable=R_2,value='ACTIVE').place(x=750,y=200)
            Radiobutton(root_add_emp,text='Inactive',variable=R_2,value='INACTIVE').place(x=850,y=200)
            
            DES=StringVar()
            DES.set(record[13])

            DEPT=IntVar()
            DEPT.set(record[4])
            
            label=Label(root_add_emp,text='Please enter the following details to update an employee.')
            label.place(x=325,y=20)

            lab_Empid=Label(root_add_emp,text='Employee ID:')
            lab_Empid.place(x=50,y=100)

            lab_Fname=Label(root_add_emp,text='First name:')
            lab_Fname.place(x=350,y=100)

            lab_Lname=Label(root_add_emp,text='Last name:')
            lab_Lname.place(x=650,y=100)

            lab_Address=Label(root_add_emp,text='Address:')
            lab_Address.place(x=50,y=150)

            lab_Dept_id=Label(root_add_emp,text='Department ID:')
            lab_Dept_id.place(x=350,y=150)

            lab_IO_ref_code=Label(root_add_emp,text='IO reference code:')
            lab_IO_ref_code.place(x=650,y=150)

            lab_Acc=Label(root_add_emp,text='Account number:')
            lab_Acc.place(x=150,y=350)

            lab_Basic=Label(root_add_emp,text='Basic salary:')
            lab_Basic.place(x=50,y=400)


            lab_PF=Label(root_add_emp,text='Provident Fund:')
            lab_PF.place(x=350,y=400)

            lab_Club=Label(root_add_emp,text='Club Contribution:')
            lab_Club.place(x=650,y=400)

            lab_Des=Label(root_add_emp,text='Designation:')
            lab_Des.place(x=350,y=200)

            lab_RIGHTS=Label(root_add_emp,text='Rights:')
            lab_RIGHTS.place(x=50,y=200)

            lab_PF_Acc=Label(root_add_emp,text='PF Account Number:')
            lab_PF_Acc.place(x=500,y=350)

            lab_Status=Label(root_add_emp,text='Status:')
            lab_Status.place(x=650,y=200)
            
            lab_Show_ID=Label(root_add_emp,text=p)
            lab_Show_ID.place(x=150,y=100)

            e_Fname=Entry(root_add_emp)
            e_Fname.place(x=450,y=100)
            e_Fname.insert(0,record[1])

            e_Lname=Entry(root_add_emp)
            e_Lname.place(x=750,y=100)
            e_Lname.insert(0,record[2])

            e_Address=Entry(root_add_emp)
            e_Address.place(x=150,y=150)
            e_Address.insert(0,record[3])

            Drop_DeptID=OptionMenu(root_add_emp,DEPT,101,102,103)
            Drop_DeptID.place(x=450,y=150)

            e_IO_ref=Entry(root_add_emp)
            e_IO_ref.place(x=750,y=150)
            e_IO_ref.insert(0,record[5])

            e_Acc_no=Entry(root_add_emp)
            e_Acc_no.place(x=275,y=350)
            e_Acc_no.insert(0,record[6])

            lab_bank_show=Label(root_add_emp,text=record[7])
            lab_bank_show.place(x=500,y=400)

            e_Basic=Entry(root_add_emp)
            e_Basic.place(x=150,y=400)
            e_Basic.insert(0,record[8])
            
            e_HRA=Entry(root_add_emp)
            e_HRA.place(x=500,y=500)
            e_HRA.insert(0,record[9])

            e_SA=Entry(root_add_emp)
            e_SA.place(x=500,y=550)
            e_SA.insert(0,record[10])

            e_PF=Entry(root_add_emp)
            e_PF.place(x=450,y=400)
            e_PF.insert(0,record[11])

            e_CLUB=Entry(root_add_emp)
            e_CLUB.place(x=760,y=400)
            e_CLUB.insert(0,record[12])

            Drop_DES=OptionMenu(root_add_emp,DES,"CEO","CFO","Sr Project Manager","Project Manager","Associate VP","VP","CIO")
            Drop_DES.place(x=450,y=200)

            e_PF_ACC=Entry(root_add_emp)
            e_PF_ACC.place(x=625,y=350)
            e_PF_ACC.insert(0,record[16])
            
            e_RIGHTS=Entry(root_add_emp)
            e_RIGHTS.place(x=500,y=900)
            e_RIGHTS.insert(0,record[19])

            e_STATUS=Entry(root_add_emp)
            e_STATUS.place(x=600,y=900)
            e_STATUS.insert(0,record[20])
            def sumbit(a,record):
                def check_IO_ref_new(f):
                    t=c1.execute('select ID from emp')
                    r=c1.fetchall()
                    check=0
                    for i in r:
                        if int(f) in i:
                            return True
                    else:
                        return False      
                qu=c1.execute('select ID from emp')
                t=c1.fetchall()
                a=str(a)
                ID=str(a)
                b=e_Fname.get()
                c=e_Lname.get()
                d=e_Address.get()
                e=DEPT.get()
                e=str(e)
                f=e_IO_ref.get()
                g=e_Acc_no.get()
                h='HDFC Bank'
                i=e_Basic.get()
                l=e_PF.get()
                m=e_CLUB.get()
                n=DES.get()
                o=record[15] #DOJ
                p=e_PF_ACC.get()
                s=record[18] #Password
                Rights=R_1.get()
                status=R_2.get()
                L=[a,b,c,d,f,g,h,i,l,m,p,s]
                def len_chk(L):
                    for i in L:
                        if len(i)==0:
                            return False
                    else:
                        return True
                def type_chk(a):
                    for i in a:
                        if a.isdigit():
                            pass
                        else:
                            return False
                    else:
                        return True
                def type_chk_list(L):
                    for i in L:
                        chk=type_chk(i)
                        if chk==True:
                            pass
                        elif chk==False:
                            response=messagebox.showerror('Error','Incorrect input')
                            return False
                    else:
                        return True

                
                length=len_chk(L)
                L_S=[i,f]
                chk_tpe=type_chk_list(L_S)
                if length==False:
                    response=messagebox.showerror('Error','You left one of the fields empty.')
                elif chk_tpe==False:
                    pass
                else:
                    j=0.4*int(i)
                    j=int(j)
                    j=str(j) # HRA
                    k=0.5*int(i)
                    k=int(k)
                    k=str(k) # SA

                    L=[a,b,c,d,e,f,g,h,i,j,k,l,m,o,p,s]
                    L1=[a,b,c,d,e,f,g,i,j,k,l,m,n,p,s]
                    L2=[5,20,20,50,3,5,12,10,10,10,10,4,20,12,15]
                    RIGHTS=['ADMIN','EMPLOYEE']
                    for v in L:
                        if len(i)==0:
                            response=messagebox.showerror('Error','You left one of the fields empty.')
                            break
                    else:
                        check_id=int(a)
                        check_IO=int(f)
                        for tup in t:
                            if check_id in tup:
                                pass
                        else:
                            check_io_ref=check_IO_ref_new(f)
                            if check_io_ref==False:
                                response=messagebox.showerror('Error',"Entered IO refer code doesn't exist")
                            else:
                                L3=[a,e,f,g,i,j,k,l,m,p]
                                check=0
                                for v in L3:
                                    if check==0:
                                        for char in v:
                                            if char.isdigit():
                                                continue
                                            elif char=='.':
                                                continue
                                            else:
                                                response_add=messagebox.showerror('Error','Incorrect input.')
                                                check=1
                                                break
                                    else:
                                        break
                                else:
                                    for v in range(len(L1)):
                                        a=len(L1[v])
                                        if a>L2[v]:
                                            response_add=messagebox.showerror('Error','Data entered in one of the fields exceeds limit.')
                                            break
                                    else:
                                        lol=chk_acc(g,p,record[6],record[16])
                                        if a==e:
                                            response_add=messagebox.showerror('Error','ID and IO refer code cannot be same.')
                                        elif lol==False:
                                            pass
                                        elif Rights=='' or status=='':
                                            response=messagebox.showerror('Error','You have not selected a radiobutton.')
                                        else:
                                            b=e_Fname.get()
                                            c=e_Lname.get()
                                            d=e_Address.get()
                                            e=DEPT.get()
                                            f=e_IO_ref.get()
                                            g=e_Acc_no.get()
                                            h='HDFC Bank'
                                            i=e_Basic.get()
                                            l=e_PF.get()
                                            m=e_CLUB.get()
                                            n=DES.get()
                                            o=record[15]
                                            p=e_PF_ACC.get()
                                            s=record[18]  
                                            Rights=R_1.get()
                                            status=R_2.get()
                                            a=int(a)
                                            #e=int(e)
                                            f=int(f)
                                            g=str(g)
                                            i=int(i)
                                            j=int(j)
                                            k=int(k)
                                            l=int(l)
                                            m=int(m)
                                            p=str(p)
                                            del_id=int(ID)
                                            delete='delete from emp where id=%s'%(del_id)
                                            c1.execute(delete)
                                            z='insert into emp values (%s,"%s","%s","%s",%s,%s,%s,"%s",%s,%s,%s,%s,%s,"%s",NULL,"%s",%s,"PERMANENT","%s","%s","%s")'%(ID,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,s,Rights,status)
                                            c1.execute(z)
                                            conn.commit()
                                            response=messagebox.showinfo('Done','Employee updated.')
                                            root_add_emp.destroy()
                                            admin()
                
            b_sumbit=Button(root_add_emp,text='Sumbit',command=lambda:[sumbit(p,record)])
            b_sumbit.place(x=375,y=275)

            b_end=Button(root_add_emp,text='Back',command=lambda:[root_add_emp.destroy(),admin()],padx=10)
            b_end.place(x=500,y=275)
            mainloop()
            conn.commit()
        submit_query()

    def Contract(Right):
        def type_chk(a):
            for i in a:
                if a.isdigit():
                    pass
                else:
                    return False
            else:
                return True
        def type_chk_list(L):
            for i in L:
                chk=type_chk(i)
                if chk==True:
                    pass
                elif chk==False:
                    response=messagebox.showerror('Error','Incorrect input')
                    return False
            else:
                return True

        def date_check(DOJ,allow):
            if allow==True:
                try:
                    now=datetime.datetime.now()
                    date=now.strftime("%d")
                    month=now.strftime("%m")
                    year=now.strftime("%Y")
                    L=re.split('-|/',DOJ)
                    a=L[0]
                    b=L[1]
                    c=L[2]
                    a,b,c=int(a),int(b),int(c)
                    year,month,date=int(year),int(month),int(date)
                    date_entered=datetime.datetime(a,b,c)
                    date_today=datetime.datetime(year,month,date)
                    
                    Check=date_entered>=date_today
                    if Check==False:
                        return False
                    else:
                        return True
                except IndexError:
                    pass
        def date_format(DOJ):
            str1='-/'
            for i in DOJ:
                if i.isdigit():
                    pass
                elif i.isalpha():
                    response=messagebox.showerror('Error','Incorrect input.')
                    break
                else:
                    if i not in str1:
                        response=messagebox.showerror('Error','Please reconsider the seperator used in the date.Possible values include (/,-)')
                        break
            else:
                L=re.split('-|/',DOJ)
                a=L[0]
                b=L[1]
                c=L[2]
                if a=='' or b=='' or c=='':
                    response=messagebox.showerror('Error','Please follow YY/MM/DD.')
                    return False
                else:
                    s=int(a)
                    d=int(b)
                    f=int(c)
                    if s in range(1,10000) and d in range(1,13) and f in range(1,31):
                        return True
                    else:
                        response=messagebox.showerror('Error','Please follow YY/MM/DD.')
                        return False
        def check_IO_ref(f):
            t=c1.execute('select ID from emp')
            r=c1.fetchall()
            check=0
            for i in r:
                if int(f) in i:
                    return True
            else:
                return False        
        def chk_acc(Acc):
            s='select Acc_no from emp'
            c1.execute(s)
            p=c1.fetchall()
            k=str(Acc)
            LENGTH_acc=len(Acc)
            g=k[0]
            if int(g)==0:
                response=messagebox.showerror('Error','Incorrect input for Acccount.')
                return False
            else:
                if Acc.isdigit():
                    for i in p:
                        r=i[0]
                        if r==k:
                            response=messagebox.showerror('Error','Account entered already exists.')
                            return False
                    else:
                        if LENGTH_acc==12:
                            return True
                        else:
                            if len(Acc)<12:
                                response=messagebox.showerror('Error','Acccount number cannot be less than 12 digits.')
                                return False
                else:
                    response=messagebox.showerror('Error','Incorrect input for Acccount.')
                    return False
                
        def gen_id():
            s='select id from emp'
            c1.execute(s)
            p=c1.fetchall()
            while True:
                x=random.randint(10000,99999)
                for i in p:
                    l=p[0]
                    if x==l:
                        break
                    else:
                        continue
                else:
                    return x                
                    
        ID=gen_id()
        
        root_add_emp=Tk()
        root_add_emp.geometry('950x600')
        root_add_emp.title('Add Employee')
        root_add_emp.resizable(False,False)

        DES=StringVar()
        DES.set('CEO')

        DEPT=IntVar()
        DEPT.set(101)
        
        label=Label(root_add_emp,text='Please enter the following details to register an employee.').place(x=300,y=20)

        lab_Daily=Label(root_add_emp,text='Daily rate:')
        lab_Daily.place(x=250,y=400)

        lab_Empid=Label(root_add_emp,text='Employee ID:')
        lab_Empid.place(x=50,y=100)

        lab_Fname=Label(root_add_emp,text='First name:')
        lab_Fname.place(x=350,y=100)

        lab_Lname=Label(root_add_emp,text='Last name:')
        lab_Lname.place(x=650,y=100)

        lab_Address=Label(root_add_emp,text='Address:')
        lab_Address.place(x=50,y=150)

        lab_Dept_id=Label(root_add_emp,text='Department ID:')
        lab_Dept_id.place(x=350,y=150)

        lab_IO_ref_code=Label(root_add_emp,text='IO reference code:')
        lab_IO_ref_code.place(x=650,y=150)

        lab_Acc=Label(root_add_emp,text='Account number:')
        lab_Acc.place(x=350,y=350)

        lab_Club=Label(root_add_emp,text='Club Contribution:')
        lab_Club.place(x=500,y=400)

        lab_Des=Label(root_add_emp,text='Designation:')
        lab_Des.place(x=350,y=200)

        lab_DOJ=Label(root_add_emp,text='Date of joining:')
        lab_DOJ.place(x=50,y=200)

        lab_Pass=Label(root_add_emp,text='Password:')
        lab_Pass.place(x=650,y=200)

        lab_Show_ID=Label(root_add_emp,text=ID)
        lab_Show_ID.place(x=150,y=100)

        e_Fname=Entry(root_add_emp)
        e_Fname.place(x=450,y=100)

        e_Lname=Entry(root_add_emp)
        e_Lname.place(x=750,y=100)

        e_Address=Entry(root_add_emp)
        e_Address.place(x=150,y=150)

        Drop_DeptID=OptionMenu(root_add_emp,DEPT,101,102,103)
        Drop_DeptID.place(x=450,y=150)

        e_IO_ref=Entry(root_add_emp)
        e_IO_ref.place(x=750,y=150)

        e_Acc_no=Entry(root_add_emp)
        e_Acc_no.place(x=450,y=350)

        e_CLUB=Entry(root_add_emp)
        e_CLUB.place(x=620,y=400)

        Drop_DES=OptionMenu(root_add_emp,DES,"CEO","CFO","Sr Project Manager","Project Manager","Associate VP","VP","CIO")
        Drop_DES.place(x=450,y=200)

        e_DOJ=Entry(root_add_emp)
        e_DOJ.place(x=150,y=200)

        e_PASSWORD=Entry(root_add_emp)
        e_PASSWORD.place(x=750,y=200)

        e_Daily=Entry(root_add_emp)
        e_Daily.place(x=320,y=400)
        
        def sumbit(Right):
            qu=c1.execute('select ID from emp')
            t=c1.fetchall()
            a=ID
            b=e_Fname.get()
            c=e_Lname.get()
            d=e_Address.get()
            e=DEPT
            f=e_IO_ref.get()
            g=e_Acc_no.get()
            h='HDFC Bank'
            i=e_Daily.get()
            m=e_CLUB.get()
            n=DES
            o=e_DOJ.get()
            s=e_PASSWORD.get()
            u=Right
            L=[b,c,d,f,g,h,i,m,o,s,u]
            L1=[b,c,d,f,g,h,i,m,s,u]
            L2=[20,20,50,5,12,25,5,4,10,15,10,10]
            L_check=[b,c,d,f,o,s,m,i,g]
            L2_2=[20,20,50,5,10,15,4,5,12]
            RIGHTS=['ADMIN','EMPLOYEE']
            L_S=[m,i,f]
            ty=type_chk_list(L_S)
            for v in L:
                if len(v)==0:
                    response=messagebox.showerror('Error','You left one of the fields empty.')
                    break
            else:
                if ty==True:
                    check_id=int(a)
                    check_IO=int(f)
                    for tup in t:
                        if check_id in tup:
                            response=messagebox.showerror('Error','An employee with the entered id already exists.')
                            break
                        
                    else:
                        check_io_ref=check_IO_ref(f)
                        if check_io_ref==False:
                            response=messagebox.showerror('Error',"Entered IO refer code doesn't exist")
                        else:
                            L3=[f,g,i,m]
                            check=0
                            for v in L3:
                                if check==0:
                                    for char in v:
                                        if char.isdigit():
                                            continue
                                        else:
                                            response_add=messagebox.showerror('Error','Incorrect input.')
                                            check=1
                                            break
                                else:
                                    break
                            else:
                                for v in range(len(L_check)):
                                    a=len(L_check[v])
                                    if a>L2_2[v]:
                                        response_add=messagebox.showerror('Error','Data entered in one of the fields exceeds limit.')
                                        break
                                else:
                                    chks=chk_acc(g)
                                    check_date_format=date_format(o)
                                    check_date=date_check(o,check_date_format)
                                    if check_date_format==False:
                                        pass
                                    elif check_date==False:
                                        response_add=messagebox.showerror('Error','Date cannot be before today.')
                                    elif chks==False:
                                        pass
                                    else:
                                        u=u.upper()
                                        check_department=check_dept(e)
                                        if check_dept==False:
                                            response_add=messagebox.showerror('Error',"Entered Department ID doesn't exist.")
                                        elif u not in RIGHTS:
                                            response_add=messagebox.showerror('Error','Please enter a valid right.')
                                        elif a==e:
                                            response_add=messagebox.showerror('Error','ID and IO refer code cannot be same.')
                                        else:
                                            a=ID
                                            b=e_Fname.get()
                                            c=e_Lname.get()
                                            d=e_Address.get()
                                            e=DEPT.get()
                                            f=e_IO_ref.get()
                                            g=e_Acc_no.get()
                                            h='HDFC Bank'
                                            i=e_Daily.get()
                                            m=e_CLUB.get()
                                            n=DES.get()
                                            o=e_DOJ.get()
                                            s=e_PASSWORD.get()
                                            u=Right
                                            a=int(a)
                                            e=int(e)
                                            f=int(f)
                                            g=str(g)
                                            i=int(i)
                                            m=int(m)
                                            x='ACTIVE'
                                            insert='insert into emp(ID,FNAME,LNAME,ADDRESS,DEPT_ID,IO_REF_CODE,ACC_NO,BANK,CLUB_CONT,DESIGNATION,DAILY_RATE,DOJ,TYPE,PASSWORD,RIGHTS,STAUS_AT) VALUES(%s,"%s","%s","%s",%s,%s,%s,"%s",%s,"%s",%s,"%s","CONTRACT","%s","%s","INACTIVE")'%(a,b,c,d,e,f,g,h,m,n,i,o,s,u)
                                            c1.execute(insert)
                                            conn.commit()
                                            response=messagebox.showinfo('Done','Empoyee added.')
                                            root_add_emp.destroy()
                                            admin()
            
        b_sumbit=Button(root_add_emp,text='Sumbit',padx=5,command=lambda:[sumbit(Right)])
        b_sumbit.place(x=375,y=275)

        b_end=Button(root_add_emp,text='Back',padx=15,command=lambda:[root_add_emp.destroy(),admin()])
        b_end.place(x=500,y=275)
        mainloop()
    def timesheet(ID,IO_REF):
        root_ts=Tk()
        root_ts.title('timesheet')
        root_ts.geometry('500x500')
        root_ts.resizable(False,False)

        lab_month=Label(root_ts,text='Month:')
        lab_month.place(x=150,y=100)

        lab_nodays=Label(root_ts,text='Number of days worked:')
        lab_nodays.place(x=150,y=150)

        e_month=Entry(root_ts)
        e_month.place(x=250,y=100)

        e_nodays=Entry(root_ts)
        e_nodays.place(x=250,y=150)


        def add_time(ID,IO_REF,NO_DAYS,MONTH,YEAR):
            s='insert into timesheet(ID,NO_DAYS,IO_REF_CODE,MONTH,YEAR) values(%s,%s,%s,"%s",%s)'%(ID,NO_DAYS,IO_REF,MONTH,YEAR)
            c1.execute(s)
            respone=messagebox.showinfo('Done','Timesheet added.')

        def check_date(ID,IO_REF,month,no_days):
            L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
            L2=[31,28,31,30,31,30,31,31,30,31,30,31]
            month=month.upper()
            if month not in L:
                response=messagebox.showerror('Invalid','Invalid input.')
            else:
                L5=[1,2,3,4,5,6,7,8,9,10,11,12]
                for i in range(len(L)):
                    if L[i]==month:
                        month_no=L2[i]
                        break
                now=datetime.datetime.now()
                month_now=now.strftime('%m')
                month_now=int(month_now)
                year_now=now.strftime('%Y')
                L3=[month_now,month_now-1]
                if month_no not in L3:
                    response=messagebox.showerror('Invalid input',"Can't enter a month outside current and previous.")
                else:
                    day_check=month_no-1
                    max_limit=L5[day_check]
                    year_now=int(year_now)
                    for i in no_days:
                        if i.isdigit():
                            continue
                        else:
                            response=messagebox.showerror('Invald input','Invald input.')
                            break
                    else:
                        no_days=int(no_days)
                        if no_days>day_check or no_days<0:
                            response=messagebox.showerror('Invald input','Invald input.')
                        else:
                            add_time(ID,IO_REF,no_days,month,year_now)





        def verify_run(ID,IO_REF,month,no_days):
            s='select month,year from timesheet where id=%s'%(ID)
            a=c1.execute(s)
            if a==0:
                check_date(ID,IO_REF,month,no_days)
            else:
                response=messagebox.showerror('Already exists.','Already exists.')
        b=Button(root_ts,text='Submit',command=lambda:[verify_run(ID,IO_REF,e_month.get(),e_nodays.get())])
        b.place(x=250,y=200)

    def check_IO_ref(f):
        t=c1.execute('select ID from emp')
        r=c1.fetchall()
        check=0
        for i in r:
            if int(f) in i:
                return True
        else:
            return False        
    def date_check(DOJ,allow):
        if allow==True:
            try:
                now=datetime.datetime.now()
                date=now.strftime("%d")
                month=now.strftime("%m")
                year=now.strftime("%Y")
                L=re.split('-|/',DOJ)
                a=L[0]
                b=L[1]
                c=L[2]
                a,b,c=int(a),int(b),int(c)
                year,month,date=int(year),int(month),int(date)
                date_entered=datetime.datetime(a,b,c)
                date_today=datetime.datetime(year,month,date)
                
                Check=date_entered>=date_today
                if Check==False:
                    return False
                else:
                    return True
            except IndexError:
                pass
    def date_format(DOJ):
        str1='-/'
        for i in DOJ:
            if i.isdigit():
                pass
            elif i.isalpha():
                response=messagebox.showerror('Error','Incorrect input.')
                break
            else:
                if i not in str1:
                    response=messagebox.showerror('Error','Please reconsider the seperator used in the date.Possible values include (/,-)')
                    break
        else:
            L=re.split('-|/',DOJ)
            a=L[0]
            b=L[1]
            c=L[2]
            if a=='' or b=='' or c=='':
                response=messagebox.showerror('Error','Please follow YY/MM/DD.')                
            else:
                s=int(a)
                d=int(b)
                f=int(c)
                if s in range(1,10000) and d in range(1,13) and f in range(1,31):
                    return True
                else:
                    return False

    def check_dept(e):
        dept_check=c1.execute('select Dept_Id from emp')
        dept_fetch_check=c1.fetchall()
        for dept in dept_fetch_check:
            if e in dept:
                return True
                break
            else:
                continue
        else:
            return False
    def Employee(Right):
        def chk_acc(Acc,PF):
            s='select Acc_no,PF_acc from emp'
            c1.execute(s)
            p=c1.fetchall()
            k=str(Acc)
            m=str(PF)
            LENGTH_acc=len(Acc)
            LENGTH_PF=len(PF)
            g=k[0]
            t=m[0]
            if int(g)==0:
                response=messagebox.showerror('Error','Incorrect input for Account')
                return False
            elif int(t)==0:
                response=messagebox.showerror('Error','Incorrect input for PF Account')
                return False
            else:
                for i in Acc:
                    if i.isdigit() :
                        pass
                    else:
                        response=messagebox.showerror('Error','Incorrect input for Account')
                        return False
                else:
                    for j in PF:
                        if j.isdigit():
                            pass
                        else:
                            response=messagebox.showerror('Error','Incorrect input for PF Account')
                            return False

                    else:                   
                        for i in p:
                            r=i[0]
                            t=i[1]
                            if r==k:
                                response=messagebox.showerror('Error','Account entered already exists.')
                                return False
                            elif m==t:
                                response=messagebox.showerror('Error','PF Account entered already exists.')
                                return False
                        else:
                            if LENGTH_acc==12 and LENGTH_PF==12:
                                return True
                            elif Acc==PF:
                                response=messagebox.showerror('Error','Account and PF account number are same.')
                                return False
                            else:
                                if len(Acc)<12:
                                    response=messagebox.showerror('Error','Acccount number cannot be less than 12 digits.')
                                    return False
                                elif len(PF)<12:
                                    response=messagebox.showerror('Error','PF Acccount cannot be less than 12 digits.')
                                    return False
        def gen_id():
            s='select id from emp'
            c1.execute(s)
            p=c1.fetchall()
            while True:
                x=random.randint(10000,99999)
                for i in p:
                    l=p[0]
                    if x==l:
                        break
                    else:
                        continue
                else:
                    return x                
                    
        ID=gen_id()
        
        root_add_emp=Tk()
        root_add_emp.geometry('950x500')
        root_add_emp.title('Add Employee')
        root_add_emp.resizable(False,False)

        DES=StringVar()
        DES.set('CEO')

        DEPT=IntVar()
        DEPT.set(101)
        
        label=Label(root_add_emp,text='Please enter the following details to register an employee.')
        label.place(x=325,y=20)

        lab_Empid=Label(root_add_emp,text='Employee ID:')
        lab_Empid.place(x=50,y=100)

        lab_Fname=Label(root_add_emp,text='First name:')
        lab_Fname.place(x=350,y=100)

        lab_Lname=Label(root_add_emp,text='Last name:')
        lab_Lname.place(x=650,y=100)

        lab_Address=Label(root_add_emp,text='Address:')
        lab_Address.place(x=50,y=150)

        lab_Dept_id=Label(root_add_emp,text='Department ID:')
        lab_Dept_id.place(x=350,y=150)

        lab_IO_ref_code=Label(root_add_emp,text='IO reference code:')
        lab_IO_ref_code.place(x=650,y=150)

        lab_Acc=Label(root_add_emp,text='Account number:')
        lab_Acc.place(x=150,y=350)

        lab_Basic=Label(root_add_emp,text='Basic salary:')
        lab_Basic.place(x=50,y=400)


        lab_PF=Label(root_add_emp,text='Provident Fund:')
        lab_PF.place(x=350,y=400)

        lab_Club=Label(root_add_emp,text='Club Contribution:')
        lab_Club.place(x=650,y=400)

        lab_Des=Label(root_add_emp,text='Designation:')
        lab_Des.place(x=350,y=200)

        lab_DOJ=Label(root_add_emp,text='Date of joining:')
        lab_DOJ.place(x=50,y=200)

        lab_PF_Acc=Label(root_add_emp,text='PF Account Number:')
        lab_PF_Acc.place(x=500,y=350)

        lab_Pass=Label(root_add_emp,text='Password:')
        lab_Pass.place(x=650,y=200)
        
        lab_Show_ID=Label(root_add_emp,text=ID)
        lab_Show_ID.place(x=150,y=100)

        e_Fname=Entry(root_add_emp)
        e_Fname.place(x=450,y=100)

        e_Lname=Entry(root_add_emp)
        e_Lname.place(x=750,y=100)

        e_Address=Entry(root_add_emp)
        e_Address.place(x=150,y=150)

        Drop_DeptID=OptionMenu(root_add_emp,DEPT,101,102,103)
        Drop_DeptID.place(x=450,y=150)

        e_IO_ref=Entry(root_add_emp)
        e_IO_ref.place(x=750,y=150)

        e_Acc_no=Entry(root_add_emp)
        e_Acc_no.place(x=275,y=350)

        e_Basic=Entry(root_add_emp)
        e_Basic.place(x=150,y=400)

        e_PF=Entry(root_add_emp)
        e_PF.place(x=450,y=400)

        e_CLUB=Entry(root_add_emp)
        e_CLUB.place(x=760,y=400)

        Drop_DES=OptionMenu(root_add_emp,DES,"CEO","CFO","Sr Project Manager","Project Manager","Associate VP","VP","CIO")
        Drop_DES.place(x=450,y=200)

        e_DOJ=Entry(root_add_emp)
        e_DOJ.place(x=150,y=200)

        e_PF_ACC=Entry(root_add_emp)
        e_PF_ACC.place(x=625,y=350)

        e_PASSWORD=Entry(root_add_emp)
        e_PASSWORD.place(x=750,y=200)
        
        def sumbit(Right):
            qu=c1.execute('select ID from emp')
            t=c1.fetchall()
            a=str(ID)
            b=e_Fname.get()
            c=e_Lname.get()
            d=e_Address.get()
            e=DEPT.get()
            e=str(e)
            f=e_IO_ref.get()
            g=e_Acc_no.get()
            h='HDFC Bank'
            i=e_Basic.get()
            l=e_PF.get()
            m=e_CLUB.get()
            n=DES.get()
            o=e_DOJ.get()
            p=e_PF_ACC.get()
            s=e_PASSWORD.get()
            u=Right
            L=[a,b,c,d,e,f,g,h,i,l,m,n,o,p,s,u]
            def len_chk(L):
                for i in L:
                    if len(i)==0:
                        return False
                else:
                    return True
            def type_chk(a):
                for i in a:
                    if a.isdigit():
                        pass
                    else:
                        return False
                else:
                    return True
            def type_chk_list(L):
                for i in L:
                    chk=type_chk(i)
                    if chk==True:
                        pass
                    elif chk==False:
                        response=messagebox.showerror('Error','Incorrect input')
                        return False
                else:
                    return True
            length=len_chk(L)
            L_S=[i,f]
            chk_tpe=type_chk_list(L_S)
            if length==False:
                response=messagebox.showerror('Error','You left one of the fields empty.')
            elif chk_tpe==False:
                pass
            else:
                j=0.4*int(i)
                j=int(j)
                j=str(j) # HRA
                k=0.5*int(i)
                k=int(k)
                k=str(k) # SA

                L=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,s,u]
                L1=[a,b,c,d,e,f,g,i,j,k,l,m,n,p,s]
                L2=[5,20,20,50,3,5,12,10,10,10,10,4,20,12,15]
                RIGHTS=['ADMIN','EMPLOYEE']
                for v in L:
                    if len(i)==0:
                        response=messagebox.showerror('Error','You left one of the fields empty.')
                        break
                else:
                    check_id=int(a)
                    check_IO=int(f)
                    for tup in t:
                        if check_id in tup:
                            response=messagebox.showerror('Error','An employee with the entered id already exists.')
                            break
                    else:
                        check_io_ref=check_IO_ref(f)
                        if check_io_ref==False:
                            response=messagebox.showerror('Error',"Entered IO refer code doesn't exist")
                        else:
                            L3=[a,e,f,g,i,j,k,l,m,p]
                            check=0
                            for v in L3:
                                if check==0:
                                    for char in v:
                                        if char.isdigit():
                                            continue
                                        elif char=='.':
                                            continue
                                        else:
                                            response_add=messagebox.showerror('Error','Incorrect input.')
                                            check=1
                                            break
                                else:
                                    break
                            else:
                                for v in range(len(L1)):
                                    a=len(L1[v])
                                    if a>L2[v]:
                                        response_add=messagebox.showerror('Error','Data entered in one of the fields exceeds limit.')
                                        break
                                else:
                                    check_date_format=date_format(o)
                                    check_date=date_check(o,check_date_format)
                                    if check_date_format==False:
                                        response=messagebox.showerror('Error','Please follow YY/MM/DD.')
                                    elif check_date==False:
                                        response_add=messagebox.showerror('Error','Date cannot be before today.')
                                    else:
                                        u=u.upper()
                                        check_account=chk_acc(g,p)
                                        check_department=check_dept(e)
                                        if u not in RIGHTS:
                                            pass
                                        elif check_account==False:
                                            pass
                                        elif a==e:
                                            response_add=messagebox.showerror('ID and IO refer code cannot be same.')
                                        else:
                                            a=ID
                                            b=e_Fname.get()
                                            c=e_Lname.get()
                                            d=e_Address.get()
                                            e=DEPT.get()
                                            f=e_IO_ref.get()
                                            g=e_Acc_no.get()
                                            h='HDFC Bank'
                                            i=e_Basic.get()
                                            l=e_PF.get()
                                            m=e_CLUB.get()
                                            n=DES.get()
                                            o=e_DOJ.get()
                                            p=e_PF_ACC.get()
                                            s=e_PASSWORD.get()
                                            u=Right
                                            a=int(a)
                                            #e=int(e)
                                            f=int(f)
                                            g=str(g)
                                            i=int(i)
                                            j=int(j)
                                            k=int(k)
                                            l=int(l)
                                            m=int(m)
                                            p=str(p)
                                            
                                            x='ACTIVE'
                                            z='insert into emp values(%s,"%s","%s","%s",%s,%s,%s,"%s",%s,%s,%s,%s,%s,"%s",NULL,"%s",%s,"PERMANENT","%s","%s","INACTIVE")'%(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,s,u)
                                            c1.execute(z)
                                            conn.commit()
                                            response=messagebox.showinfo('Done','Empoyee added.')
                                            root_add_emp.destroy()
                                            admin()
                                            
        b_sumbit=Button(root_add_emp,text='Sumbit',padx=5,command=lambda:[sumbit(Right)])
        b_sumbit.place(x=375,y=275)

        b_end=Button(root_add_emp,text='Back',padx=15,command=lambda:[root_add_emp.destroy(),admin()])
        b_end.place(x=500,y=275)
        mainloop()
    def add():

        root_add=Tk()
        root_add.title('Add employee')
        root_add.geometry('600x400')
        root_add.resizable(False,False)

        a= IntVar()
        b=IntVar()
        def next_page(v1,v2):
            if v1==1:
                if v2==1:
                    root_add.destroy()
                    Contract('ADMIN')
                elif v2==2:
                    root_add.destroy()
                    Contract('EMPLOYEE')
            elif v1==2:
                if v2==1:
                    root_add.destroy()
                    Employee('ADMIN')
                elif v2==2:
                    root_add.destroy()
                    Employee('EMPLOYEE')
        L_type=Label(root_add,text='Employee Type:')
        L_type.place(x=50,y=75)

        L_rights=Label(root_add,text='Employee Rights:')
        L_rights.place(x=50,y=275)
        
        Radiobutton(root_add,text='Contract',variable=a,value=1).place(x=150,y=50)
        Radiobutton(root_add,text='Employee',variable=a,value=2).place(x=150,y=100)

        Radiobutton(root_add,text='Admin',variable=b,value=1).place(x=150,y=250)
        Radiobutton(root_add,text='General',variable=b,value=2).place(x=150,y=300)

    ##    Radiobutton(root_add,text='Admin',variable=b,value=1).place(150,y=250)
    ##    Radiobutton(root_add,text='General',variable=b,value=2).place(150,y=300)


        b1=Button(root_add,text='Next',command=lambda:next_page(a.get(),b.get()),padx=5)
        b1.place(x=300,y=175)

        b_back=Button(root_add,text='Back',padx=5,command=lambda:[root_add.destroy(),admin()])
        b_back.place(x=300,y=225)
        mainloop()

    def search():
        root_search=Tk()
        root_search.geometry('950x500')
        root_search.title('Search Employee')
        root_search.resizable(False,False)

        lab_input=Label(root_search,text='Please enter the ID of the employee you want to search:')
        lab_input.place(x=230,y=50)

        e_input=Entry(root_search)
        e_input.place(x=530,y=50)
        def chk_input():
            inp=e_input.get()
            for i in inp:
                if i.isdigit():
                    pass
                else:
                    response=messagebox.showerror('Error','Wrong Input.')
                    break
            else:
                if len(inp)!=5:
                    response=messagebox.showerror('Error','Invalid ID inputted.')
                else:
                    search_emp()

        def search_emp():
            a=e_input.get()
            a=int(a)
            s=('select * from emp where ID=%s')%(a)
            p=c1.execute(s)
            t=c1.fetchall()
            if p==0:
                response_add=messagebox.showinfo('Non existent','No employee found.')
            else:
                type_query=('select type from emp where ID=%s')%(a)
                p=c1.execute(type_query)
                type_fetch=c1.fetchall()
                a=type_fetch[0][0]
                chk_dpt=t[0][4]
                find='select dept from dept where dept_id=%s'%(chk_dpt)
                c1.execute(find)
                dep_fetch=c1.fetchall()
                dept_name=dep_fetch[0][0] 
                b=a.upper()
                def wid_destroy_emp():
                    head_ID.destroy()
                    head_Fname.destroy()
                    head_Lname.destroy()
                    head_Address.destroy()  
                    head_Department_id.destroy()
                    head_IO_ref.destroy()
                    head_acc.destroy()
                    head_bank.destroy()
                    head_basic.destroy()
                    head_hra.destroy()   
                    head_sa.destroy()
                    head_pf.destroy()
                    head_club.destroy()
                    head_des.destroy()
                    head_DOJ.destroy()
                    head_PF_Acc.destroy()           
                    head_Type.destroy()           
                    head_Rights.destroy()
                    head_status.destroy()
                    head_dept_name.destroy()

                    lab_ID.destroy()
                    
                    lab_Fname.destroy()
                    lab_Lname.destroy()
                    lab_Address.destroy()
                    lab_Department_id.destroy()
                    lab_IO_ref.destroy()
                    lab_acc.destroy()
                    lab_bank.destroy()
                    lab_basic.destroy()
                    lab_hra.destroy()
                    lab_sa.destroy()
                    lab_pf.destroy()
                    lab_club.destroy()
                    lab_des.destroy()
                    lab_DOJ.destroy()
                    lab_Type.destroy()
                    lab_Rights.destroy()
                    lab_status.destroy()
                    lab_PF_Acc.destroy()
                    lab_DEPT.destroy()
                def wid_destroy_contract():
                    head_ID.destroy()
                    head_Fname.destroy()
                    head_Lname.destroy()
                    head_Address.destroy()  
                    head_Department_id.destroy()
                    head_IO_ref.destroy()
                    head_acc.destroy()
                    head_bank.destroy()
                    head_club.destroy()
                    head_des.destroy()
                    head_DR.destroy()
                    head_DOJ.destroy()
                    head_Type.destroy()           
                    head_Rights.destroy()
                    head_status.destroy()
                    head_dept_name.destroy()
                    
                    lab_Fname.destroy()
                    lab_Lname.destroy()
                    lab_ID.destroy()
                    lab_Address.destroy()
                    lab_Department_id.destroy()
                    lab_IO_ref.destroy()
                    lab_acc.destroy()
                    lab_bank.destroy()
                    lab_DR.destroy()
                    lab_club.destroy()
                    lab_des.destroy()
                    lab_DOJ.destroy()
                    lab_Type.destroy()
                    lab_Rights.destroy()
                    lab_status.destroy()
                    lab_DEPT.destroy()

                if b=='PERMANENT':
                    value=t[0]

                    head_ID=Label(root_search,text='ID:')
                    head_ID.place(x=40,y=200)

                    head_Fname=Label(root_search,text='First name:')
                    head_Fname.place(x=310,y=200)
                    
                    head_Lname=Label(root_search,text='Last name:')
                    head_Lname.place(x=530,y=200)
                
                    head_Address=Label(root_search,text='Address:')
                    head_Address.place(x=740,y=200)
                    
                    head_Department_id=Label(root_search,text='Department ID:')
                    head_Department_id.place(x=40,y=250)

                    head_dept_name=Label(root_search,text='Department:')
                    head_dept_name.place(x=310,y=250)
                    
                    head_acc=Label(root_search,text='Account:')
                    head_acc.place(x=530,y=250)
                    
                    head_bank=Label(root_search,text='Bank:')
                    head_bank.place(x=740,y=250)
                    
                    head_basic=Label(root_search,text='Basic:')
                    head_basic.place(x=40,y=300)
                    
                    head_hra=Label(root_search,text='HRA:')
                    head_hra.place(x=310,y=300)
                    
                    head_sa=Label(root_search,text='SA:')
                    head_sa.place(x=530,y=300)
                    
                    head_pf=Label(root_search,text='PF:')
                    head_pf.place(x=740,y=300)
                    
                    head_club=Label(root_search,text='Club contribution:')
                    head_club.place(x=40,y=350)
                    
                    head_des=Label(root_search,text='Designation:')
                    head_des.place(x=310,y=350)
                    
                    head_DOJ=Label(root_search,text='Date of joining:')
                    head_DOJ.place(x=530,y=350)
                    
                    head_PF_Acc=Label(root_search,text='PF Account:')
                    head_PF_Acc.place(x=740,y=350)
                    
                    head_Type=Label(root_search,text='Type:')
                    head_Type.place(x=40,y=400)
                    
                    head_Rights=Label(root_search,text='Rights:')
                    head_Rights.place(x=310,y=400)
                    
                    head_status=Label(root_search,text='Status:')
                    head_status.place(x=530,y=400)
                    
                    head_IO_ref=Label(root_search,text='IO reference code:')
                    head_IO_ref.place(x=740,y=400)

                    lab_ID=Label(root_search,text=value[0])
                    lab_ID.place(x=150,y=200)

                    lab_Fname=Label(root_search,text=value[1])
                    lab_Fname.place(x=410,y=200)
                    
                    lab_Lname=Label(root_search,text=value[2])
                    lab_Lname.place(x=630,y=200)
                    
                    lab_Address=Label(root_search,text=value[3])
                    lab_Address.place(x=840,y=200)
                    
                    lab_Department_id=Label(root_search,text=value[4])
                    lab_Department_id.place(x=150,y=250)

                    lab_DEPT=Label(root_search,text=dept_name)
                    lab_DEPT.place(x=410,y=250)
                    
                    lab_acc=Label(root_search,text=value[6])
                    lab_acc.place(x=630,y=250)
                    
                    lab_bank=Label(root_search,text=value[7])
                    lab_bank.place(x=840,y=250)
                    
                    lab_basic=Label(root_search,text=value[8])
                    lab_basic.place(x=150,y=300)
                    
                    lab_hra=Label(root_search,text=value[9])
                    lab_hra.place(x=410,y=300)
                    
                    lab_sa=Label(root_search,text=value[10])
                    lab_sa.place(x=630,y=300)
                    
                    lab_pf=Label(root_search,text=value[11])
                    lab_pf.place(x=840,y=300)
                    
                    lab_club=Label(root_search,text=value[12])
                    lab_club.place(x=150,y=350)
                    
                    lab_des=Label(root_search,text=value[13])
                    lab_des.place(x=410,y=350)
                    
                    lab_DOJ=Label(root_search,text=value[15])
                    lab_DOJ.place(x=630,y=350)
                    
                    lab_PF_Acc=Label(root_search,text=value[16])
                    lab_PF_Acc.place(x=840,y=350)
                    
                    lab_Type=Label(root_search,text=value[17])
                    lab_Type.place(x=150,y=400)
                    
                    lab_Rights=Label(root_search,text=value[19])
                    lab_Rights.place(x=410,y=400)
                    
                    lab_status=Label(root_search,text=value[20])
                    lab_status.place(x=630,y=400)

                    lab_IO_ref=Label(root_search,text=value[5])
                    lab_IO_ref.place(x=840,y=400)

                    b_sumbit=Button(root_search,text='Search',command=lambda:[wid_destroy_emp(),chk_input()])
                    b_sumbit.place(x=380,y=100)
                elif b=='CONTRACT':
                    value=t[0]

                    head_ID=Label(root_search,text='ID:')
                    head_ID.place(x=40,y=200)

                    head_Fname=Label(root_search,text='First name:')
                    head_Fname.place(x=310,y=200)
                    
                    head_Lname=Label(root_search,text='Last name:')
                    head_Lname.place(x=530,y=200)
                
                    head_Address=Label(root_search,text='Address:')
                    head_Address.place(x=740,y=200)
                    
                    head_Department_id=Label(root_search,text='Department ID:')
                    head_Department_id.place(x=40,y=250)

                    head_dept_name=Label(root_search,text='Department:')
                    head_dept_name.place(x=310,y=250)
                    
                    head_acc=Label(root_search,text='Account:')
                    head_acc.place(x=530,y=250)
                    
                    head_bank=Label(root_search,text='Bank:')
                    head_bank.place(x=740,y=250)
                    
                    head_club=Label(root_search,text='Club contribution:')
                    head_club.place(x=40,y=300)
                    
                    head_des=Label(root_search,text='Designation:')
                    head_des.place(x=310,y=300)
                    
                    head_DOJ=Label(root_search,text='Date of joining:')
                    head_DOJ.place(x=530,y=300)

                    head_DR=Label(root_search,text='Daily rate:')
                    head_DR.place(x=740,y=300)
                    
                    head_Type=Label(root_search,text='Type:')
                    head_Type.place(x=40,y=350)
                    
                    head_Rights=Label(root_search,text='Rights:')
                    head_Rights.place(x=310,y=350)
                    
                    head_status=Label(root_search,text='Status:')
                    head_status.place(x=530,y=350)

                    head_IO_ref=Label(root_search,text='IO reference code:')
                    head_IO_ref.place(x=740,y=350)

                    lab_ID=Label(root_search,text=value[0])
                    lab_ID.place(x=150,y=200)

                    lab_Fname=Label(root_search,text=value[1])
                    lab_Fname.place(x=410,y=200)
                    
                    lab_Lname=Label(root_search,text=value[2])
                    lab_Lname.place(x=630,y=200)
                    
                    lab_Address=Label(root_search,text=value[3])
                    lab_Address.place(x=840,y=200)
                    
                    lab_Department_id=Label(root_search,text=value[4])
                    lab_Department_id.place(x=150,y=250)

                    lab_DEPT=Label(root_search,text=dept_name)
                    lab_DEPT.place(x=410,y=250)
                    
                    lab_acc=Label(root_search,text=value[6])
                    lab_acc.place(x=630,y=250)
                    
                    lab_bank=Label(root_search,text=value[7])
                    lab_bank.place(x=840,y=250)
                    
                    lab_club=Label(root_search,text=value[12])
                    lab_club.place(x=150,y=300)
                    
                    lab_des=Label(root_search,text=value[13])
                    lab_des.place(x=410,y=300)
                    
                    lab_DOJ=Label(root_search,text=value[15])
                    lab_DOJ.place(x=630,y=300)

                    lab_DR=Label(root_search,text=value[14])
                    lab_DR.place(x=840,y=300)
                    
                    lab_Type=Label(root_search,text=value[17])
                    lab_Type.place(x=150,y=350)
                    
                    lab_Rights=Label(root_search,text=value[19])
                    lab_Rights.place(x=410,y=350)
                    
                    lab_status=Label(root_search,text=value[20])
                    lab_status.place(x=630,y=350)

                    lab_IO_ref=Label(root_search,text=value[5])
                    lab_IO_ref.place(x=840,y=350)

                    b_sumbit=Button(root_search,text='Search',command=lambda:[wid_destroy_contract(),chk_input()])
                    b_sumbit.place(x=380,y=100)

                    
        b_sumbit=Button(root_search,text='Search',command=lambda:[chk_input()])
        b_sumbit.place(x=380,y=100)

        b_back=Button(root_search,text='Back',padx=5,command=lambda:[root_search.destroy(),admin()])
        b_back.place(x=530,y=100)

        mainloop()
    def delete():
        def del_emp():
            a=e_id.get()
            if len(a)==0:
                response=messagebox.showerror('Error','You left a field empty.')
            elif a.isdigit()==False:
                response=messagebox.showerror('Error','Incorrect input')
            else:
                j=int(a)
                if j==10101:
                    response=messagebox.showerror('Error','You cannot delete the main admin')
                else:
                    s='select * from emp where id=%s'%(a)
                    t=c1.execute(s)
                    if t==0:
                        response=messagebox.showerror("Error","Entered employee doesn't exist.")
                    else:
                        s='delete from emp where id=%s'%(a)
                        c1.execute(s)
                        conn.commit()
                        messagebox.showinfo('Deleted','Employee has been deleted.')

        root_del=Tk()
        root_del.geometry('500x200')
        root_del.title('Delete')
        root_del.resizable(False,False)

        lab_ask=Label(root_del,text='Enter ID of employee you want to delete:')
        lab_ask.place(x=75,y=50)

        e_id=Entry(root_del)
        e_id.place(x=300,y=50)

        submit_button=Button(root_del,text='Submit',command=del_emp)
        submit_button.place(x=175,y=100)

        b_back=Button(root_del,text='Back',padx=6,command=lambda:[root_del.destroy(),admin()])
        b_back.place(x=275,y=100)

    def view(ID):
        root_view=Tk()
        root_view.geometry('1200x800')
        root_view.title('View Payslip')
        root_view.resizable(False,False)

        MONTH_NOW=StringVar()
        MONTH_NOW.set("January")

        lab_month=Label(root_view,text='Month:')
        lab_month.place(x=300,y=50)

        lab_year=Label(root_view,text='Year:')
        lab_year.place(x=600,y=50)

        drop=OptionMenu(root_view,MONTH_NOW,"January","February","March","April","May","June","July","August","September","October","November","December")
        drop.place(x=400,y=50)

        e_YEAR=Entry(root_view)
        e_YEAR.place(x=700,y=50)
        def month_check(ID,M,Y):
            for i in Y:
                if i.isdigit():
                    pass
                else:
                    response=messagebox.showerror('Error','Invalid input.')
                    b=Button(root_view,text='Enter',command=lambda:[month_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                    b.place(x=900,y=50)
                    break
            else:
                if type(M)==str:
                    L=['january','february','march','april','may','june','july','august','september','october','november','december']
                    chk_m=M.lower()
                    if chk_m not in L:
                        pass
                    else:
                        for i in range(1900,10000):
                            if i==int(Y):
                                fetch(ID,M,Y)
                                break
                        else:
                            b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                            b.place(x=900,y=50)
                            response=messagebox.showerror('Error','Year out of range.')
                else:
                    pass
        def type_emp(rec,pay,day):
            TYPE=rec[0][17]
            TYPE=TYPE.upper()
            if TYPE=='CONTRACT':
                headings_cont()
                show_contract(rec,pay,day)
            elif TYPE=='PERMANENT':
                headings_emp()
                show_emp(rec,pay,day)
        def show_contract(rec,pay,day):
            def destroy_cont():
                l_ID.destroy()  
                l_FN.destroy()
                l_LN.destroy()
                l_ADD.destroy()
                l_DEPT.destroy()
                l_ACC.destroy()
                l_BANK.destroy()
                l_DES.destroy()
                l_DOJ.destroy()
                l_DAYS.destroy()
                l_CLUB.destroy()
                l_NET.destroy()
                l_DR.destroy()
                l_MONTH.destroy()
                l_YEAR.destroy()
            b=Button(root_view,text='Enter',command=lambda:[destroy_cont(),month_check(ID,MONTH_NOW.get(),e_YEAR.get())])
            b.place(x=900,y=50)
            
            rec=rec[0]
            ID=rec[0]
            FN=rec[1]
            LN=rec[2]
            ADD=rec[3]
            DEPT=rec[4]
            ACC=rec[6]
            BANK=rec[7]
            CLUB=rec[12]
            DES=rec[13]
            DR=rec[14]
            DOJ=rec[15]
            PF_ACC=rec[16]
            DAYS=day[0][0]
            MONTH=pay[0][3]
            YEAR=pay[0][4]
            NET=pay[0][1]
            l_ID=Label(root_view,text=ID)
            l_ID.place(x=200,y=150)        
            l_FN=Label(root_view,text=FN)
            l_FN.place(x=500,y=150)
            l_LN=Label(root_view,text=LN)
            l_LN.place(x=800,y=150)
            l_ADD=Label(root_view,text=ADD)
            l_ADD.place(x=1050,y=150)
            l_DEPT=Label(root_view,text=DEPT)
            l_DEPT.place(x=200,y=200)
            l_ACC=Label(root_view,text=ACC)
            l_ACC.place(x=500,y=200)
            l_BANK=Label(root_view,text=BANK)
            l_BANK.place(x=800,y=200)
            l_DES=Label(root_view,text=DES)
            l_DES.place(x=1050,y=200)
            l_DOJ=Label(root_view,text=DOJ)
            l_DOJ.place(x=200,y=250)

            l_DAYS=Label(root_view,text=DAYS)
            l_DAYS.place(x=800,y=300)
            l_DR=Label(root_view,text=DR)
            l_DR.place(x=500,y=400)

            l_CLUB=Label(root_view,text=CLUB)
            l_CLUB.place(x=500,y=450)

            l_NET=Label(root_view,text=NET)
            l_NET.place(x=800,y=500)
            l_MONTH=Label(root_view,text=MONTH)
            l_MONTH.place(x=800,y=250)
            l_YEAR=Label(root_view,text=YEAR)
            l_YEAR.place(x=1050,y=250)

        def headings_emp():
            h_ID=Label(root_view,text='ID:')
            h_ID.place(x=50,y=150)        
            h_FN=Label(root_view,text='First Name:')
            h_FN.place(x=350,y=150)
            h_LN=Label(root_view,text='Last Name:')
            h_LN.place(x=650,y=150)
            h_ADD=Label(root_view,text='Address:')
            h_ADD.place(x=950,y=150)
            h_DEPT=Label(root_view,text='Department ID:')
            h_DEPT.place(x=50,y=200)
            h_ACC=Label(root_view,text='Account:')
            h_ACC.place(x=350,y=200)
            h_BANK=Label(root_view,text='Bank:')
            h_BANK.place(x=650,y=200)
            h_DES=Label(root_view,text='Designation:')
            h_DES.place(x=950,y=200)
            h_DOJ=Label(root_view,text='Date of joining:')
            h_DOJ.place(x=50,y=250)
            h_PFACC=Label(root_view,text='PF Account:')
            h_PFACC.place(x=350,y=250)
            h_DAYS=Label(root_view,text='Days worked:')
            h_DAYS.place(x=650,y=300)
            h_BASIC=Label(root_view,text='Basic:')
            h_BASIC.place(x=350,y=500)
            h_HRA=Label(root_view,text='House Rental Allowance:')
            h_HRA.place(x=350,y=525)
            h_SA=Label(root_view,text='Special Allowance:')
            h_SA.place(x=350,y=550)
            h_PF=Label(root_view,text='Provident Fund:')
            h_PF.place(x=650,y=525)
            h_CLUB=Label(root_view,text='Club Contribution:')
            h_CLUB.place(x=350,y=575)

            h_TAX=Label(root_view,text='Tax:')
            h_TAX.place(x=650,y=500)
            h_NET=Label(root_view,text='Net Salary:')
            h_NET.place(x=650,y=600)
            h_MONTH=Label(root_view,text='Month:')
            h_MONTH.place(x=650,y=250)
            h_YEAR=Label(root_view,text='Year:')
            h_YEAR.place(x=950,y=250)
        def headings_cont():
            h_ID=Label(root_view,text='ID:')
            h_ID.place(x=50,y=150)        
            h_FN=Label(root_view,text='First Name:')
            h_FN.place(x=350,y=150)
            h_LN=Label(root_view,text='Last Name:')
            h_LN.place(x=650,y=150)
            h_ADD=Label(root_view,text='Address:')
            h_ADD.place(x=950,y=150)
            h_DEPT=Label(root_view,text='Department ID:')
            h_DEPT.place(x=50,y=200)
            h_ACC=Label(root_view,text='Account:')
            h_ACC.place(x=350,y=200)
            h_BANK=Label(root_view,text='Bank:')
            h_BANK.place(x=650,y=200)
            h_DES=Label(root_view,text='Designation:')
            h_DES.place(x=950,y=200)
            h_DOJ=Label(root_view,text='Date of joining:')
            h_DOJ.place(x=50,y=250)
            h_DAYS=Label(root_view,text='Days worked:')
            h_DAYS.place(x=650,y=300)
            h_DR=Label(root_view,text='Daily rate:')
            h_DR.place(x=350,y=400)
            h_CLUB=Label(root_view,text='Club Contribution:')
            h_CLUB.place(x=350,y=450)

            h_NET=Label(root_view,text='Net Salary:')
            h_NET.place(x=650,y=500)
            h_MONTH=Label(root_view,text='Month:')
            h_MONTH.place(x=650,y=250)
            h_YEAR=Label(root_view,text='Year:')
            h_YEAR.place(x=950,y=250)


        def show_emp(rec,pay,day):
            def destroy_emp():
                l_ID.destroy()
                l_FN.destroy()
                l_LN.destroy()
                l_ADD.destroy()
                l_DEPT.destroy()
                l_ACC.destroy()
                l_BANK.destroy()
                l_DES.destroy()
                l_DOJ.destroy()
                l_PFACC.destroy()
                l_DAYS.destroy()
                l_BASIC.destroy()
                l_HRA.destroy()
                l_SA.destroy()
                l_PF.destroy()
                l_CLUB.destroy()

                l_TAX.destroy()
                l_NET.destroy()
                l_MONTH.destroy()
                l_YEAR.destroy()

            b=Button(root_view,text='Enter',command=lambda:[destroy_emp(),len_check(ID,MONTH_NOW.get(),e_YEAR.get())])
            b.place(x=900,y=50)
            rec=rec[0]
            ID=rec[0]
            FN=rec[1]
            LN=rec[2]
            ADD=rec[3]
            DEPT=rec[4]
            ACC=rec[6]
            BANK=rec[7]
            BASIC=rec[8]
            HRA=rec[9]
            SA=rec[10]
            PF=rec[11]
            CLUB=rec[12]
            DES=rec[13]
            DOJ=rec[15]
            PF_ACC=rec[16]
            DAYS=day[0][0]
            MONTH=pay[0][3]
            YEAR=pay[0][4]
            NET=pay[0][1]
            TAX=pay[0][2]
            l_ID=Label(root_view,text=ID)
            l_ID.place(x=200,y=150)        
            l_FN=Label(root_view,text=FN)
            l_FN.place(x=500,y=150)
            l_LN=Label(root_view,text=LN)
            l_LN.place(x=800,y=150)
            l_ADD=Label(root_view,text=ADD)
            l_ADD.place(x=1050,y=150)
            l_DEPT=Label(root_view,text=DEPT)
            l_DEPT.place(x=200,y=200)
            l_ACC=Label(root_view,text=ACC)
            l_ACC.place(x=500,y=200)
            l_BANK=Label(root_view,text=BANK)
            l_BANK.place(x=800,y=200)
            l_DES=Label(root_view,text=DES)
            l_DES.place(x=1050,y=200)
            l_DOJ=Label(root_view,text=DOJ)
            l_DOJ.place(x=200,y=250)
            l_PFACC=Label(root_view,text=PF_ACC)
            l_PFACC.place(x=500,y=250)
            l_DAYS=Label(root_view,text=DAYS)
            l_DAYS.place(x=800,y=300)
            l_BASIC=Label(root_view,text=BASIC)
            l_BASIC.place(x=500,y=500)
            l_HRA=Label(root_view,text=HRA)
            l_HRA.place(x=500,y=525)
            l_SA=Label(root_view,text=SA)
            l_SA.place(x=500,y=550)
            l_PF=Label(root_view,text=PF)
            l_PF.place(x=800,y=525)
            l_CLUB=Label(root_view,text=CLUB)
            l_CLUB.place(x=500,y=575)

            l_TAX=Label(root_view,text=TAX)
            l_TAX.place(x=800,y=500)
            l_NET=Label(root_view,text=NET)
            l_NET.place(x=800,y=600)
            l_MONTH=Label(root_view,text=MONTH)
            l_MONTH.place(x=800,y=250)
            l_YEAR=Label(root_view,text=YEAR)
            l_YEAR.place(x=1050,y=250)

        def fetch(ID,month,year):
            s='select * from emp where ID=%s'%(ID)
            c1.execute(s)
            p='select * from payslip where ID=%s and month="%s" and year=%s'%(ID,month,year)
            g=c1.fetchall()
            c1.execute(p)
            k=c1.fetchall()
            t='select no_days from timesheet where ID=%s and month="%s" and year=%s'%(ID,month,year)
            c1.execute(t)
            j=c1.fetchall()
            if len(k)==0 or len(j)==0:
                response=messagebox.showinfo('Not Found',"Payslip doesn't exist.")
                b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                b.place(x=900,y=50)
            else:
                type_emp(g,k,j)

        def len_check(ID,Month,Year):
            if len(Year)==0:
                respose=messagebox.showerror('Error','No year entered.')
                b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                b.place(x=900,y=50)
            elif Year.isdigit()==False:
                respose=messagebox.showerror('Error','Invalid input.')
                b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                b.place(x=900,y=50)                
            else:
                month_check(ID,Month,Year)
        b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
        b.place(x=900,y=50)

        b_exit=Button(root_view,text='Back',command=lambda:[root_view.destroy(),admin()])
        b_exit.place(x=950,y=50)
        
    def view_EMP(ID):
        root_view=Tk()
        root_view.geometry('1200x800')
        root_view.title('View Payslip')
        root_view.resizable(False,False)

        MONTH_NOW=StringVar()
        MONTH_NOW.set("January")

        lab_month=Label(root_view,text='Month:')
        lab_month.place(x=300,y=50)

        lab_year=Label(root_view,text='Year:')
        lab_year.place(x=600,y=50)

        drop=OptionMenu(root_view,MONTH_NOW,"January","February","March","April","May","June","July","August","September","October","November","December")
        drop.place(x=400,y=50)

        e_YEAR=Entry(root_view)
        e_YEAR.place(x=700,y=50)
        def month_check(ID,M,Y):
            for i in Y:
                if i.isdigit():
                    pass
                else:
                    response=messagebox.showerror('Error','Invalid input.')
                    b=Button(root_view,text='Enter',command=lambda:[month_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                    b.place(x=900,y=50)
                    break
            else:
                if type(M)==str:
                    L=['january','february','march','april','may','june','july','august','september','october','november','december']
                    chk_m=M.lower()
                    if chk_m not in L:
                        pass
                    else:
                        for i in range(1900,10000):
                            if i==int(Y):
                                fetch(ID,M,Y)
                                break
                        else:
                            b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                            b.place(x=900,y=50)
                            response=messagebox.showerror('Error','Year out of range.')
                else:
                    pass
        def type_emp(rec,pay,day):
            TYPE=rec[0][17]
            TYPE=TYPE.upper()
            if TYPE=='CONTRACT':
                headings_cont()
                show_contract(rec,pay,day)
            elif TYPE=='PERMANENT':
                headings_emp()
                show_emp(rec,pay,day)
        def show_contract(rec,pay,day):
            def destroy_cont():
                l_ID.destroy()  
                l_FN.destroy()
                l_LN.destroy()
                l_ADD.destroy()
                l_DEPT.destroy()
                l_ACC.destroy()
                l_BANK.destroy()
                l_DES.destroy()
                l_DOJ.destroy()
                l_DAYS.destroy()
                l_CLUB.destroy()
                l_NET.destroy()
                l_DR.destroy()
                l_MONTH.destroy()
                l_YEAR.destroy()
            b=Button(root_view,text='Enter',command=lambda:[destroy_cont(),month_check(ID,MONTH_NOW.get(),e_YEAR.get())])
            b.place(x=900,y=50)
            
            rec=rec[0]
            ID=rec[0]
            FN=rec[1]
            LN=rec[2]
            ADD=rec[3]
            DEPT=rec[4]
            ACC=rec[6]
            BANK=rec[7]
            CLUB=rec[12]
            DES=rec[13]
            DR=rec[14]
            DOJ=rec[15]
            PF_ACC=rec[16]
            DAYS=day[0][0]
            MONTH=pay[0][3]
            YEAR=pay[0][4]
            NET=pay[0][1]
            l_ID=Label(root_view,text=ID)
            l_ID.place(x=200,y=150)        
            l_FN=Label(root_view,text=FN)
            l_FN.place(x=500,y=150)
            l_LN=Label(root_view,text=LN)
            l_LN.place(x=800,y=150)
            l_ADD=Label(root_view,text=ADD)
            l_ADD.place(x=1050,y=150)
            l_DEPT=Label(root_view,text=DEPT)
            l_DEPT.place(x=200,y=200)
            l_ACC=Label(root_view,text=ACC)
            l_ACC.place(x=500,y=200)
            l_BANK=Label(root_view,text=BANK)
            l_BANK.place(x=800,y=200)
            l_DES=Label(root_view,text=DES)
            l_DES.place(x=1050,y=200)
            l_DOJ=Label(root_view,text=DOJ)
            l_DOJ.place(x=200,y=250)

            l_DAYS=Label(root_view,text=DAYS)
            l_DAYS.place(x=800,y=300)
            l_DR=Label(root_view,text=DR)
            l_DR.place(x=500,y=400)

            l_CLUB=Label(root_view,text=CLUB)
            l_CLUB.place(x=500,y=450)

            l_NET=Label(root_view,text=NET)
            l_NET.place(x=800,y=500)
            l_MONTH=Label(root_view,text=MONTH)
            l_MONTH.place(x=800,y=250)
            l_YEAR=Label(root_view,text=YEAR)
            l_YEAR.place(x=1050,y=250)

        def headings_emp():
            h_ID=Label(root_view,text='ID:')
            h_ID.place(x=50,y=150)        
            h_FN=Label(root_view,text='First Name:')
            h_FN.place(x=350,y=150)
            h_LN=Label(root_view,text='Last Name:')
            h_LN.place(x=650,y=150)
            h_ADD=Label(root_view,text='Address:')
            h_ADD.place(x=950,y=150)
            h_DEPT=Label(root_view,text='Department ID:')
            h_DEPT.place(x=50,y=200)
            h_ACC=Label(root_view,text='Account:')
            h_ACC.place(x=350,y=200)
            h_BANK=Label(root_view,text='Bank:')
            h_BANK.place(x=650,y=200)
            h_DES=Label(root_view,text='Designation:')
            h_DES.place(x=950,y=200)
            h_DOJ=Label(root_view,text='Date of joining:')
            h_DOJ.place(x=50,y=250)
            h_PFACC=Label(root_view,text='PF Account:')
            h_PFACC.place(x=350,y=250)
            h_DAYS=Label(root_view,text='Days worked:')
            h_DAYS.place(x=650,y=300)
            h_BASIC=Label(root_view,text='Basic:')
            h_BASIC.place(x=350,y=500)
            h_HRA=Label(root_view,text='House Rental Allowance:')
            h_HRA.place(x=350,y=525)
            h_SA=Label(root_view,text='Special Allowance:')
            h_SA.place(x=350,y=550)
            h_PF=Label(root_view,text='Provident Fund:')
            h_PF.place(x=650,y=525)
            h_CLUB=Label(root_view,text='Club Contribution:')
            h_CLUB.place(x=350,y=575)

            h_TAX=Label(root_view,text='Tax:')
            h_TAX.place(x=650,y=500)
            h_NET=Label(root_view,text='Net Salary:')
            h_NET.place(x=650,y=600)
            h_MONTH=Label(root_view,text='Month:')
            h_MONTH.place(x=650,y=250)
            h_YEAR=Label(root_view,text='Year:')
            h_YEAR.place(x=950,y=250)
        def headings_cont():
            h_ID=Label(root_view,text='ID:')
            h_ID.place(x=50,y=150)        
            h_FN=Label(root_view,text='First Name:')
            h_FN.place(x=350,y=150)
            h_LN=Label(root_view,text='Last Name:')
            h_LN.place(x=650,y=150)
            h_ADD=Label(root_view,text='Address:')
            h_ADD.place(x=950,y=150)
            h_DEPT=Label(root_view,text='Department ID:')
            h_DEPT.place(x=50,y=200)
            h_ACC=Label(root_view,text='Account:')
            h_ACC.place(x=350,y=200)
            h_BANK=Label(root_view,text='Bank:')
            h_BANK.place(x=650,y=200)
            h_DES=Label(root_view,text='Designation:')
            h_DES.place(x=950,y=200)
            h_DOJ=Label(root_view,text='Date of joining:')
            h_DOJ.place(x=50,y=250)
            h_DAYS=Label(root_view,text='Days worked:')
            h_DAYS.place(x=650,y=300)
            h_DR=Label(root_view,text='Daily rate:')
            h_DR.place(x=350,y=400)
            h_CLUB=Label(root_view,text='Club Contribution:')
            h_CLUB.place(x=350,y=450)

            h_NET=Label(root_view,text='Net Salary:')
            h_NET.place(x=650,y=500)
            h_MONTH=Label(root_view,text='Month:')
            h_MONTH.place(x=650,y=250)
            h_YEAR=Label(root_view,text='Year:')
            h_YEAR.place(x=950,y=250)


        def show_emp(rec,pay,day):
            def destroy_emp():
                l_ID.destroy()
                l_FN.destroy()
                l_LN.destroy()
                l_ADD.destroy()
                l_DEPT.destroy()
                l_ACC.destroy()
                l_BANK.destroy()
                l_DES.destroy()
                l_DOJ.destroy()
                l_PFACC.destroy()
                l_DAYS.destroy()
                l_BASIC.destroy()
                l_HRA.destroy()
                l_SA.destroy()
                l_PF.destroy()
                l_CLUB.destroy()

                l_TAX.destroy()
                l_NET.destroy()
                l_MONTH.destroy()
                l_YEAR.destroy()

            b=Button(root_view,text='Enter',command=lambda:[destroy_emp(),len_check(ID,MONTH_NOW.get(),e_YEAR.get())])
            b.place(x=900,y=50)
            rec=rec[0]
            ID=rec[0]
            FN=rec[1]
            LN=rec[2]
            ADD=rec[3]
            DEPT=rec[4]
            ACC=rec[6]
            BANK=rec[7]
            BASIC=rec[8]
            HRA=rec[9]
            SA=rec[10]
            PF=rec[11]
            CLUB=rec[12]
            DES=rec[13]
            DOJ=rec[15]
            PF_ACC=rec[16]
            DAYS=day[0][0]
            MONTH=pay[0][3]
            YEAR=pay[0][4]
            NET=pay[0][1]
            TAX=pay[0][2]
            l_ID=Label(root_view,text=ID)
            l_ID.place(x=200,y=150)        
            l_FN=Label(root_view,text=FN)
            l_FN.place(x=500,y=150)
            l_LN=Label(root_view,text=LN)
            l_LN.place(x=800,y=150)
            l_ADD=Label(root_view,text=ADD)
            l_ADD.place(x=1050,y=150)
            l_DEPT=Label(root_view,text=DEPT)
            l_DEPT.place(x=200,y=200)
            l_ACC=Label(root_view,text=ACC)
            l_ACC.place(x=500,y=200)
            l_BANK=Label(root_view,text=BANK)
            l_BANK.place(x=800,y=200)
            l_DES=Label(root_view,text=DES)
            l_DES.place(x=1050,y=200)
            l_DOJ=Label(root_view,text=DOJ)
            l_DOJ.place(x=200,y=250)
            l_PFACC=Label(root_view,text=PF_ACC)
            l_PFACC.place(x=500,y=250)
            l_DAYS=Label(root_view,text=DAYS)
            l_DAYS.place(x=800,y=300)
            l_BASIC=Label(root_view,text=BASIC)
            l_BASIC.place(x=500,y=500)
            l_HRA=Label(root_view,text=HRA)
            l_HRA.place(x=500,y=525)
            l_SA=Label(root_view,text=SA)
            l_SA.place(x=500,y=550)
            l_PF=Label(root_view,text=PF)
            l_PF.place(x=800,y=525)
            l_CLUB=Label(root_view,text=CLUB)
            l_CLUB.place(x=500,y=575)

            l_TAX=Label(root_view,text=TAX)
            l_TAX.place(x=800,y=500)
            l_NET=Label(root_view,text=NET)
            l_NET.place(x=800,y=600)
            l_MONTH=Label(root_view,text=MONTH)
            l_MONTH.place(x=800,y=250)
            l_YEAR=Label(root_view,text=YEAR)
            l_YEAR.place(x=1050,y=250)

        def fetch(ID,month,year):
            s='select * from emp where ID=%s'%(ID)
            c1.execute(s)
            p='select * from payslip where ID=%s and month="%s" and year=%s'%(ID,month,year)
            g=c1.fetchall()
            c1.execute(p)
            k=c1.fetchall()
            t='select no_days from timesheet where ID=%s and month="%s" and year=%s'%(ID,month,year)
            c1.execute(t)
            j=c1.fetchall()
            if len(k)==0 or len(j)==0:
                response=messagebox.showinfo('Not Found',"Payslip doesn't exist.")
                b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                b.place(x=900,y=50)
            else:
                type_emp(g,k,j)

        def len_check(ID,Month,Year):
            if len(Year)==0:
                respose=messagebox.showerror('Error','No year entered.')
                b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                b.place(x=900,y=50)
            elif Year.isdigit()==False:
                respose=messagebox.showerror('Error','Invalid input.')
                b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
                b.place(x=900,y=50)                
            else:
                month_check(ID,Month,Year)
        b=Button(root_view,text='Enter',command=lambda:[len_check(ID,MONTH_NOW.get(),e_YEAR.get()),b.destroy()])
        b.place(x=900,y=50)

        b_exit=Button(root_view,text='Back',command=lambda:[root_view.destroy(),Emp_window()])
        b_exit.place(x=950,y=50)

    def time_sheet(ID):
        def timesheet(ID,IO_REF):
            root_ts=Tk()
            root_ts.title('timesheet')
            root_ts.geometry('500x200')
            root_ts.resizable(False,False)

            date=datetime.datetime.now()
            month=date.strftime('%B')

            lab_month=Label(root_ts,text='Current Month:')
            lab_month.place(x=150,y=75)

            lab_mon=Label(root_ts,text=month)
            lab_mon.place(x=250,y=75)

            lab_nodays=Label(root_ts,text='Number of days worked:')
            lab_nodays.place(x=100,y=50)

            e_nodays=Entry(root_ts)
            e_nodays.place(x=250,y=50)

            b_button=Button(root_ts,text='Submit',command=lambda:[date(ID,IO_REF,e_nodays.get())])
            b_button.place(x=175,y=130)

            b_back=Button(root_ts,text='Back',command=lambda:[root_ts.destroy(),admin()])
            b_back.place(x=250,y=130)

            def date(ID,IO_REF,NO_DAYS):
                if NO_DAYS.isdigit() and len(NO_DAYS)!=0:
                    now=datetime.datetime.now()
                    year=now.strftime('%Y')
                    year=int(year)
                    month_no=now.strftime('%m')
                    month_no=int(month_no)
                    month=now.strftime('%B')
                    day=now.strftime('%d')
                    day=int(day)

                    L=[1,2,3,4,5,6,7,8,9,10,11,12]
                    L2=[31,28,31,30,31,30,31,31,30,31,30,31]
                    for i in range(len(L)):
                        if L[i]==month_no:
                            if L2[i]==day:
                                check_day(ID,IO_REF,NO_DAYS,month,year,L2[i])
                            else:
                                check_day(ID,IO_REF,NO_DAYS,month,year,L2[i])
                                response=messagebox.showerror('Error',"Can't run before month end.")
                else:
                           response=messagebox.showerror('Error','Invalid input.')
            def add_time(ID,IO_REF,NO_DAYS,MONTH,YEAR):
                s='insert into timesheet(ID,NO_DAYS,IO_REF_CODE,MONTH,YEAR) values(%s,%s,%s,"%s",%s)'%(ID,NO_DAYS,IO_REF,MONTH,YEAR)
                c1.execute(s)
                conn.commit()
                respone=messagebox.showinfo('Done','Timesheet added.')
                root_ts.destroy()
                admin()

            def check_day(ID,IO_REF,NO_DAYS,MONTH,YEAR,MAX):
                NO_DAYS=int(NO_DAYS)
                p=type(NO_DAYS)
                if p==int:
                    if NO_DAYS<=0:
                        response=messagebox.showerror('Error','Invalid input')
                    elif NO_DAYS>MAX:
                        response=messagebox.showerror('Error','Invalid input')
                    else:
                        verify_run(ID,IO_REF,NO_DAYS,MONTH,YEAR)
                else:
                    response=messagebox.showerror('Error','Invalid input')

            def verify_run(ID,IO_REF,NO_DAYS,MONTH,YEAR):
                s='select * from timesheet where month="%s" and year=%s and ID=%s'%(MONTH,YEAR,ID)
                a=c1.execute(s)
                if a==0:
                    add_time(ID,IO_REF,NO_DAYS,MONTH,YEAR)
                else:
                    response=messagebox.showerror('Already exists.','Already exists.')
        def IO_ref_get(ID):
            s='select IO_REF_CODE from emp where id="%s"'%(ID)
            c1.execute(s)
            p=c1.fetchall()
            IO=p[0][0]
            timesheet(ID,IO)
        IO_ref_get(ID)
        
    def time_sheet_EMP(ID):
        def timesheet(ID,IO_REF):
            root_ts=Tk()
            root_ts.title('timesheet')
            root_ts.geometry('500x200')
            root_ts.resizable(False,False)

            date=datetime.datetime.now()
            month=date.strftime('%B')

            lab_month=Label(root_ts,text='Current Month:')
            lab_month.place(x=150,y=75)

            lab_mon=Label(root_ts,text=month)
            lab_mon.place(x=250,y=75)

            lab_nodays=Label(root_ts,text='Number of days worked:')
            lab_nodays.place(x=100,y=50)

            e_nodays=Entry(root_ts)
            e_nodays.place(x=250,y=50)

            b_button=Button(root_ts,text='Submit',command=lambda:[date(ID,IO_REF,e_nodays.get())])
            b_button.place(x=175,y=130)

            b_back=Button(root_ts,text='Back',command=lambda:[root_ts.destroy(),Emp_window()])
            b_back.place(x=250,y=130)

            def date(ID,IO_REF,NO_DAYS):
                if NO_DAYS.isdigit() and len(NO_DAYS)!=0:
                    now=datetime.datetime.now()
                    year=now.strftime('%Y')
                    year=int(year)
                    month_no=now.strftime('%m')
                    month_no=int(month_no)
                    month=now.strftime('%B')
                    day=now.strftime('%d')
                    day=int(day)

                    L=[1,2,3,4,5,6,7,8,9,10,11,12]
                    L2=[31,28,31,30,31,30,31,31,30,31,30,31]
                    for i in range(len(L)):
                        if L[i]==month_no:
                            if L2[i]==day:
                                check_day(ID,IO_REF,NO_DAYS,month,year,L2[i])
                            else:
                                check_day(ID,IO_REF,NO_DAYS,month,year,L2[i])
                                response=messagebox.showerror('Error',"Can't run before month end.")
                else:
                           response=messagebox.showerror('Error','Invalid input.')
            def add_time(ID,IO_REF,NO_DAYS,MONTH,YEAR):
                s='insert into timesheet(ID,NO_DAYS,IO_REF_CODE,MONTH,YEAR) values(%s,%s,%s,"%s",%s)'%(ID,NO_DAYS,IO_REF,MONTH,YEAR)
                c1.execute(s)
                conn.commit()
                respone=messagebox.showinfo('Done','Timesheet added.')
                root_ts.destroy()
                Emp_window()

            def check_day(ID,IO_REF,NO_DAYS,MONTH,YEAR,MAX):
                NO_DAYS=int(NO_DAYS)
                p=type(NO_DAYS)
                if p==int:
                    if NO_DAYS<=0:
                        response=messagebox.showerror('Error','Invalid input')
                    elif NO_DAYS>MAX:
                        response=messagebox.showerror('Error','Invalid input')
                    else:
                        verify_run(ID,IO_REF,NO_DAYS,MONTH,YEAR)
                else:
                    response=messagebox.showerror('Error','Invalid input')

            def verify_run(ID,IO_REF,NO_DAYS,MONTH,YEAR):
                s='select * from timesheet where month="%s" and year=%s and ID=%s'%(MONTH,YEAR,ID)
                a=c1.execute(s)
                if a==0:
                    add_time(ID,IO_REF,NO_DAYS,MONTH,YEAR)
                else:
                    response=messagebox.showerror('Already exists.','Already exists.')
        def IO_ref_get(ID):
            s='select IO_REF_CODE from emp where id="%s"'%(ID)
            c1.execute(s)
            p=c1.fetchall()
            IO=p[0][0]
            timesheet(ID,IO)
        IO_ref_get(ID)
    
    def pay_process():
        root_pay=Tk()
        root_pay.title('Payroll Process')
        root_pay.geometry('500x200')
        root_pay.resizable(False,False)
        def exist(month,year):
            s='select * from payslip where month="%s" and year=%s'%(month,year)
            c=c1.execute(s)
            if c==0:
                return True
        def input_id():
            s='select id from emp where staus_AT="%s" order by id'%('ACTIVE')
            c1.execute(s)
            a=c1.fetchall()
            return a
        def input_timesheet(a,month,year):
            for i in a:
                id_=i[0]
                s='select * from TIMESHEET where MONTH="%s" and year=%s and id=%s order by id'%(month,year,id_)
                c1.execute(s)
                p=c1.fetchall()
                a='select * from emp where id=%s'%(id_)
                c1.execute(a)
                g=c1.fetchall()
                if len(p)==0:
                    continue
                else:
                    calc_fetch(g,p,month,year)
            root_pay.destroy()
            admin()
            
        def taxation(Basic):
            sal=Basic*12
            if sal<=250000:
                tax=0
                return tax/12
            elif sal>=250001 and sal<=500000:
                tax=sal*0.05
                return tax/12
            elif sal>=500001 and sal<=750000:
                tax=12500+(sal-500000)*0.1
                return tax/12
            elif sal>=750001 and sal<=1000000:
                tax=37500+(sal-750000)*0.15
                return tax/12
            elif sal>=1000001 and sal<=1250000:
                tax=75000+(sal-1000000)*0.2
                return tax/12
            elif sal>=1250001 and sal<=1500000:
                tax=12500+(sal-1250000)*0.25
                print(tax,Basic,sal)
                return tax/12
            elif sal>1500000:
                tax=187500+(sal-1500000)*0.3
                return tax/12
        def date_chk():
            now=datetime.datetime.now()
            year=now.strftime('%Y')
            year=int(year)
            month_no=now.strftime('%m')
            month_no=int(month_no)
            month=now.strftime('%B')
            day=now.strftime('%d')
            day=int(day)

            L=[1,2,3,4,5,6,7,8,9,10,11,12]
            L2=[31,28,31,30,31,30,31,31,30,31,30,31]
            for i in range(len(L)):
                if L[i]==month_no:
                    p=exist(month,year)
                    if p==True:
                        if L2[i]==day:
                            a=input_id()
                            input_timesheet(a,month,year)
                        else:
                            a=input_id()
                            input_timesheet(a,month,year)
                            messagebox.showerror('Error',"Can't run before month end.")          
                    else:
                        messagebox.showerror('Error','Payslip already run.')
        def pay_emp(Basic,HRA,SA,PF,CLUB,DAYS):
            def month_div():
                date=datetime.datetime.now()
                month=date.strftime('%B')
                month=str(month)
                year=date.strftime('%Y')
                year=int(year)
                month=month.upper()
                L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
                L2=[31,29,31,30,31,30,31,31,30,31,30,31]
                L3=[31,28,31,30,31,30,31,31,30,31,30,31]
                if year==2021:
                    for i in range(len(L)):
                        if L[i]==month:
                            return L3[i]
                elif year==2020:
                    for i in range(len(L)):
                        if L[i]==month:
                            return L2[i]
            def month_now():
                date=datetime.datetime.now()
                month=date.strftime('%B')
                month=str(month)
                year=date.strftime('%Y')
                year=int(year)
                month=month.upper()
                L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
                if year==2020:
                    L2=[23,20,22,22,21,22,23,21,22,22,21,23]
                    for i in range(len(L)):
                        if L[i]==month:
                            return L2[i]
                elif year==2021:
                    L2=[21,20,23,22,21,22,22,22,22,21,22,23]
                    for i in range(len(L)):
                        if L[i]==month:
                            return L2[i]
            Mand_days=month_now()
            Div=month_div()
            D_basic=Basic/Div
            if DAYS<Mand_days:
                D_not_worked=Mand_days-DAYS
                SUB=D_basic*D_not_worked
                S_basic=Basic-SUB
                HRA=0.4*S_basic
                SA=0.5*S_basic
                tax_basic=S_basic+HRA+SA
                tax=taxation(tax_basic)
                total=S_basic+HRA+SA-PF-tax-CLUB
                return [tax,total]
            elif DAYS>Mand_days:
                D_extra=DAYS-Mand_days
                ADD=D_basic*D_extra
                S_basic=Basic+ADD
                HRA=0.4*S_basic
                SA=0.5*S_basic
                tax_basic=S_basic+HRA+SA
                tax=taxation(tax_basic)
                total=S_basic+HRA+SA-PF-tax-CLUB
                return [tax,total]
            elif DAYS==Mand_days:
                S_basic=Basic
                HRA=0.4*S_basic
                SA=0.5*S_basic
                tax_basic=S_basic+HRA+SA
                tax=taxation(tax_basic)
                total=S_basic+HRA+SA-PF-tax-CLUB
                return [tax,total]
        def pay_contract(DR,CLUB,DAYS):
            def month_div():
                date=datetime.datetime.now()
                month=date.strftime('%B')
                month=str(month)
                year=date.strftime('%Y')
                year=int(year)
                month=month.upper()
                L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
                L2=[31,29,31,30,31,30,31,31,30,31,30,31]
                L3=[31,28,31,30,31,30,31,31,30,31,30,31]
                if year==2021:
                    for i in range(len(L)):
                        if L[i]==month:
                            return L3[i]
                elif year==2020:
                    for i in range(len(L)):
                        if L[i]==month:
                            return L2[i]
            def month_now():
                date=datetime.datetime.now()
                month=date.strftime('%B')
                month=str(month)
                year=date.strftime('%Y')
                year=int(year)
                month=month.upper()
                L=['JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER']
                if year==2020:
                    L2=[23,20,22,22,21,22,23,21,22,22,21,23]
                    for i in range(len(L)):
                        if L[i]==month:
                            return L2[i]
                elif year==2021:
                    L2=[21,20,23,22,21,22,22,22,22,21,22,23]
                    for i in range(len(L)):
                        if L[i]==month:
                            return L2[i]
            Mand_days=month_now()
            Div=month_div()

            if DAYS>Mand_days:
                E_days=DAYS-Mand_days
                E_pay=500*E_days # 500 units of bonus for overtime            
                net_pay=DR*Mand_days+E_pay-CLUB
                return net_pay
            else:
                net_pay=DR*DAYS-CLUB
                return net_pay
        def calc_fetch(record,record_time,month,year):
            record=record[0]
            record_time=record_time[0]
            ID=record[0]
            Basic=record[8]
            HRA=record[9]
            SA=record[10]
            PF=record[11]
            CLUB=record[12]
            DR=record[14]
            TYPE=record[17]
            TYPE=TYPE.upper()
            No_days=record_time[1]
            if TYPE=='CONTRACT':
                L=pay_contract(DR,CLUB,No_days)
                payslip_contract(ID,L,month,year)
            elif TYPE=='PERMANENT':
                L=pay_emp(Basic,HRA,SA,PF,CLUB,No_days)
                net_pay=L[1]
                tax=L[0]
                payslip_emp(ID,net_pay,tax,month,year)
        def payslip_emp(ID,netpay,tax,month,year):
            s='insert into payslip values(%s,%s,%s,"%s",%s,NULL)'%(ID,netpay,tax,month,year)
            c1.execute(s)
            conn.commit()

        def payslip_contract(ID,net,month,year):
            s='insert into payslip values(%s,%s,NULL,"%s",%s,NULL)'%(ID,net,month,year)
            c1.execute(s)
            conn.commit()
        date=datetime.datetime.now()
        month=date.strftime('%B')
        L_display=Label(root_pay,text='Run payroll process for the month:')
        L_display.place(x=105,y=50)

        L_month=Label(root_pay,text=month)
        L_month.place(x=295,y=50)
        
        b_button=Button(root_pay,padx=5,text='Run',command=lambda:[date_chk()])
        b_button.place(x=200,y=100)

        b_back=Button(root_pay,padx=2,text='Back',command=lambda:[root_pay.destroy(),admin()])
        b_back.place(x=250,y=100)

        mainloop()
    def Pass_change():
        def Change(new,con):
            global Operating_ID
            def old_same(new):
                global Operating_ID
                s='select Password from emp where id=%s'%(Operating_ID)
                c1.execute(s)
                p=c1.fetchall()
                old=p[0][0]
                if old==new:
                    response=messagebox.showerror('Error',"New password can't be the same as old.")
                    return False
                elif len(new)>15:
                    response=messagebox.showerror('Error',"Password too long.")
                    return False
                elif len(new)==0:
                    response=messagebox.showerror('Error',"You left the field empty")
                    return False
                else:
                    return True
            def con_chk(new,con):
                if len(con)==0:
                    response=messagebox.showerror('Error',"You left the field empty")
                    return False
                elif new!=con:
                    response=messagebox.showerror('Error',"The two password are not matching. Please check and re-enter.")
                    return False
                else:
                    return True
            Check_old=old_same(new)
            if Check_old==True:
                Check_same=con_chk(new,con)
                if Check_old==True and Check_same==True:
                    stat='update emp set password="%s"where ID=%s'%(new,Operating_ID)
                    c1.execute(stat)
                    response=messagebox.showinfo('Done',"Your password has been updated.")
                    root_change.destroy()
                    admin()

        root_change=Tk()
        root_change.geometry('500x200')
        root_change.title('Change Password')
        root_change.resizable(False,False)

        L_New=Label(root_change,text='New Password :')
        L_New.place(x=100,y=50)

        L_Con=Label(root_change,text='Confirm Password :')
        L_Con.place(x=100,y=100)

        new=Entry(root_change,show='*')
        new.place(x=250,y=50)

        con=Entry(root_change,show='*')
        con.place(x=250,y=100)

        b_submit=Button(root_change,text='Confirm Changes',command=lambda:[Change(new.get(),con.get())])
        b_submit.place(x=150,y=150)

        b_back=Button(root_change,text='Back',padx=5,command=lambda:[root_change.destroy(),admin()])
        b_back.place(x=275,y=150)

        mainloop()

    def Pass_change_EMP():
        def Change(new,con):
            global Operating_ID
            def old_same(new):
                global Operating_ID
                s='select Password from emp where id=%s'%(Operating_ID)
                c1.execute(s)
                p=c1.fetchall()
                old=p[0][0]
                if old==new:
                    response=messagebox.showerror('Error',"New password can't be the same as old.")
                    return False
                elif len(new)>15:
                    response=messagebox.showerror('Error',"Password too long.")
                    return False
                elif len(new)==0:
                    response=messagebox.showerror('Error',"You left the field empty")
                    return False
                else:
                    return True
            def con_chk(new,con):
                if len(con)==0:
                    response=messagebox.showerror('Error',"You left the field empty")
                    return False
                elif new!=con:
                    response=messagebox.showerror('Error',"The two password are not matching. Please check and re-enter.")
                    return False
                else:
                    return True
            Check_old=old_same(new)
            if Check_old==True:
                Check_same=con_chk(new,con)
                if Check_old==True and Check_same==True:
                    stat='update emp set password="%s"where ID=%s'%(new,Operating_ID)
                    c1.execute(stat)
                    response=messagebox.showinfo('Done',"Your password has been updated.")
                    root_change.destroy()
                    Emp_window()

        root_change=Tk()
        root_change.geometry('500x200')
        root_change.title('Change Password')
        root_change.resizable(False,False)

        L_New=Label(root_change,text='New Password :')
        L_New.place(x=100,y=50)

        L_Con=Label(root_change,text='Confirm Password :')
        L_Con.place(x=100,y=100)

        new=Entry(root_change,show='*')
        new.place(x=250,y=50)

        con=Entry(root_change,show='*')
        con.place(x=250,y=100)

        b_submit=Button(root_change,text='Confirm Changes',command=lambda:[Change(new.get(),con.get())])
        b_submit.place(x=150,y=150)

        b_back=Button(root_change,text='Back',padx=5,command=lambda:[root_change.destroy(),Emp_window()])
        b_back.place(x=275,y=150)

        mainloop()
    def Emp_window():
        global Operating_ID
        s='select * from emp where ID="%s"'%(Operating_ID)
        c1.execute(s)
        m=c1.fetchall()
        r=m[0]

        root=Tk()
        root.geometry('800x800')
        root.title('Admin')
        root.resizable(False,False)

        ID=r[0]
        FN=r[1]
        LN=r[2]
        D_ID=r[4]
        ACC=r[6]
        DES=r[13]
        DOJ=r[15]
        NAME=FN+' '+LN

        w = Canvas(root, width=800, height=500)
        w.pack()

        w.create_line(0, 70, 800,70)
        w.create_line(0, 200, 800,200)

        date=datetime.datetime.now()
        Date=date.strftime("%d")
        Month=date.strftime("%m")
        Year=date.strftime("%y")

        F_date=Date+'-'+Month+'-'+Year
       
        


        H_DATE=Label(root,text='Date:')
        H_DATE.place(x=550,y=40)

        L_DATE=Label(root,text=F_date)
        L_DATE.place(x=650,y=40)

        H_ID=Label(root,text='Employee ID:')
        H_ID.place(x=75,y=100)

        H_NAME=Label(root,text='Name:')
        H_NAME.place(x=310,y=100)

        H_D_ID=Label(root,text='Department ID:')
        H_D_ID.place(x=75,y=150)

        H_ACC=Label(root,text='Account:')
        H_ACC.place(x=310,y=150)

        H_DES=Label(root,text='Designation:')
        H_DES.place(x=550,y=100)

        H_DOJ=Label(root,text='Date of joining:')
        H_DOJ.place(x=550,y=150)

        L_ID=Label(root,text=ID)
        L_ID.place(x=175,y=100)

        L_NAME=Label(root,text=NAME)
        L_NAME.place(x=410,y=100)

        L_D_ID=Label(root,text=D_ID)
        L_D_ID.place(x=175,y=150)

        L_ACC=Label(root,text=ACC)
        L_ACC.place(x=410,y=150)

        L_DES=Label(root,text=DES)
        L_DES.place(x=650,y=100)

        L_DOJ=Label(root,text=DOJ)
        L_DOJ.place(x=650,y=150)

        L_OPPE=Label(root,text='Personal Operations:')
        L_OPPE.place(x=25,y=500)

        
        b_time=Button(root,text='Fill timesheet',command=lambda:[root.destroy(),time_sheet_EMP(Operating_ID)],padx=5)
        b_time.place(x=300,y=500)

        b_view_slip=Button(root,text='View payslip',command=lambda:[root.destroy(),view_EMP(Operating_ID)],padx=10)
        b_view_slip.place(x=425,y=500)

        b_Pass=Button(root,text='Change Password',command=lambda:[root.destroy(),Pass_change_EMP()],padx=10)
        b_Pass.place(x=425,y=700)

        b_Logout=Button(root,text='Logout',padx=20,command=lambda:[root.destroy(),main()])
        b_Logout.place(x=300,y=700)
        mainloop()
    def admin():
        global Operating_ID
        s='select * from emp where ID="%s"'%(Operating_ID)
        c1.execute(s)
        m=c1.fetchall()
        r=m[0]
        
        root=Tk()
        root.geometry('800x800')
        root.title('Admin')
        root.resizable(False,False)

        ID=r[0]
        FN=r[1]
        LN=r[2]
        D_ID=r[4]
        ACC=r[6]
        DES=r[13]
        DOJ=r[15]
        NAME=FN+' '+LN

        w = Canvas(root, width=800, height=500,bd=0,highlightthickness=0)
        w.pack()

        w.create_line(0, 70, 800,70)
        w.create_line(0, 200, 800,200)

        date=datetime.datetime.now()
        Date=date.strftime("%d")
        Month=date.strftime("%m")
        Year=date.strftime("%y")

        F_date=Date+'-'+Month+'-'+Year        
        


        H_DATE=Label(root,text='Date:')
        H_DATE.place(x=550,y=40)

        L_DATE=Label(root,text=F_date)
        L_DATE.place(x=650,y=40)

        H_ID=Label(root,text='Employee ID:')
        H_ID.place(x=75,y=100)

        H_NAME=Label(root,text='Name:')
        H_NAME.place(x=310,y=100)

        H_D_ID=Label(root,text='Department ID:')
        H_D_ID.place(x=75,y=150)

        H_ACC=Label(root,text='Account:')
        H_ACC.place(x=310,y=150)

        H_DES=Label(root,text='Designation:')
        H_DES.place(x=550,y=100)

        H_DOJ=Label(root,text='Date of joining:')
        H_DOJ.place(x=550,y=150)

        L_ID=Label(root,text=ID)
        L_ID.place(x=175,y=100)

        L_NAME=Label(root,text=NAME)
        L_NAME.place(x=410,y=100)

        L_D_ID=Label(root,text=D_ID)
        L_D_ID.place(x=175,y=150)

        L_ACC=Label(root,text=ACC)
        L_ACC.place(x=410,y=150)

        L_DES=Label(root,text=DES)
        L_DES.place(x=650,y=100)

        L_DOJ=Label(root,text=DOJ)
        L_DOJ.place(x=650,y=150)

        L_OPE=Label(root,text='Employee Operations:')
        L_OPE.place(x=25,y=300)

        L_OPP=Label(root,text='Payroll Operations:')
        L_OPP.place(x=25,y=400)

        L_OPPE=Label(root,text='Personal Operations:')
        L_OPPE.place(x=25,y=500)
        
        b_add=Button(root,text='Add employee',command=lambda:[root.destroy(),add()],padx=5)
        b_add.place(x=185,y=300)

        b_Search=Button(root,text='Search employee',command=lambda:[root.destroy(),search()],padx=5)
        b_Search.place(x=300,y=300)

        b_update=Button(root,text='Update employee',command=lambda:[root.destroy(),update()],padx=5)
        b_update.place(x=425,y=300)
        
        b_delete=Button(root,text='Delete employee',command=lambda:[root.destroy(),delete()],padx=5)
        b_delete.place(x=550,y=300)

        b_payroll=Button(root,text='Generate Payslip',command=lambda:[root.destroy(),pay_process()],padx=5)
        b_payroll.place(x=185,y=400)

        b_time=Button(root,text='Fill timesheet',command=lambda:[root.destroy(),time_sheet(Operating_ID)],padx=5)
        b_time.place(x=185,y=500)

        b_view_slip=Button(root,text='View payslip',command=lambda:[root.destroy(),view(Operating_ID)],padx=5)
        b_view_slip.place(x=300,y=500)

        b_EX=Button(root,text='Exceptional Payroll',command=lambda:[root.destroy(),EXCEPTION()],padx=5)
        b_EX.place(x=300,y=400)

        b_Pass=Button(root,text='Change Password',command=lambda:[root.destroy(),Pass_change()],padx=10)
        b_Pass.place(x=425,y=700)

        b_Logout=Button(root,text='Logout',padx=20,command=lambda:[root.destroy(),main()])
        b_Logout.place(x=300,y=700)
        mainloop()

    def check():
        a=e_id.get()
        b=e_pass.get()
        if a.isdigit() and len(a)!=0:
            p=c1.execute('select password,rights,staus_AT from emp where id=%s'%(a))
            f=c1.fetchall()
            if p==0:
                response=messagebox.showerror('Error',"Entered id doesn't exist. Please try again.")
            else:
                if f[0][0]!=b:
                    response=messagebox.showerror('Error',"Entered password doesn't match. Please try again.")
                elif f[0][2]=='INACTIVE':
                    response=messagebox.showerror('Error',"Your account has been terminated. Please contact an admin for reauthorization.")
                else:
                    q=f[0][1]
                    r=q.upper()
                    global Operating_ID
                    Operating_ID=a 
                    if r=='EMPLOYEE':
                        root.destroy()
                        Emp_window()              
                    else:       
                        root.destroy()
                        admin()
        else:
            if len(a)==0:
                response=messagebox.showerror('Error','You left the ID field empty.')            
            elif a.isdigit()==False:
                response=messagebox.showerror('Error','Incorrect input.')

    def doj():
        date=datetime.datetime.now()
        s='select ID,DOJ from emp'
        c1.execute(s)
        p=c1.fetchall()
        day=date.strftime('%d')
        month=date.strftime('%m')
        year=date.strftime('%Y')
        date_tod=year+'-'+month+'-'+day
        for i in p:
            if str(i[1])==date_tod:
                ID=i[0]
                l='ACTIVE'
                s='update emp set Staus_at="%s" where ID=%s'%(l,ID)
                c1.execute(s)
                conn.commit()
    doj()
    label_id=Label(root,text='Employee ID:')
    label_id.place(x=10,y=100)
    e_id=Entry(root)
    e_id.place(x=90,y=100)

    label_pass=Label(root,text='Password:')
    label_pass.place(x=10,y=130)
    e_pass=Entry(root,show='*')
    e_pass.place(x=90,y=130)

    b=Button(root,text='Sumbit',command=check)
    b.place(x=90,y=170)

    mainloop()
main()
