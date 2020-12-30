import random
import pyperclip
from pyperclip import copy
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3

root = Tk()

root.title('RANDOM PASSWORD GENERATOR')
root.geometry('800x730')

tab = ttk.Notebook(root)
tab.pack()

frame1 = Frame(tab,bd=50,width=800,height=750)
frame2 = Frame(tab,bd=50,width=800,height=750)

frame1.pack(fill="both",expand=5)
frame2.pack(fill="both",expand=1)

tab.add(frame1,text="Password     ")
tab.add(frame2,text="Saved password    ")

img = ImageTk.PhotoImage(Image.open("image3.png"))
label = Label(frame1,image=img)
label.pack()

passstr= StringVar()
passstr1=StringVar()
savename = StringVar()
savecontent =StringVar()

def password():
    passstr.set("")
    def all():
        num={'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
        all={'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9','!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~'}
        all_list=list()
        for all_1 in all:
            all_list.append(all_1)

        random.shuffle(all_list)
        pa=""
        for n in range(e.get()):
            n=n+2*n+n-n+3
            pa=pa+all_list[n]
        all_list.clear()
        
        print(pa)
        passstr.set(pa)
        all_list.clear()
 
    all()
    pa=passstr
    conn=sqlite3.connect("password.sqlite")
    cur=conn.cursor()
    cur.execute('''SELECT Password FROM password''')
    row=cur.fetchall()
    for check in row:
        if pa == check:
            password()
            e2.delete(0.0,END)
            cur.close()

def copy1():
    random_password = e1.get()
    pyperclip.copy(random_password)

def save():
    top =Toplevel()
    top.iconbitmap("icon.ico")
    top.title("SAVE")
    top.geometry("400x270") 
  
    def ok():
        content=e3.get()
        random_password = e1.get()
        conn = sqlite3.connect("password.sqlite")
        cur=conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Password(id INTEGER PRIMARY KEY,Content TEXT,Password UNIQUETEXT)''')
        cur.execute('''SELECT Content FROM Password''')
        row1 =cur.fetchall()
        if str(content) in str(row1):
            messagebox.showinfo("Name error","Name has taken choose another")
            conn.commit()
            cur.close()
            top.destroy()
            save()
        
        cur.execute('''INSERT INTO Password(Content,Password) VALUES(?,?)''',(content,random_password))    
        conn.commit()
        cur.close()
        top.destroy()
        savename.set("")
        savecontent.set("")

    label4 =Label(top,text="Domain:",fg="Black", bd= 0,highlightthickness= 5)
    e3=Entry(top,textvariable=savecontent,bg="#1eb5d4",bd=5)
    save_button1 = Button(top,text="OK!",command=ok,bg="#3acbe8",activebackground='#449aab') 
    label4.place(x=100,y=100)
    e3.place(x=200,y=100)
    save_button1.place(x=170,y=150)

def submit():
    conn = sqlite3.connect("password.sqlite")
    cur=conn.cursor()
    cur.execute('''SELECT Content,Password FROM Password''')
    row=cur.fetchall()
    domain = e4.get()
    count=0
    for co in row:
        count=count+1
    final_pass=0
    for i in row:
        if str(i[0])==str(domain):
            final_pass =i[1]
            text.insert(END,"\nFound-->      ")
            text.insert(END,final_pass)
        else:
            final_pass =final_pass+1
    if final_pass>(count-1):
        text.insert(END,"\nNot found in database!! ") 
    conn.commit()
    cur.close()

def clear():
    text.delete(0.0,END)
        
label1=Label(frame1,text="Select len of pass:",fg="Black", bd= 0,highlightthickness= 5)
label1.place(x=240,y=470)
label2=Label(frame1,text="password:",fg="Black", bd= 0,highlightthickness= 5)
label2.place(x=240,y=510)

e = Scale(frame1,from_=8,to=16,orient=HORIZONTAL,bg="#1eb5d4",sliderlength=20)
e.place(x=360,y=460)
e1= Entry(frame1, textvariable=passstr,bg="#1eb5d4",bd=5)
e1.place(x=360,y=510)
generate_button= Button(frame1, text="Generate",command=password,bg="#3acbe8",activebackground='#449aab')
generate_button.place(x=240,y=570)

copy_button = Button(frame1, text="Copy", command=copy1,bg="#3acbe8",activebackground='#449aab')
copy_button.place(x=370,y=570)

save_button = Button(frame1,text="save",command=save,bg="#3acbe8",activebackground='#449aab')
save_button.place(x=450,y=570)

exit_button = Button(frame1, text="Exit", command=frame1.quit,bg="#3acbe8",activebackground='#449aab')
exit_button.place(x=370,y=610)

label5=Label(frame2,text="Enter Domain:",fg="Black", bd= 0,highlightthickness= 5)
label5.place(x=100,y=50)

e4 = Entry(frame2, textvariable=passstr1,width=30,bg="#1eb5d4",bd=5)
e4.place(x=200,y=50)

text = Text(frame2,bd=4,width=60,height=20,font=("Helvetica",12))
text.place(x=100,y=90)

submit = Button(frame2,text="Submit",command=submit,bg="#3acbe8",activebackground='#449aab')
submit.place(x=420,y=50)

clear = Button(frame2,text="Clear",command=clear,bg="#3acbe8",activebackground='#449aab')
clear.place(x=490,y=50)

frame1.mainloop()