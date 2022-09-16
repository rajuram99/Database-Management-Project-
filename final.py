import sqlite3
conn=sqlite3.connect('database.db')
print('database connected')

import tkinter as tk
top = tk.Tk()
top.title('Customer Database')

def close_window ():
    a = E1.get()
    b = E2.get()
    c = E3.get()
    d = E4.get()
    e = E5.get()
    f = E6.get()
    params = (a, b, c ,d ,e, f)

    conn.execute("INSERT INTO data VALUES (?, ?, ?, ?, ?, ? )", params)

    top.destroy()






var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()
var4 = tk.StringVar()
var5 = tk.StringVar()
var6 = tk.StringVar()


label1 = tk.Label(top, textvariable=var1, relief=tk.RAISED )
label1.pack()
E1 = tk.Entry(top, bd =5)
E1.pack()
var1.set("NAME OF THE CUSTOMER ")
E1.focus_set()

label2 = tk.Label(top, textvariable=var2, relief=tk.RAISED )
label2.pack()
E2 = tk.Entry(top, bd =5)
E2.pack()
var2.set("EMAIL OF THE CUSTOMER ")
E2.focus_set()

label3 = tk.Label(top, textvariable=var3, relief=tk.RAISED )
label3.pack()
E3 = tk.Entry(top, bd =5)
E3.pack()
var3.set("PHONE NUMBER OF THE CUSTOMER")
E3.focus_set()

label4 = tk.Label(top, textvariable=var4, relief=tk.RAISED )
label4.pack()
E4 = tk.Entry(top, bd =5)
E4.pack()
var4.set("COLLEGE OF THE CUSTOMER")
E4.focus_set()

label5 = tk.Label(top, textvariable=var5, relief=tk.RAISED )
label5.pack()
E5 = tk.Entry(top, bd =5)
E5.pack()
var5.set("BANK ACCOUNT NO. OF THE CUSTOMER")
E5.focus_set()

label6 = tk.Label(top, textvariable=var6, relief=tk.RAISED )
label6.pack()
E6 = tk.Entry(top, bd =5)
E6.pack()
var6.set("IFSC CODE OF THE CUSTOMER")
E6.focus_set()

#Create a Button to validate Entry Widget

tk.Button(top, text= "Close",width= 5, command= close_window).pack(pady=20)

conn.execute("""CREATE TABLE IF NOT EXISTS data(name text,email text, phno integer, college text,bankacno integer,
ifsc integer)""")



top.mainloop()