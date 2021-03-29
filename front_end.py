#importing all methods and objects for direct use from tkinter module
from tkinter import *

#importing backend script 
import back_end

#creating methods to link frontend with backend

#get_selected_row method operates when someone clicks on a row in list
#the selected row's data is shown in entry widgets
#we get the selected row data in selected_tuple which is globally available 
def get_selected_row(event):
  try:
     global selected_tuple
     index=lst.curselection()[0]
     selected_tuple=lst.get(index)
     e1.delete(0,END)
     e1.insert(END,selected_tuple[1])
     e2.delete(0,END)
     e2.insert(END,selected_tuple[2])
     e3.delete(0,END)
     e3.insert(END, selected_tuple[3])
     e4.delete(0,END)
     e4.insert(END, selected_tuple[4])
  except IndexError:
    pass
  

def view_command():
  lst.delete(0,END)
  for row in back_end.view():
    lst.insert(END,row)

def search_command():
  lst.delete(0,END)
  for row in back_end.search(title_entry.get(),author_entry.get(), year_entry.get(), isbn_entry.get()):
      lst.insert(END,row)

def add_command():
  back_end.insert(title_entry.get(),author_entry.get(), year_entry.get(), isbn_entry.get())
  lst.delete(0,END)
  lst.insert(END,(title_entry.get(),author_entry.get(), year_entry.get(), isbn_entry.get()))

def delete_command():  
  back_end.delete(selected_tuple[0])
  e1.delete(0,END)
  e2.delete(0,END)
  e3.delete(0,END)
  e4.delete(0,END)

def update_command():
  back_end.update(selected_tuple[0], title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())


#creating main window
window=Tk()
window.wm_title("Book Store")

#creating labels
l1=Label(window,text="Title")
l1.grid(row=0, column=0)
l2=Label(window,text="Author")
l2.grid(row=0, column=2)
l3=Label(window,text="Year")
l3.grid(row=1, column=0)
l4=Label(window,text="ISBN")
l4.grid(row=1, column=2)

#creating entries for labels
title_entry=StringVar()
e1=Entry(window, textvariable=title_entry)
e1.grid(row=0,column=1)
author_entry=StringVar()
e2=Entry(window, textvariable=author_entry)
e2.grid(row=0,column=3)
year_entry=StringVar()
e3=Entry(window, textvariable=year_entry)
e3.grid(row=1,column=1)
isbn_entry=StringVar()
e4=Entry(window, textvariable=isbn_entry)
e4.grid(row=1,column=3)

#creating a list box for book records
lst=Listbox(window, height=6, width=35 )
lst.grid(row=2,column=0,rowspan=6,columnspan=2)

#creating scrollbar for list 
scrl=Scrollbar(window)
scrl.grid(row=2, column=2, rowspan=6)

#arranging listbox and scrollbar side by side
lst.configure(yscrollcommand=scrl.set)
scrl.configure(command=lst.yview)

#binding get_selected_row method to click on Listbox window
lst.bind("<<ListboxSelect>>", get_selected_row)



#creating buttons 
b1=Button(window, text='View all', width=12 , command=view_command)
b1.grid(row=2,column=3)
b2=Button(window, text='Search entry', width=12, command=search_command)
b2.grid(row=3,column=3)
b3=Button(window, text='Add entry', width=12, command=add_command)
b3.grid(row=4,column=3)
b4=Button(window, text='Update Selected ', width=12, command=update_command)
b4.grid(row=5,column=3)
b5=Button(window, text='Delete Selected', width=12, command=delete_command)
b5.grid(row=6,column=3)
b6=Button(window, text='Close', width=12, command=window.destroy)
b6.grid(row=7,column=3)


#keeping window open until user close it 
window.mainloop()
