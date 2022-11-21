import tkinter
from tkinter import *

root=Tk()
root.title("To Do List")
root.geometry("400x650+400+100")

root.resizable(False,False)

task_list=[]



def openTaskFile():
    
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
             tasks=  taskfile.readlines()
        for task in tasks:
            if(task!='\n'):
                task_list.append(task)
                listbox.insert(END,task) 
    except:
        file=open('tasklist.txt','w')
        file.close()
#icon 
Image_icon=PhotoImage(file="task.png")
root.iconphoto(False,Image_icon)

#top bar 
TopImage=PhotoImage(file="topbar.png")
Label(root,image=TopImage).pack()

dockImage=PhotoImage(file="dock.png")
Label(root,image=dockImage,bg="#32405b").place(x=30,y=25)

noteImage=PhotoImage(file="task.png")
Label(root,image=noteImage,bg="#32405b").place(x=30,y=25)


heading=Label(root,text="All Task",font=("arial 20 bold"),fg="white",bg="#32405b")
heading.place(x=130,y=20)

#main 
frame=Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=180)


task=StringVar()
task_entry=Entry(frame,width=18,font="arial 20",bd=0)
task_entry.place(x=10,y=7)


def add_task():
    task=task_entry.get()
    task_entry.delete(0,END)
    if(task):
        with open("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
            task_list.append(task)
            listbox.insert(END,task)

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#5a95ff",command=add_task)
button.place(x=300,y=0)


#listbox 
frame1=Frame(root,bd=3,width=700,height=280,bg="#32405b")
frame1.pack(pady=(160))

listbox=Listbox(frame1,font=("arial",12),width=40,height=16,bg="#32405b",fg="white")
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack( side=RIGHT,fill=BOTH)

#listbox.config(yscrollcommand=scrollbar.set)
#scrollbar.config(command=listbox.yview)


#delete 

Delete_icon=PhotoImage(file="delete.png")
def delete_task():
    global task_list
    task=str(listbox.get(ANCHOR))
    print("task is ",task)
    if task in task_list:
        task_list.remove(task)
        with open("tasklist.txt",'w') as taskfie:
            for task in task_list:
                task_fie.write(task+"\n ")
        listbox.delete(ANCHOR)
Button(root,command=delete_task,image=Delete_icon,bd=0).place(x=180,y=550)


openTaskFile()
root.mainloop()