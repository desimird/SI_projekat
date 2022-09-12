
import tkinter as tk
from fpdf import FPDF
import time 
import csv



import csv_functions as cf
import classes as cls




global start_time
HEIGHT = 500
WIDTH = 600


def end_call():
    end = time.time()
    min = start_time - end
    res = user_phone.calling(min)
    if res == 0:
        root3 = tk.Tk()

        label = tk.Button(root3,text="Nemate dovoljno kredita za ovu akciju.")
        label.pack()

        root3.mainloop()

    enrty000.delete(0,tk.END)
    

def call():
    global start_time
    start_time = time.time()



def send_smss():
    res = user_phone.send_sms()
    if res == 0:
        root3 = tk.Tk()

        label = tk.Button(root3,text="Nemate dovoljno kredita za ovu akciju.")
        label.pack()
    
        root3.mainloop()
    enrty11.delete(0,tk.END)
    enrty10.delete(0,tk.END)
    

def check_balances():
    res = user_phone.check_balance()
    root3 = tk.Tk()

    
    label = tk.Label(root3,text=res,font=40)
    label.place(relx=0.5,rely=0.1)
    label1 = tk.Label(root3, text='Stanje kredita na vasem broju je: ',font=40)
    label1.place(relx=0.1,rely=0.1)

    
    root3.mainloop()

def print_recipe():
    res = user_phone.print_pdf()
    if res:
        root3 = tk.Tk()

        label = tk.Button(root3,text='Vas racun se nalazi u folderu pod nazivom "racun.pdf"')
        label.pack()
        
        root3.mainloop()
    else:
        root3 = tk.Tk()

        label = tk.Button(root3,text='Ova mogucnosti je moguca samo za postpejd korisnike."')
        label.pack()
        
        root3.mainloop()

def login_check():

    phone_num = phone_no.get()
    passwo = password.get()
    header, rows = cf.get_data_from_csv()
    for row in rows:
        if ((row[2]==phone_num)and(row[-1]==passwo)):
            root1.destroy()
            main_screen()
            break
    
    entry00.delete(0,tk.END)
    entry01.delete(0,tk.END)
    root1.destroy()

    root2 = tk.Tk()

    label = tk.Label(root2,text="Netacni podaci! Pokusajte ponovo")
    label.pack()
    
    root2.mainloop()

    login_screen()
            
def login_screen():
    global root1

    root1 = tk.Tk()

    global phone_no
    global password
    global entry00
    global entry01

    phone_no = tk.StringVar()
    password = tk.StringVar()

    canvas = tk.Canvas(root1, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame0 = tk.Frame(canvas, bg='#80c1ff')
    frame0.place(relx=0.1,rely=0.1,relheight= 0.8,relwidth=0.8)

    label00 = tk.Label(frame0, text= 'Broj telefona:', bg='#80c1ff', font=40)
    label00.place(relx=0.1,rely=0.1,relheight=0.25,relwidth= 0.4)

    entry00 = tk.Entry(frame0, font = 40,textvariable= phone_no)
    entry00.place(relx=0.55,rely= 0.17, relheight=0.1, relwidth=0.4)

    label01 = tk.Label(frame0, text= 'Lozinka:', bg='#80c1ff', font=40)
    label01.place(relx=0.1,rely=0.4,relheight=0.25,relwidth= 0.4)

    entry01 = tk.Entry(frame0, font = 40,show='*',textvariable=password)
    entry01.place(relx=0.55,rely= 0.47, relheight=0.1, relwidth=0.4)

    button00 = tk.Button(frame0, text='Login',font=40, command= login_check)
    button00.place(relx=0.45,rely=0.7)

    root1.mainloop()

def main_screen():
    
    global enrty000
    global entry011
    global enrty11
    global enrty10
    global user
    global user_phone
    user = cls.User(phone_no.get())
    user_phone = cls.Phone(user.phone_no)



    root = tk.Tk()

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    frame0 = tk.Frame(root, bg='#80c1ff')
    frame0.place(relx= 0.1, rely= 0.1, relwidth=0.8, relheight= 0.15)

    label00 = tk.Label(frame0, text = 'Unesite broj telefona', bg='#80c1ff',font=40)
    label00.place(relx=0.02,rely=0.05,relheight=0.7,relwidth=0.33)

    entry011 = tk.Label(frame0, bg='#80c1ff',font=30)
    entry011.place(relx=0.35,rely=0.7,relheight=0.2,relwidth=0.33)

    enrty000 = tk.Entry(frame0,font=40)
    enrty000.place(relx=0.35,rely=0.2,relheight=0.4,relwidth=0.33)

    button00 = tk.Button(frame0, text = 'Pozovi', bg = 'white',command= call)
    button00.place(relx=0.69,rely=0.1,relheight=0.4,relwidth=0.30)

    button01 = tk.Button(frame0, text = 'Zavrsi poziv', bg = 'white',command= end_call)
    button01.place(relx=0.69,rely=0.55,relheight=0.4,relwidth=0.30)

    frame1 = tk.Frame(root, bg='#80c1ff')
    frame1.place(relx= 0.1, rely= 0.3, relwidth=0.8, relheight= 0.20)

    label10 = tk.Label(frame1, text='Unesite broj telefona', bg='#80c1ff',font=40)
    label10.place(relx=0.02,rely=0.1,relheight=0.25,relwidth=0.33)

    enrty10 = tk.Entry(frame1,font=40)
    enrty10.place(relx=0.02,rely=0.35,relheight=0.25,relwidth=0.33)

    button10 = tk.Button(frame1,text = 'Posalji poruku', command= send_smss)
    button10.place(relx=0.02,rely=0.65,relheight=0.25,relwidth=0.33)

    label11 = tk.Label(frame1, text='Tekst poruke:', bg='#80c1ff',font=25)
    label11.place(relx=0.35,rely=0.05,relheight=0.2,relwidth=0.33)

    enrty11 = tk.Entry(frame1,font=40)
    enrty11.place(relx=0.4,rely=0.3,relheight=0.55,relwidth=0.55)

    frame2 = tk.Frame(root, bg='#80c1ff')
    frame2.place(relx=0.1, rely=0.55, relheight= 0.25, relwidth= 0.4)

    label20 = tk.Label(frame2, text= 'Vas broj telefona:',bg='#80c1ff' )
    label20.place(relx=0.05,rely=0.1,relheight=0.33)
    label22 = tk.Label(frame2, text= user.phone_no ,bg='#80c1ff' )
    label22.place(relx=0.5,rely=0.1,relheight=0.33)

    label21 = tk.Label(frame2, text= 'Tip predplate:',bg='#80c1ff' )
    label21.place(relx=0.05,rely=0.35,relheight=0.33)
    label23 = tk.Label(frame2, text= 'Pripejd' if int(user_phone.type)==0 else 'Postpejd' ,bg='#80c1ff' )
    label23.place(relx=0.5,rely=0.35,relheight=0.33)

    button20 = tk.Button(frame2,text='Stampaj racun',command=print_recipe)
    button20.place(relx=0.09,rely= 0.7, relheight=0.25, relwidth= 0.4)

    button20 = tk.Button(frame2,text='Stanje kredita',command=check_balances)
    button20.place(relx=0.51,rely= 0.7, relheight=0.25, relwidth= 0.4)

   

    root.mainloop()


login_screen()
