from tkinter import *
import backend

m='row added successfully!'
n='row deleted successfully!'
o='row updated successfully!'
window=Tk()
#title for the window
window.wm_title("BookStore")


'''event which is used in binding the listbox(frontend) with backend script
passed as a second parameter, ist one is '<<ListboxSelect>>'
Function: to fetch tuple by tuple from the backend script
'''

def get_selected_row(event):
    global selected_tuple
    try:
        index=list1.curselection()[0]
        selected_tuple=list1.get(index)
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1])
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2])
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3])
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4])
    except IndexError:
        pass

#view command on VEIW ALL COMMAND BUTTON
def view_command():
    list1.delete(0,END)
    for i in backend.view():
        list1.insert(END,i)

#Search command on SEARCH Command button
def search_command():
    list1.delete(0,END)
    for i in backend.search(title_text.get().upper(),author_text.get().upper(),year_text.get().upper(),ISBN_text.get().upper()):
        list1.insert(END,i)
#ADD command on ADD Command button
def add_command():
    backend.insert(title_text.get().upper(),author_text.get().upper(),year_text.get().upper(),ISBN_text.get().upper())
    list1.delete(0,END)
    list1.insert(END,m)
#DELETE command on Delete Command button
def del_command():
    backend.delete(selected_tuple[0])
    list1.delete(0,END)
    list1.insert(END,n)
#Update command on Update Command button
def update_command():
    backend.update(selected_tuple[0],title_text.get().upper(),author_text.get().upper(),year_text.get().upper(),ISBN_text.get().upper())
    list1.delete(0,END)
    list1.insert(END,o)

#CREATING LABLES title,year,ISBN and Author on main window
l1=Label(window,text='Title')
l1.grid(row=0,column=0)

l2=Label(window,text='Author')
l2.grid(row=0,column=2)

l3=Label(window,text='Year')
l3.grid(row=1,column=0)

l4=Label(window,text='ISBN')
l4.grid(row=1,column=2)

#creating entry fields to corresponding labels
title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

author_text=StringVar()
e2=Entry(window,textvariable=author_text)
e2.grid(row=0,column=3)

year_text=StringVar()
e3=Entry(window,textvariable=year_text)
e3.grid(row=1,column=1)

ISBN_text=StringVar()
e4=Entry(window,textvariable=ISBN_text)
e4.grid(row=1,column=3)


#list_box and scrollbar

list1=Listbox(window,height=6,width=35)
list1.grid(row=2,rowspan=6,column=0,columnspan=2)

s1=Scrollbar(window)
s1.grid(row=3,column=2,rowspan=4)


#interaction between listbox and Scrollbar
list1.configure(yscrollcommand=s1.set)
s1.configure(command=list1.yview)
#binding of frontend and backend
list1.bind('<<ListboxSelect>>',get_selected_row)
#buttons for veiw,add,search,delete,update etc
b1=Button(window,text='VEIW ALL', width=12,command=view_command)
b1.grid(row=2,column=3)

b2=Button(window,text='SEARCH',width=12,command=search_command)
b2.grid(row=3,column=3)

b3=Button(window,text='ADD',width=12,command=add_command)
b3.grid(row=4,column=3)

b4=Button(window,text='UPDATE',width=12,command=update_command)
b4.grid(row=5,column=3)

b5=Button(window,text='DELETE',width=12,command=del_command)
b5.grid(row=6,column=3)

b6=Button(window,text='CLOSE',width=12,command=window.destroy)
b6.grid(row=7,column=3)


window.mainloop()
