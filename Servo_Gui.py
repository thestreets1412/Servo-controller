from tkinter import *
from tkinter import simpledialog,messagebox,ttk
import sqlite3
from scrolltable import *

window=Tk()
window.geometry('665x695')
window.title('Servo controller 6 DOF')
window.resizable(0,0)

con = sqlite3.connect('Config_servo.db')
cur = con.cursor()

menu_bar=Menu()
window.config(menu=menu_bar)
menu_file=Menu(menu_bar,tearoff=False)
menu_bar.add_cascade(menu=menu_file,label='Setting')
for k in range(1,7):
    menu_file.add_command(label=f'Servo#{k}',command=lambda id=k:set_max_min(id))
max1=180;max2=180;max3=180;max4=180;max5=180;max6=180
Maximum=[max1,max2,max3,max4,max5,max6,]
min1=0;min2=0;min3=0;min4=0;min5=0;min6=0
Minimum=[min1,min2,min3,min4,min5,min6]
for i in range(0,len(Maximum)):
    sql = f'SELECT max FROM Set_max_min WHERE ID={i+1}'
    cur.execute(sql)
    rows = cur.fetchall()
    Maximum[i]=rows[0][0]
for i in range(0,len(Minimum)):
    sql = f'SELECT min FROM Set_max_min WHERE ID={i+1}'
    cur.execute(sql)
    rows = cur.fetchall()
    Minimum[i]=rows[0][0]

notebook=ttk.Notebook(window,width=650,height=660)
tab_controll=Frame(notebook)
tab_data=Frame(notebook)
notebook.add(tab_controll,text='Controller')
notebook.add(tab_data,text='Data')
notebook.pack(anchor=CENTER,expand=YES)


#Servo1
fm1=LabelFrame(tab_controll,text='Servo 1')
fm1.grid(row=0,column=0,padx=10,pady=5)
Label(fm1,text='Current angle (degree):').grid(row=0,column=0,padx=5,pady=5,sticky=E)
tx1=Text(fm1,width=10,height=1,bg='powderblue')
tx1.grid(row=0,column=1,padx=5,pady=5)
tx1.bind('<Key>',lambda e: 'break')
Button(fm1,text='Set Pin',command=lambda id=1:set_pin(id)).grid(row=0,column=2,padx=5,pady=5)
Label(fm1,text='Force Servo motor:').grid(row=1,column=0,padx=5,pady=5,sticky=E)
ent1=Entry(fm1,width=10)
ent1.grid(row=1,column=1,padx=5,pady=5,sticky=W+E)
Button(fm1,text='Go',command=lambda id=1:fc_go(id)).grid(row=1,column=2,padx=5,pady=5,sticky=W+E)
scale_horz_sv1=Scale(fm1,from_=Minimum[0],to=Maximum[0],resolution=1,showvalue=FALSE,orient=HORIZONTAL,tickinterval=((Maximum[0]+Minimum[0])*0.5)//4.5,
                 length=285,command=lambda *a:scale_sv1(*a))
scale_horz_sv1.grid(row=2,column=0,padx=5,pady=5,columnspan=3,sticky=S+E)
Button(fm1,text='Set Home',command=lambda id=1:set_home(id)).grid(row=3,column=0,padx=5,pady=2,sticky=W+E,columnspan=3)
Button(fm1,text='Go Home',command=lambda id=1:go_home(id)).grid(row=4,column=0,padx=5,pady=5,sticky=W+E,columnspan=3)

#Servo2
fm2=LabelFrame(tab_controll,text='Servo 2')
fm2.grid(row=1,column=0,padx=10,pady=5)
Label(fm2,text='Current angle (degree):').grid(row=0,column=0,padx=5,pady=5,sticky=E)
tx2=Text(fm2,width=10,height=1,bg='powderblue')
tx2.grid(row=0,column=1,padx=5,pady=5)
tx2.bind('<Key>',lambda e: 'break')
Button(fm2,text='Set Pin',command=lambda id=2:set_pin(id)).grid(row=0,column=2,padx=5,pady=5)
Label(fm2,text='Force Servo motor:').grid(row=1,column=0,padx=5,pady=5,sticky=E)
ent2=Entry(fm2,width=10)
ent2.grid(row=1,column=1,padx=5,pady=5,sticky=W+E)
Button(fm2,text='Go',command=lambda id=2:fc_go(id)).grid(row=1,column=2,padx=5,pady=5,sticky=W+E)
scale_horz_sv2=Scale(fm2,from_=Minimum[1],to=Maximum[1],resolution=1,showvalue=FALSE,orient=HORIZONTAL,tickinterval=((Maximum[1]+Minimum[1])*0.5)//4.5,
                 length=285,command=lambda *a:scale_sv2(*a))
scale_horz_sv2.grid(row=2,column=0,padx=5,pady=5,columnspan=3,sticky=S+E)
Button(fm2,text='Set Home',command=lambda id=2:set_home(id)).grid(row=3,column=0,padx=5,pady=2,sticky=W+E,columnspan=3)
Button(fm2,text='Go Home',command=lambda id=2:go_home(id)).grid(row=4,column=0,padx=5,pady=5,sticky=W+E,columnspan=3)

#Servo3
fm3=LabelFrame(tab_controll,text='Servo 3')
fm3.grid(row=2,column=0,padx=10,pady=5)
Label(fm3,text='Current angle (degree):').grid(row=0,column=0,padx=5,pady=5,sticky=E)
tx3=Text(fm3,width=10,height=1,bg='powderblue')
tx3.grid(row=0,column=1,padx=5,pady=5)
tx3.bind('<Key>',lambda e: 'break')
Button(fm3,text='Set Pin',command=lambda id=3:set_pin(id)).grid(row=0,column=2,padx=5,pady=5)
Label(fm3,text='Force Servo motor:').grid(row=1,column=0,padx=5,pady=5,sticky=E)
ent3=Entry(fm3,width=10)
ent3.grid(row=1,column=1,padx=5,pady=5,sticky=W+E)
Button(fm3,text='Go',command=lambda id=3:fc_go(id)).grid(row=1,column=2,padx=5,pady=5,sticky=W+E)
scale_horz_sv3=Scale(fm3,from_=Minimum[2],to=Maximum[2],resolution=1,showvalue=FALSE,orient=HORIZONTAL,tickinterval=((Maximum[2]+Minimum[2])*0.5)//4.5,
                 length=285,command=lambda *a:scale_sv3(*a))
scale_horz_sv3.grid(row=2,column=0,padx=5,pady=5,columnspan=3,sticky=S+E)
Button(fm3,text='Set Home',command=lambda id=3:set_home(id)).grid(row=3,column=0,padx=5,pady=2,sticky=W+E,columnspan=3)
Button(fm3,text='Go Home',command=lambda id=3:go_home(id)).grid(row=4,column=0,padx=5,pady=5,sticky=W+E,columnspan=3)

#Servo4
fm4=LabelFrame(tab_controll,text='Servo 4')
fm4.grid(row=0,column=1,padx=10,pady=5)
Label(fm4,text='Current angle (degree):').grid(row=0,column=0,padx=5,pady=5,sticky=E)
tx4=Text(fm4,width=10,height=1,bg='powderblue')
tx4.grid(row=0,column=1,padx=5,pady=5)
tx4.bind('<Key>',lambda e: 'break')
Button(fm4,text='Set Pin',command=lambda id=4:set_pin(id)).grid(row=0,column=2,padx=5,pady=5)
Label(fm4,text='Force Servo motor:').grid(row=1,column=0,padx=5,pady=5,sticky=E)
ent4=Entry(fm4,width=10)
ent4.grid(row=1,column=1,padx=5,pady=5,sticky=W+E)
Button(fm4,text='Go',command=lambda id=4:fc_go(id)).grid(row=1,column=2,padx=5,pady=5,sticky=W+E)
scale_horz_sv4=Scale(fm4,from_=Minimum[3],to=Maximum[3],resolution=1,showvalue=FALSE,orient=HORIZONTAL,tickinterval=((Maximum[3]+Minimum[3])*0.5)//4.5,
                 length=285,command=lambda *a:scale_sv4(*a))
scale_horz_sv4.grid(row=2,column=0,padx=5,pady=5,columnspan=3,sticky=S+E)
Button(fm4,text='Set Home',command=lambda id=4:set_home(id)).grid(row=3,column=0,padx=5,pady=2,sticky=W+E,columnspan=3)
Button(fm4,text='Go Home',command=lambda id=4:go_home(id)).grid(row=4,column=0,padx=5,pady=5,sticky=W+E,columnspan=3)

#Servo5
fm5=LabelFrame(tab_controll,text='Servo 5')
fm5.grid(row=1,column=1,padx=10,pady=5)
Label(fm5,text='Current angle (degree):').grid(row=0,column=0,padx=5,pady=5,sticky=E)
tx5=Text(fm5,width=10,height=1,bg='powderblue')
tx5.grid(row=0,column=1,padx=5,pady=5)
tx5.bind('<Key>',lambda e: 'break')
Button(fm5,text='Set Pin',command=lambda id=5:set_pin(id)).grid(row=0,column=2,padx=5,pady=5)
Label(fm5,text='Force Servo motor:').grid(row=1,column=0,padx=5,pady=5,sticky=E)
ent5=Entry(fm5,width=10)
ent5.grid(row=1,column=1,padx=5,pady=5,sticky=W+E)
Button(fm5,text='Go',command=lambda id=5:fc_go(id)).grid(row=1,column=2,padx=5,pady=5,sticky=W+E)
scale_horz_sv5=Scale(fm5,from_=Minimum[4],to=Maximum[4],resolution=1,showvalue=FALSE,orient=HORIZONTAL,tickinterval=((Maximum[4]+Minimum[4])*0.5)//4.5,
                 length=285,command=lambda *a:scale_sv5(*a))
scale_horz_sv5.grid(row=2,column=0,padx=5,pady=5,columnspan=3,sticky=S+E)
Button(fm5,text='Set Home',command=lambda id=5:set_home(id)).grid(row=3,column=0,padx=5,pady=2,sticky=W+E,columnspan=3)
Button(fm5,text='Go Home',command=lambda id=5:go_home(id)).grid(row=4,column=0,padx=5,pady=5,sticky=W+E,columnspan=3)

#Servo6
fm6=LabelFrame(tab_controll,text='Servo 6')
fm6.grid(row=2,column=1,padx=10,pady=5)
Label(fm6,text='Current angle (degree):').grid(row=0,column=0,padx=5,pady=5,sticky=E)
tx6=Text(fm6,width=10,height=1,bg='powderblue')
tx6.grid(row=0,column=1,padx=5,pady=5)
tx6.bind('<Key>',lambda e: 'break')
Button(fm6,text='Set Pin',command=lambda id=6:set_pin(id)).grid(row=0,column=2,padx=5,pady=5)
Label(fm6,text='Force Servo motor:').grid(row=1,column=0,padx=5,pady=5,sticky=E)
ent6=Entry(fm6,width=10)
ent6.grid(row=1,column=1,padx=5,pady=5,sticky=W+E)
Button(fm6,text='Go',command=lambda id=6:fc_go(id)).grid(row=1,column=2,padx=5,pady=5,sticky=W+E)
scale_horz_sv6=Scale(fm6,from_=Minimum[5],to=Maximum[5],resolution=1,showvalue=FALSE,orient=HORIZONTAL,tickinterval=((Maximum[5]+Minimum[5])*0.5)//4.5,
                 length=285,command=lambda *a:scale_sv6(*a))
scale_horz_sv6.grid(row=2,column=0,padx=5,pady=5,columnspan=3,sticky=S+E)
Button(fm6,text='Set Home',command=lambda id=6:set_home(id)).grid(row=3,column=0,padx=5,pady=2,sticky=W+E,columnspan=3)
Button(fm6,text='Go Home',command=lambda id=6:go_home(id)).grid(row=4,column=0,padx=5,pady=5,sticky=W+E,columnspan=3)

#Table
table_pin=None;table_home=None;table_max_min=None
def show_table():
    # Table_pin
    global table_pin
    if isinstance(table_pin, TableView):
        table_pin.destroy()
    sql = 'SELECT * FROM Set_pin'
    cur.execute(sql)
    rows = cur.fetchall()
    hd = ['ID', 'Name', 'GPIO']
    wd = [5, 15, 15]
    alt = ['#ddeeff', '#ffffff']
    table_pin = TableView(tab_data, height=200, headers=hd, header_bg='navy', header_fg='white',
                          header_font='tahoma 10 bold',
                          alternate_colors=alt, column_widths=wd, cell_font='tahoma 10')
    table_pin.grid(row=0, column=0, padx=5, pady=20)
    table_pin.setdata(rows)

    # Table_Home
    global table_home
    if isinstance(table_home, TableView):
        table_home.destroy()
    sql = 'SELECT * FROM Set_Home'
    cur.execute(sql)
    rows = cur.fetchall()
    hd = ['ID', 'Name', 'Home angle']
    wd = [5, 15, 15]
    alt = ['#ddeeff', '#ffffff']
    table_home = TableView(tab_data, height=200, headers=hd, header_bg='navy', header_fg='white',
                           header_font='tahoma 10 bold',
                           alternate_colors=alt, column_widths=wd, cell_font='tahoma 10')
    table_home.grid(row=0, column=1, padx=5, pady=20)
    table_home.setdata(rows)

    # Table_Max_Min
    global table_max_min
    if isinstance(table_max_min, TableView):
        table_max_min.destroy()
    sql = 'SELECT * FROM Set_max_min'
    cur.execute(sql)
    rows = cur.fetchall()
    hd = ['ID', 'Name', 'Max angle','Min angle']
    wd = [5, 15, 15,15]
    alt = ['#ddeeff', '#ffffff']
    table_home = TableView(tab_data, height=200, headers=hd, header_bg='navy', header_fg='white',
                           header_font='tahoma 10 bold',
                           alternate_colors=alt, column_widths=wd, cell_font='tahoma 10')
    table_home.grid(row=1, column=0, padx=5, pady=20,columnspan=2)
    table_home.setdata(rows)
show_table()

#Botton refresh data
Button(tab_data,text='Refresh',command=show_table).grid(row=2,column=0,padx=5,pady=5,columnspan=2,sticky=W+E)

#=======================================================================================================================
#Design function
def scale_sv1(*a):
    tx1.delete(1.0,END)
    tx1.insert(1.0,scale_horz_sv1.get())
def scale_sv2(*a):
    tx2.delete(1.0,END)
    tx2.insert(1.0,scale_horz_sv2.get())
def scale_sv3(*a):
    tx3.delete(1.0,END)
    tx3.insert(1.0,scale_horz_sv3.get())
def scale_sv4(*a):
    tx4.delete(1.0,END)
    tx4.insert(1.0,scale_horz_sv4.get())
def scale_sv5(*a):
    tx5.delete(1.0,END)
    tx5.insert(1.0,scale_horz_sv5.get())
def scale_sv6(*a):
    tx6.delete(1.0,END)
    tx6.insert(1.0,scale_horz_sv6.get())
def set_home(id):
    tx=[tx1,tx2,tx3,tx4,tx5,tx6]
    home=tx[id-1].get(1.0,END)
    sql = '''UPDATE Set_Home SET Home_angle=? WHERE ID=?'''
    cur.execute(sql, [home,id])
    con.commit()
    messagebox.showinfo('Success', 'Data saved')
    show_table()
def set_pin(id):
    sv_pin = simpledialog.askinteger(f'Set pin of Servo #{id}', 'Indicate GPIO')
    sql = '''UPDATE Set_pin SET GPIO=? WHERE ID=?'''
    r = cur.execute(sql, [sv_pin,id])
    if r.rowcount == 1:
        con.commit()
        if sv_pin == None:
            messagebox.showinfo('Success', f'Pin{id}=None')
        else:
            messagebox.showinfo('Success', 'Data saved')
    else:
        messagebox.showerror('Error', 'Data didn\'t save')
    show_table()
def fc_go(id):
    try:
        tx = [tx1, tx2, tx3, tx4, tx5, tx6]
        ent = [ent1, ent2, ent3, ent4, ent5, ent6]
        scale_horz_sv=[scale_horz_sv1,scale_horz_sv2,scale_horz_sv3,scale_horz_sv4,scale_horz_sv5,scale_horz_sv6]
        global Minimum,Maximum
        tx[id-1].delete(1.0,END)
        if int(ent[id-1].get())>=Minimum[id-1] and int(ent[id-1].get())<=Maximum[id-1]:
            tx[id-1].insert(1.0,ent[id-1].get())
            messagebox.showinfo('Force servo',f'Servo{id} reached')
            scale_horz_sv[id-1].set(int(ent[id-1].get()))
            ent[id-1].delete(0, END)
        else:
            messagebox.showerror('Force servo',f'Angle must be between {Minimum[id-1]} and {Maximum[id-1]} degree.')
            ent[id - 1].delete(0, END)
            return
    except:
        messagebox.showerror('Force servo', 'Error')
def go_home(id):
    sql = f'SELECT Home_angle FROM Set_Home WHERE ID={id}'
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows[0][0])
    messagebox.showinfo('Home','Reached home position.')
def set_max_min(id):
    global Minimum,Maximum
    scale_horz_sv = [scale_horz_sv1, scale_horz_sv2, scale_horz_sv3, scale_horz_sv4, scale_horz_sv5, scale_horz_sv6]
    min = simpledialog.askinteger(f'Set min of Servo #{id}', 'Indicate minimum of angle')
    max = simpledialog.askinteger(f'Set max of Servo #{id}', 'Indicate maximum of angle')
    if min>=max:
        messagebox.showerror('Error', 'Max must greater than min.')
        return
    else:
        sql = '''UPDATE Set_max_min SET max=?,min=? WHERE ID=?'''
        cur.execute(sql, [max,min, id])
        con.commit()
        ava=(max+min)/2
        scale_horz_sv[id-1].config(from_=min,to=max,tickinterval=ava//4.5)
        show_table()
mainloop()