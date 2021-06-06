# coding: UTF-8

from  tkinter import*
from tkinter import ttk
from tkinter.filedialog import *
import os
from setting import*
import time
import getpass
from tkinter.messagebox import*
from tkinter.font import Font
import subprocess

workspace = f'C:\\Users\\{getpass.getuser()}\\Documents\\'

global filesaved
filesaved = ''
global file_saved
file_saved = False

app = Tk()
app.title(" PYIDE V1 ")
w, h = app.winfo_screenwidth(), app.winfo_screenheight()

app.geometry("%dx%d+0+0" % (w, h))
app.iconbitmap('icone.ico')

global font_size
font_size = 18

background_color = bg
forground_color = fg
larg_cons = 400
larg_entry = w-larg_cons

console = Frame(app,width=larg_cons,height=h,bg="#000021")
console.propagate(0)
console.pack(side='right')

wel = Label(console,text='PYIDE V1',bg='#00B9AB', fg='#fff', font=("Arial", font_size))
wel.pack(fill='x')

entree = StringVar()
entree = Text(app, width=larg_entry, height=h,bg=background_color, fg=forground_color, font=("Monospace", font_size))
entree.config(insertbackground="#fff")
entree.pack(side='left')
entree.focus()

def get_user_entry():
    return entree.get('1.0', END)

def font_plus(event):
    global font_size
    font_size = font_size+1
    entree.config(font=('None',font_size))

def font_moins(event):
    global font_size
    font_size = font_size-1
    entree.config(font=('None',font_size))

entree.bind('<Control-space>',font_plus)
entree.bind('<Control-p>',font_moins)

def save_file(event):
    global file_saved
    global filesaved
    user = entree.get('1.0', END)
    if file_saved is True:
        sf = open(filesaved,'w')
        sf.write(user)
        sf.close()
    else:
        flot = asksaveasfilename(title="Enregistrer",filetypes=[('script python','.py'),('all files','.*')])
        try:
            file = open(flot+'.py', "w")
            file.write(user)
            file.close()
            title_open = os.path.basename(flot)
            app.title(f"PYIDE : [{title_open}]")
            file_saved = True
            filesaved = file.name
        except FileNotFoundError:
            showwarning("ERROR","File Not Found Error")


def open_file(event):
    global file_saved
    global filesaved
    flit = askopenfilename(title="Ouvrir un fichier", filetypes=[('script python','.py'),('all files','.*')])
    file = open(flit, "r")
    filesaved = file.name
    lire = file.read()
    entree.delete('1.0', END)
    entree.insert(INSERT, lire)
    title_open = os.path.basename(flit)
    app.title(f"PYIDE : [{title_open}]")
    file.close()
    file_saved = True


app.bind("<Control-s>", save_file)
app.bind("<Control-o>", open_file)

def clear_consol():
    for child in console.winfo_children():
        child.destroy()
    wel = Label(console,text='PYIDE V1 (ready)',bg='#00B9AB', fg='#fff', font=("Arial", font_size))
    wel.pack(fill='x')

def run_(event):
    
    if file_saved is False:
        save_file(event)
    elif filesaved == '':
        pass
    else:
        fs = '"' + filesaved + '"'
        cmd = f'python {fs}'
        out = subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.STDOUT,shell=True)
        stdout,stderr = out.communicate()
        result = stdout.decode('utf-8')
        clear_consol()
        ot = Label(console,text=result,bg='#000021', fg='#fff', font=("Arial", font_size),wraplength=305,justify="left")
        ot.pack(side='left',anchor='n')

app.bind("<Control-r>", run_)


app.mainloop()

