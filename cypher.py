from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password =code.get()

    if password == "1234":
        screen2 = Toplevel(screen)
        screen2.title("encryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        decrypt = base64_bytes.decode("ascii")

        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y=0)
        text2 = Text(screen2, font="Robote 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, decrypt)

    elif password == "":
        messagebox.showerror("decryption", "input password")
    elif password != "1234":
        messagebox.showerror("decryption", "Invalid password")


def encrypt():
    password = code.get()

    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message = text1.get(1.0,END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        encrypt = base64_bytes.decode("ascii")

        Label(screen1,text= "ECRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2 = Text(screen1,font = "Robote 10",bg="white",relief=GROOVE,wrap = WORD,bd=0)
        text2.place(x=10, y=40, width=380, height=150)

        text2.insert(END, encrypt)

    elif password == "":
        messagebox.showerror("encryption","input password")
    elif password != "1234":
        messagebox.showerror("encryption","Invalid password")




def mainscreen():
    global text1
    global code
    global screen

    screen = Tk()
    screen.geometry("375x398")


    screen.title("pythonApp")

    def reset():
        code.set("")
        text1.delete(1.0,END)

    Label(text="Enter the message here to encrypt it:", fg ="black" ,font=("calbri",13)).place(x=10, y=10)
    text1 = Text(font= "Robote 14",bg="white",relief =GROOVE, wrap=WORD,bd=0)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter the security code:", fg="black", font=("calbri", 13)).place(x=10, y=170)

    code = StringVar()
    Entry(textvariable=code,width = 19,bd=0,font=("airal",25),show="*").place(x=10,y=200)
    Button(text="ENCRYPT", height="2",width="23",bg="red",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT", height="2",width="23",bg="green",fg="white",bd=0,command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2", width="50", bg="blue", fg="white", bd=0,command=reset).place(x=10, y=300)




    screen.mainloop()

mainscreen()

