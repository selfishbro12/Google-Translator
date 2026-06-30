from tkinter import *
from tkinter import Tk,ttk
from googletrans import Translator,LANGUAGES
import asyncio


def change(text,src='english',dest='Hindi'):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1= asyncio.run(trans.translate(text,src=src1,dest=dest1))
    return trans1

def data():                      #for getting the data
    s=comb_sou.get()
    d=comb_des.get()
    msg=sor_txt.get(1.0,END)
    textget=change(text=msg,src=s,dest=d)
    des_txt.delete(1.0,END)
    des_txt.insert(END,textget) 
 
root=Tk()
root.title('google translator')
root.geometry('500x400')
root.config(bg='yellow')

label_txt=Label(root,text='google translator',font=('Times New Roman',20,'bold'),bg='yellow')
label_txt.place(x=150,y=30,height=30,width=200)

sor_txt=Label(root,text='source:--',font=('Times New Roman',20,'bold'),bg='yellow')
sor_txt.place(x=-30,y=110,height=30,width=200)

frame=Frame(root).pack(side=BOTTOM)
sor_txt=Text(frame,font=('Times New Roman',10,'bold'),wrap=WORD)           # making source txt value 
sor_txt.place(x=128,y=80,height=100,width=250)

list_txt=list(LANGUAGES.values())                                 
comb_sou=ttk.Combobox(frame,values=list_txt)
comb_sou.place(x=128,y=200,height=25,width=80)
comb_sou.set('english')

button=Button(frame,text='translate',relief=RAISED,command=data)
button.place(x=214,y=199,height=25,width=80)

comb_des=ttk.Combobox(frame,values=list_txt)
comb_des.place(x=304,y=199,height=25,width=70)
comb_des.set('english')

des_txt=Label(root,text='destin:--',font=('Times New Roman',20,'bold'),bg='yellow')
des_txt.place(x=-30,y=270,height=30,width=200)
des_txt=Text(frame,font=('Times New Roman',9,'bold'),wrap=WORD)          
des_txt.place(x=128,y=240,height=100,width=250)

root.mainloop()
