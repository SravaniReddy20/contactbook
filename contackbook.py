#PythonGeeks - import library
from tkinter import *
from tkinter import messagebox


#PythonGeeks - Initialize window
root = Tk()
root.geometry('700x655')
root.config(bg = '#e0e4e3')
root.title('Contact Book')
root.resizable(0,0)
contactlist = [
    ['Siddharth Nigam','369854712'],
    ['Gaurav Patil', '521155222'],
    ['Abhishek Nikam', '78945614'],
    ['Sakshi Gaikwad', '58745246']
    ]

Name = StringVar()
Number = StringVar()


#PythonGeeks - create frame
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set,font=('Times new roman',16),bg="#f0fffc",width=20,height=20,borderwidth=3,relief="groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


#PythonGeeks - function to get select value

def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error", "Please Select the Name")
	else:
		return int(select.curselection()[0])
    
#PythonGeeks -function to add new contact
def AddContact():
    if Name.get()!="" and Number.get()!="":
        contactlist.append([Name.get() ,Number.get()])
        print(contactlist)
        Select_set()
        ClearAllContacts()
        messagebox.showinfo("Confirmation", "Successfully Add New Contact")

    else:
        messagebox.showerror("Error","Please fill the information")


# fun to edit existing contact

def UpdateDetail():
	if Name.get() and Number.get():
		contactlist[Selected()] = [Name.get(), Number.get()]
    

		messagebox.showinfo("Confirmation", "Successfully Update Contact")
		ClearAllContacts()
		Select_set()

	elif not(Name.get()) and not(Number.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n press Load button")
		else:
			message1 = """To Load the all information of \n 
						  selected row press Load button\n.
						  """   
			messagebox.showerror("Error", message1)


#PythonGeeks- function to delete selected contact
def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','You Want to Delete Contact\n Which you selected')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

   
# func to view contact
def VIEW():
    NAME, PHONE = contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)

# func to clear all contacts in the book 
def ClearAllContacts():
    if contactlist:
        result = messagebox.askyesno("Confirmation", "Are you sure you want to delete all contacts?")
        if result:
            contactlist.clear()  # Clear the contact list
            Select_set()         # Refresh the listbox
            messagebox.showinfo("Success", "All contacts have been cleared.")
    else:
        messagebox.showinfo("Info", "No contacts to clear.")

        

#PythonGeeks- function to exit game window   
def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone in contactlist :
        select.insert (END, name)
Select_set()


#PythonGeeks - define buttons labels and entry widget 
Label(root, text = 'Name', font=("Times new roman",25,"bold"), bg = '#e0e4e3').place(x= 50, y=30)
Entry(root, textvariable = Name, width=30).place(x= 200, y=30)
Label(root, text = 'Contact No.', font=("Times new roman",22,"bold"),bg = '#e0e4e3').place(x= 50, y=70)
Entry(root, textvariable = Number, width=30).place(x= 200, y=80)

Button(root,text=" ADD", font='Helvetica 18 bold',bg='#22dad8', command = AddContact, padx=20). place(x= 50, y=140)
Button(root,text="UPDATE", font='Helvetica 18 bold',bg='#22dad8',command = UpdateDetail, padx=20).place(x= 50, y=200)
Button(root,text="DELETE", font='Helvetica 18 bold',bg='#22dad8',command = Delete_Entry, padx=20).place(x= 50, y=260)
Button(root,text="VIEW", font='Helvetica 18 bold',bg='#22dad8', command = VIEW).place(x= 50, y=325)
Button(root,text="CLEAR ALL", font='Helvetica 18 bold',bg='#22dad8', command = ClearAllContacts).place(x= 50, y=390)
Button(root,text="EXIT", font='Helvetica 24 bold',bg='tomato', command = EXIT).place(x= 250, y=470)

root.mainloop()