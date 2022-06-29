#import libraries
from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
show = "all"


def match(pin):
    if(pin == "1234"):  return True
    else: False
class Node:
    def __init__(self, data = None):
        self.value = data
        self.id = 0
        self.next = None
        self.prev = None


class Doubly_link_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.id = 0
    
    def append(self,data):
        new_node = Node(data)
        self.id = self.id + 1
        
        new_node.id = self.id
        if self.head is None:
            self.head = new_node 
            self.tail = new_node
            return
        
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node
        
    def delete(self,data):
        if(self.head is None):
            print("List is empty")
            return
        
        if(self.head.value[0] == data):
            self.head = self.head.next
            self.id = self.id - 1
            return
        
        if(self.tail.value[0] == data):
            self.tail = self.tail.prev
            self.tail.next = None
            self.id = self.id - 1
            return

        temp_1= self.head
        
        prev = None
        while(temp_1 is not None):
            if(temp_1.value[0] == data):
                temp_1.next.prev = prev
                prev.next = temp_1.next
                self.id = self.id - 1
                print("Deleted Successfuly")
                return
            prev = temp_1
            temp_1 = temp_1.next
        
        print("Sorry not found ")
        
    def display(self):
        temp = self.head
        while(temp is not None):
            print(temp.value)
            temp = temp.next
    
    def Search(self, data):
        search_list = Doubly_link_list()
        if(self.head is None):
            print("List is empty")
            return -1
        
#        if(self.head.value[0] == data):
#             search_list.append(data)
#             return search_list
        
#         if(self.tail.value[0] == data):
#             return data
        
        
        temp_1 = self.head
        while(temp_1 is not None):
            if(temp_1.value[0] == data):
                search_list.append(temp_1.value)
            temp_1 = temp_1.next

        if(search_list.head is None):
            print("data not found")
        return search_list

    def Update(self,search_key, data):
        if(self.head is None):
            print("List is empty")
            return -1
        
        if(self.head.value[0] == search_key):
            self.head.value = data
            return
            
        if(self.tail.value[0] == search_key):
            self.tail.value = data
            return
        
        
        temp_1 = self.head
        while(temp_1 is not None):
            if(temp_1.value[0] == search_key):
                temp_1.value = data
                return
            temp_1 = temp_1.next

        print("data not found")
    
    def Delete_ALL(self):
        self.head = None
        self.tail = None

L = Doubly_link_list()
Fav = Doubly_link_list()

#defining function for creating GUI Layout
def DisplayForm():
    #creating window
    heading_color = "#15244C"
    label_color = "#15244C"
    btn_color = "#a6aaab"
    
    display_screen = Tk()
    #setting width and height for window
    display_screen.geometry("1800x800")
    #setting title for window
    display_screen.title("SmartPhone Contact Directory")
    global tree
    global SEARCH
    global fname,lname,gender,address,contact,second_contact, designation, email, nickname, relationship, birthday
    SEARCH = StringVar()
    fname = StringVar()
    lname = StringVar()
    gender = StringVar()
    address = StringVar()
    contact = StringVar()
    second_contact = StringVar()
    designation = StringVar()
    email = StringVar()
    nickname = StringVar()
    relationship = StringVar()
    birthday = StringVar()


    #creating frames for layout
    #topview frame for heading
    TopViewForm = Frame(display_screen, width=600, bd=1, relief=SOLID)
    TopViewForm.pack(side=TOP, fill=X)
    #first left frame for registration from
    LFrom = Frame(display_screen, width="350",bg="#15244C")
    LFrom.pack(side=LEFT, fill=Y)
    #seconf left frame for search form
    LeftViewForm = Frame(display_screen, width=500,bg="#15244C")
    LeftViewForm.pack(side=LEFT, fill=Y)
    
    #mid frame for displaying lnames record
    MidViewForm = Frame(display_screen, width=600)
    MidViewForm.pack()


    #label for heading
    lbl_text = Label(TopViewForm, text="SmartPhone Contact Directory", font=('century gothic', 70), width=600,bg=heading_color,fg= 'white')
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="First Name  ", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=fname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Last Name ", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=lname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Gender ", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    #Entry(LFrom, font=("Arial", 10, "bold"),textvariable=gender).pack(side=TOP, padx=10, fill=X)
    gender.set("Select Gender")
    content={'Male','Female'}
    OptionMenu(LFrom,gender,*content).pack(side=TOP, padx=10, fill=X)


    Label(LFrom, text="Address ", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=address).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Phone ", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Another Phone", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=second_contact).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Designation", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=designation).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Nickname", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=nickname).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=email).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="BirthDate", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=birthday).pack(side=TOP, padx=10, fill=X)

    Label(LFrom, text="Relationship", font=("Arial", 12),bg=label_color,fg="#fcfcfc").pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=relationship).pack(side=TOP, padx=10, fill=X)

    Button(LFrom,text="Save Contact",font=("Arial", 10, "bold"),command=register,bg="#a6aaab",fg="black").pack(side=TOP, padx=10,pady=5, fill=X)


    #creating search label and entry in second frame
    lbl_txtsearch = Label(LeftViewForm, text="Enter Name to Search", font=('verdana', 12),bg=label_color, fg="#fcfcfc")
    lbl_txtsearch.pack()
    #creating search entry
    search = Entry(LeftViewForm, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=TOP, padx=10, fill=X)
    #creating search button
    btn_search = Button(LeftViewForm, text="Search", command=SearchRecord,bg=btn_color)
    btn_search.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating view button
    btn_view = Button(LeftViewForm, text="View All Contacts", command=veiw_All,bg=btn_color)
    btn_view.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating reset button
    btn_reset = Button(LeftViewForm, text="Reset", command=Reset,bg=btn_color)
    btn_reset.pack(side=TOP, padx=10, pady=10, fill=X)
    #creating delete button
    btn_delete = Button(LeftViewForm, text="Delete", command=Delete,bg=btn_color)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #create update button
    btn_delete = Button(LeftViewForm, text="Edit Contact", command=Update,bg=btn_color)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #add to favourite
    
    btn_delete = Button(LeftViewForm, text="Mark Favourite Contact", command=add_to_fav,bg=btn_color)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #for favrout
    btn_delete = Button(LeftViewForm, text="Favourite Contacts", command=show_fav,bg=btn_color)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)

    #create delete all button
    btn_delete = Button(LeftViewForm, text="Delete All", command=Delete_ALL,bg=btn_color)
    btn_delete.pack(side=TOP, padx=10, pady=10, fill=X)
    #setting scrollbar
    scrollbarx = Scrollbar(MidViewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(MidViewForm, orient=VERTICAL)
    tree = ttk.Treeview(MidViewForm,columns=("person Id", "fname", "lname", "sex","adrs","ph_no", "ph_no 2", "desg", "nname", "email", "bday", "rel"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('person Id', text="Id", anchor=W)
    tree.heading('fname', text="FirstName", anchor=W)
    tree.heading('lname', text="LastName", anchor=W)
    tree.heading('sex', text="Gender", anchor=W)
    tree.heading('adrs', text="Address", anchor=W)
    tree.heading('ph_no', text="Phone", anchor=W)
    tree.heading('ph_no 2', text="Another Phone", anchor=W)
    tree.heading('desg', text="Designation", anchor=W)
    tree.heading('nname', text="Nickname", anchor=W)
    tree.heading('email', text="Email", anchor=W)
    tree.heading('bday', text="Birthday", anchor=W)
    tree.heading('rel', text="Relationship", anchor=W)

    #setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=50)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=200)
    tree.column('#6', stretch=NO, minwidth=0, width=80)
    tree.column('#7', stretch=NO, minwidth=0, width=90)
    tree.column('#8', stretch=NO, minwidth=0, width=80)
    tree.column('#9', stretch=NO, minwidth=0, width=80)
    tree.column('#10', stretch=NO, minwidth=0, width=120)
    tree.column('#11', stretch=NO, minwidth=0, width=80)
    tree.pack()
    DisplayData()
#function to update data into database
def Update():
    global L
    #getting form data

    fname1=fname.get()
    lname1=lname.get()
    gender1=gender.get()
    address1=address.get()
    contact1=contact.get()
    contact2=second_contact.get()
    designation1 =designation.get()
    nickname1 =nickname.get()
    email1 = email.get()
    birthday1 = birthday.get()
    relationship1 = relationship.get()
    #applying empty validation
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        pin = askstring('Name', 'Enter Pin Code')
        if(match(pin)):
            tkMessageBox.showinfo("Warning","DONE!!!")
        else:
            tkMessageBox.showinfo("Warning","INCORECT PIN!!!")
            return
        #getting selected data
        curItem = tree.focus()
        contents = (tree.item(curItem))
        selecteditem = contents['values'][1]
        #update query
        data = (fname1,lname1,gender1,address1,contact1, contact2, designation1, nickname1, email1, birthday1)
        L.Update(selecteditem,data)
        tkMessageBox.showinfo("Message","Updated successfully")
        #reset form
        Reset()
        #refresh table data
        DisplayData()
def register():
    global L
    #getting form data
    try:
        fname1=str(fname.get())
        lname1=str(lname.get())
        gender1=gender.get()
        address1=address.get()
        contact1=int(contact.get())
        contact2=int(second_contact.get())
        designation1 = designation.get()
        nickname1 = nickname.get()
        email1 = email.get()
        birthday1 = birthday.get()
        relationship1 = relationship.get()
    except:
        tkMessageBox.showinfo("Warning","Enter Correct Data!!!")
        return
    #applying empty validation
    if fname1=='' or lname1==''or gender1=='' or address1==''or contact1=='':
        tkMessageBox.showinfo("Warning","fill the empty field!!!")
    else:
        #execute query
        data = (fname1,lname1,gender1,address1,contact1, contact2, designation1, nickname1, email1, birthday1)
        L.append(data)
        tkMessageBox.showinfo("Message","Stored successfully")
        #refresh table data
        DisplayData()
def Reset():
    #clear current data from table
    tree.delete(*tree.get_children())
    #refresh table data
    DisplayData()
    #clear search text
    SEARCH.set("")
    fname.set("")
    lname.set("")
    gender.set("")
    address.set("")
    contact.set("")
    second_contact.set("")
    designation.set("")
    email.set("")
    nickname.set("")
    birthday.set("")
def Delete():
    global L,show,Fav
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        pin = askstring('Pin', 'Enter pin code')
        if(match(pin)):
            tkMessageBox.showinfo("Warning","DONE!!!")
        else:
            tkMessageBox.showinfo("Warning","INCORECT PIN!!!")
            return
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values'][1]
            tree.delete(curItem)
            if(show == "all"):
                L.delete(selecteditem)
                Fav.delete(selecteditem)
            else:
                Fav.delete(selecteditem)
            L.display()
            
def Delete_ALL():
    pin = askstring('Pin', 'Enter Pin Code')
    if(match(pin)):
        tkMessageBox.showinfo("Warning","DONE!!!")
    else:
        tkMessageBox.showinfo("Warning","INCORECT PIN!!!")
        return
    result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',icon="warning")
    global L,Fav
    tree.delete(*tree.get_children())
    L.Delete_ALL()
    Fav.Delete_ALL()
        

#function to search data
def SearchRecord():
    global L
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        fetch = L.Search(SEARCH.get())
        #fetch all matching records
        #loop for displaying all records into GUI
        temp = fetch.head
        while temp is not None:
            tree.insert('', 'end', values=(temp.id,*temp.value))
            temp = temp.next

def veiw_All():
    global show
    show = "all"
    DisplayData()

def show_fav():
    global show
    show = "fav"
    DisplayData()

def add_to_fav():
    global Fav
    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to add to favourite")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to add this record to favourite?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            selecteditem = selecteditem[1:]
            Fav.append(tuple(selecteditem))
            Fav.display()

def DisplayData():
    global L,show,Fav
    tree.delete(*tree.get_children())

    if(show == "fav"):
        temp = Fav.head
        while temp is not None:
            tree.insert('', 'end', values=(temp.id,*temp.value))
            tree.bind("<Double-1>",OnDoubleClick)
            temp = temp.next
        return
    
    temp = L.head
    while temp is not None:
        tree.insert('', 'end', values=(temp.id,*temp.value))
        tree.bind("<Double-1>",OnDoubleClick)
        temp = temp.next
 
def OnDoubleClick(self):
    #getting focused item from treeview
    curItem = tree.focus()
    contents = (tree.item(curItem))
    selecteditem = contents['values']
    #set values in the fields
    fname.set(selecteditem[1])
    lname.set(selecteditem[2])
    gender.set(selecteditem[3])
    address.set(selecteditem[4])
    contact.set(selecteditem[5])
    second_contact.selecteditem[6]
    designation.selecteditem[7]
    email.selecteditem[8]
    nickname.selecteditem[9]
    birthday.selecteditem[10]

#calling function
DisplayForm()
if __name__=='__main__':
    #Running Application
    mainloop()
