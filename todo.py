from tkinter import *

root=Tk()
root.title=("ToDo List")
root.geometry("400x500")

#create a label
heading = Label(root,text="TASKS",bg="grey" , font="arial 25 bold")
heading.place(x=140, y=10)

#function which will help to add task , delete and edit task

def add_task():
    task_test=task.get()
    listbox.insert(END, task_test)
    task_entry.delete(0 , END)

def delete_task():
    selected_task_index = listbox.curselection()
    index = selected_task_index[0]
    listbox.delete(index)

def edit_task():
    for i in listbox.curselection():
        listbox.delete(i)
        listbox.insert(i, task_entry.get())
        task_entry.delete(0,END)

#main
frame=Frame(root, width=400 ,height=300, bg="#F0F0F0")
frame.place(x=0 ,y=120)

task=StringVar()
task_entry=Entry(frame, width=18, font="arial 20", bd=0, textvariable=task)
task_entry.pack(pady=10)

#box 
listbox=Listbox(frame, width=35, height=10 , bg="grey" , font="arial 15" , fg="white" ,selectbackground="#F0F0F0")
listbox.pack(pady=20 , padx=0)

#add task
btn1 = Button(frame , text="ADD", font="arial 20" ,bg="#008000", command=add_task)
btn1.pack(pady=10)


#delete button
btn2=Button(root, text="Delete" , font="arial 20" ,bg="red" , fg="white" ,bd=0, command=delete_task)
btn2.place(x=250 , y=450)

#edit button
btn3=Button(root, text="edit" , font="arial 20" , bg="blue", fg="white", bd=0 ,command=edit_task)
btn3.place(x=60 , y=450)

#this function will help to select the task in the listbox
def selection(event):
    selected_item= listbox.get(listbox.curselection())
    task_entry.delete(0, END)
    task_entry.insert(0 , selected_item)

listbox.bind('<<ListboxSelect>>',selection)
root.mainloop()