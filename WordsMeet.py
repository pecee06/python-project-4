import pandas as pd

credentials = pd.read_csv('credentials.csv')

from tkinter import *
from tkinter import messagebox

root = Tk()

window_height = 350
window_width = 550

root.minsize(window_width,window_height)
root.maxsize(window_width,window_height)

root.title('Login')

root.config(bg='lightgrey')

# root.wm_iconbitmap()

def basic_design(x,heading,backG,borderC,headingC):
    x.config(bg=backG)

    Label(x,
    text=heading,
    font=('High Tower Text',20),
    bg=borderC,
    fg=headingC).pack(side=TOP,fill=X)

    Label(x,
    text='',
    bg=borderC).pack(side=LEFT,fill=Y)

    Label(x,
    text='',
    bg=borderC).pack(side=RIGHT,fill=Y)

    Label(x,
    text='',
    bg=borderC).pack(side=BOTTOM,fill=X)

basic_design(root,'Enter your Credentials','#DAF7A6','#C70039','white')

F1 = Frame(root)
F1.pack(pady=25)

Label(F1,
text='Username :',
fg='crimson',
font='bold 15').grid(row=1,column=1,pady=5)

Label(F1,
text='Password :',
fg='crimson',
font='bold 15').grid(row=2,column=1,pady=5)

v1 = StringVar()
v2 = StringVar()

Entry(F1,
textvariable=v1,
font=15).grid(row=1,column=2,pady=5)

Entry(F1,
textvariable=v2,
font=15).grid(row=2,column=2,pady=5)

def create_ac():
    window = Toplevel(root)
    window.minsize(window_width,window_height)
    window.maxsize(window_width,window_height)
    window.title('Signup')
    basic_design(window,'Enter your Details','#DAF7A6','#097969','white')

    F = Frame(window)
    F.pack(pady=25)

    Label(F,
    text='Username :',
    font='bold 15',
    fg='crimson').grid(row=1,column=1,pady=5)

    Label(F,
    text='Password :',
    font='bold 15',
    fg='crimson').grid(row=2,column=1,pady=5)

    Label(F,
    text='Phone No :',
    font='bold 15',
    fg='crimson').grid(row=3,column=1,pady=5)

    V1 = StringVar()
    V2 = StringVar()
    V3 = StringVar()

    Entry(F,
    textvariable=V1,
    font=15).grid(row=1,column=2,pady=5)

    Entry(F,
    textvariable=V2,
    font=15).grid(row=2,column=2,pady=5)

    Entry(F,
    textvariable=V3,
    font=15).grid(row=3,column=2,pady=5)

    V4 = IntVar()

    Label(F,
    text='Gender :',
    font='bold 15',
    fg='crimson').grid(row=4,column=1,pady=5)

    Radiobutton(F,
    text='Male',
    variable=V4,
    value=1).grid(row=4,column=2,pady=5)

    Radiobutton(F,
    text='Female',
    variable=V4,
    value=2).grid(row=4,column=3,pady=5)

    def signup():
        u_name = V1.get()
        pwd = V2.get()
        pno = V3.get()
        sex = V4.get()

        if sex == 1:
            gender = 'M'
        elif sex == 2:
            gender = 'F'

        data = [u_name,pwd,pno,gender]
        credentials.loc[len(credentials)] = data
        credentials.to_csv('credentials.csv',index=False)

        V1.set('')
        V2.set('')
        V3.set('')

        window.destroy()

    v1.set('')
    v2.set('')

    Button(F,
    text='Signup',
    font=('High Tower Text',13),
    bg='teal',
    fg='white',
    command=signup).grid(row=5,column=4,pady=5)

def main_window():
    window = Toplevel(root)
    window.geometry('950x550')
    window.minsize(window_width,window_height)
    window.title('WordsMeet')
    basic_design(window,f'WELCOME {v1.get()}','#DAF7A6','#581845','white')

    F1 = Frame(window)
    F1.pack(side=BOTTOM,anchor=E)

    Label(F1,
    text='Write a Post',
    font='bold 15',
    fg='white',
    bg='crimson').pack(fill=X)

    textbox = Text(F1,font=15,height=15,width=50)
    textbox.pack()

    F2 = Frame(window)
    F2.pack(anchor=W)

    def post():
        user_text = textbox.get(1.0,"end-1c")    # {1.0} means from first character, {'end-1c'} means till last character without newline character
        Label(F2,
        text=f'{user_text}\n',
        font='bold 13',
        bg='#DAF7A6').pack(fill=X)

        textbox.delete(1.0,'end')

    Button(F1,
    text='Post',
    command=post,
    bg='teal',
    fg='white',
    font=('High Tower Text',13)).pack(side=BOTTOM,anchor=E,fill=X)

def login():
    u_name = v1.get()
    pwd = v2.get()

    if u_name in list(credentials['username']):
        record = credentials.loc[credentials['username']==u_name]
        Pass = record['password'].values

        if pwd == Pass[0]:
            main_window()
        else:
            messagebox.showerror('Login Error',f'Check your password {u_name}')

    else:
        messagebox.showerror('Login Error','You have entered an invalid username')
        response = messagebox.askquestion('','Signup Now')
        
        if response == 'yes':
            create_ac()
        else:
            pass
    v1.set('')
    v2.set('')

Button(F1,
text='Login',
bg='teal',
fg='white',
font=('High Tower Text',13),
command=login).grid(row=3,column=3)

Button(root,
text='Click here to Signup',
bg='#93C572',
fg='#800020',
font=('High Tower Text',15),
command=create_ac).pack(side=BOTTOM,fill=X,padx=5,pady=2)

root.mainloop()