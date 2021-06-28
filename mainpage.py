import tkinter as tk
from tkinter import *
from tkinter import messagebox 
import os 
import webbrowser
import pymysql

org,co='nun','nun'
def action(dep):
    if dep=='Computer Department':
        a='comp_form_action'
    elif dep=='Electrical Department':
        a='electrical_form_action'
    elif dep=='Electronic Department':
        a='electronic_form_action'
    elif dep=='Mechanical Department':
        a='mech_form_action'
    elif dep=='NSS':
        a='nss_form_action'
    elif dep=='College level':
        a='collegeLevel_form_action'
    os.system('python'+' '+a+'.py')

def client_exit():
    exit()

def client_sql():
    feed = tk.Tk()
    feed.geometry("1000x600")
    feed.title("FEEDBACK.....")
    feed.config(bg='gray')
    v1=tk.IntVar()
    # Dictionary to create multiple buttons
    values = {"ENTER FEEDBACK" : "1",
            "VIEW FEEDBACK" : "2"}

    # Loop is used to create multiple Radiobuttons
    # rather than creating each button separately
    tk.Radiobutton(feed,
            text="ENETR FEEDBACK",
            padx = 20,
            variable=v1, activebackground="red",activeforeground="white",value=1,command=lambda *args:FeedbackEntryPoint(feed)).place(x=0,y=0)
    tk.Radiobutton(feed,
            text="VIEW FEEDBACK",
            padx = 20,
            variable=v1,activebackground="red",activeforeground="white",value=2,command=lambda *args:feedbackShow_action(feed)).place(x=0,y=50)
def radioo(i):
	global org
	if i=='g':
		org='Good'
	elif i=='v':
		org='Very Good'
	elif i == 'e':
		org='Excellent'
	elif i=='b':
		org='Bad'
		
def radioc(i):
	global co
	if i=='g':
		co='Good'
	elif i=='v':
		co='Very Good'
	elif i == 'e':
		co='Excellent'
	elif i=='b':
		co='Bad'
	elif i=='n':
		co='Not Known'
		
def FeedbackEntryPoint(feed):
	new=tk.Tk()
	new.geometry("1000x600")
	root.title("Feedback")
	h='Feedback For College'
	Label(new, text = h, font =('Verdana', 15)).pack(side = TOP, pady = 10)
	tk.Label(new,text="Name:").place(x=0,y=100)
	tk.Label(new,text="Location:").place(x=0,y=120)
	tk.Label(new,text="Phone NO.:").place(x=0,y=140)
	t="Please mention the name of event for which you want to give feedback :"
	tk.Label(new,text=t).place(x=0,y=160)
	t="How much do you like organisation of events ?"
	tk.Label(new,text=t).place(x=0,y=200)
	value = IntVar()
	statRadio1 = tk.Radiobutton(new, text = "Good", value = 0,command=lambda *args: radioo('g'), font = 'Calibri 11')
	statRadio1.place(x = 0, y =220, height = 20, width = 100)
	statRadio2 = tk.Radiobutton(new, text = "Very Good", value = 1,command=lambda *args: radioo('v'), font = 'Calibri 11')
	statRadio2.place(x = 120, y =220, height = 20, width = 100)
	statRadio3 = tk.Radiobutton(new, text = "Excellent", value = 2,command=lambda *args: radioo('e'), font = 'Calibri 11')
	statRadio3.place(x = 260, y =220, height = 20, width = 100)
	statRadio4 = tk.Radiobutton(new, text = "Bad", value = 3,command=lambda *args: radioo('b'), font = 'Calibri 11')
	statRadio4.place(x = 380, y =220, height = 20, width = 100)
	v2 = IntVar()
	t="What remark do you like to give for College Level Events ?"
	tk.Label(new,text=t).place(x=0,y=240)
	statRadio5 = tk.Radiobutton(new, text = "Good", variable=v2,value=0,command=lambda *args: radioc('g'), font = 'Calibri 11')
	statRadio5.place(x = 0, y =260, height = 20, width = 100)
	statRadio6 = tk.Radiobutton(new, text = "Very Good", variable=v2,value=1,command=lambda *args: radioc('v'), font = 'Calibri 11')
	statRadio6.place(x = 120, y =260, height = 20, width = 100)
	statRadio7 = tk.Radiobutton(new, text = "Excellent", variable=v2,value=2,command=lambda *args: radioc('e'), font = 'Calibri 11')
	statRadio7.place(x = 260, y =260, height = 20, width = 100)
	statRadio8 = tk.Radiobutton(new, text = "Bad", variable=v2,value=3,command=lambda *args: radioc('b'), font = 'Calibri 11')
	statRadio8.place(x = 380, y =260, height = 20, width = 100)
	
	tk.Label(new,text="Feedback:").place(x=0,y=300)
	e1 = tk.Entry(new)
	e2 = tk.Entry(new)
	e3 = tk.Entry(new)
	e4 = tk.Entry(new)
	e5 = tk.Entry(new)

	e1.place(x=90,y=100)
	e2.place(x=90,y=120)
	e3.place(x=90,y=140)
	e4.place(x=0,y=180)
	e5.place(x=90,y=300)
	tk.Button(new,text='ADD',command=lambda *args: feedbackEntry_action(new,feed,e1,e2,e3,e4,e5),width=30).place(x=40,y=340)
		
def feedbackEntry_action(new,feed,e1,e2,e3,e4,e5):
    if (e1.get()=='' or e2.get()=='' or e3.get()=='' or e4.get()==''):
		messagebox.showinfo("ERROR", "Please fill all the entries")
		feed.destroy()
	elif e3.get().isdigit() and len(e3.get())==10:
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="project")
		
		try:
			if e5.get()=='.!entry5':
				e5='-'
			else:
				e5=e5.get()
			cursor = connection.cursor()
			sql = "INSERT INTO `feedback` (`Name`, `ExtraFeedback`, `Location`, `Phone_no.`, `ManagementOfEvent`, `Remark`, `EventName`) VALUES (%s, %s, %s, %s,%s,%s,%s)"
					# Execute the query
					cursor.execute(sql, (e1.get(),e5,e2.get(),e3.get(),org,co,e4.get()))

			# the connection is not autocommited by default. So we must commit to save our changes.
			connection.commit()
			messagebox.showinfo("Conformation", "Thank You !\nFEEDBACK SUCCESSFUL")
			feed.destroy()
			new.destroy()
		except:
			messagebox.showinfo("Conformation", "Sorry for inconvinence.\nSomething went wrong please try latter.")
			feed.destroy()
	else:
		messagebox.showinfo("ERROR", "Please feed valid phone number")
		feed.destroy()

def feedbackShow_action(feed):
	mydb = pymysql.connect(
		host="localhost",
		user="root",
		passwd="",
		database="project"
		)

	mycursor = mydb.cursor()
	def on_configure(event):
		# update scrollregion after starting 'mainloop'
		# when all widgets are in canvas
		canvas.configure(scrollregion=canvas.bbox('all'))



	# --- create canvas with scrollbar ---

	canvas = tk.Canvas(feed)
	canvas.pack(fill = BOTH,expand = True,side=tk.LEFT)

	scrollbar = tk.Scrollbar(feed, command=canvas.yview)
	scrollbar.pack(side=tk.RIGHT, fill='y')

	canvas.configure(yscrollcommand = scrollbar.set)

	# update scrollregion after starting 'mainloop'
	# when all widgets are in canvas
	canvas.bind('<Configure>', on_configure)

	# --- put frame in canvas ---

	frame = tk.Frame(canvas)
	canvas.create_window((0,0), window=frame, anchor='nw')
	mycursor.execute("SELECT * FROM feedback")
	obj=mycursor.fetchall()

	row_count=len(obj)
	i=0
	Label(frame, text = 'FEEDBACK VIEW WINDOW\n'+tkvar.get(), font =('Candara Bold Italic', 16)).pack(side = TOP, pady = 10)
	while i<row_count:
		pr=('NAME:',obj[i][0])
		Label(frame, text = pr, font =('Calibri', 13)).pack(side = TOP, pady = 10)
		pr=('FEEDBACK:',obj[i][1])
		Label(frame, text = pr, font =('Calibri', 13)).pack(side = TOP, pady = 10)
		pr=('LOCATION:',obj[i][2])
		Label(frame, text = pr, font =('Calibri', 13)).pack(side = TOP, pady = 10)
		pr=('PHONE_NO.:',obj[i][3])
		Label(frame, text = pr, font =('Calibri', 13)).pack(side = TOP, pady = 10)
		pr=('---------------------------------------------------')
		Label(frame, text = pr, font =('Calibri', 13)).pack(side = TOP, pady = 10)
		i=i+1



def callback():
    webbrowser.open_new(("http://sigce.edu.in/aspdat/page.asp?id=41"))

root = tk.Tk()
root.geometry("700x420")
root.config(bg='red')
root.title("Event Management System")
img = PhotoImage(file="sigce.png")
img=img.subsample(4, 4)
label=Label(root,image=img).place(x=0,y=0)
Label(root, text = 'Smt. Indira Gandhi College Of Engineering Events', font =('Verdana', 15)).pack(side = TOP, pady = 10)
menu = Menu(root)
root.config(menu=menu)
file = Menu(menu)
menu.add_cascade(label="menu", menu=file)
file.add_command(label="Feedback", command=client_sql)
edit = Menu(menu)
menu.add_cascade(label="about us", menu=edit)
edit.add_command(label="history",command=callback)


# Add a grid
mainframe = Frame(root)
mainframe.pack()
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

# Create a Tkinter variable
tkvar = StringVar(root)

# Dictionary with options
choices = { 'Computer Department','Electrical Department','Electronic Department','Mechanical Department','NSS','College level'}
tkvar.set('Computer Department') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="PLEASE HAVE YOUR CHOICE:").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    action(tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)
Button(root, text="QUIT",height = 1, width = 40,activebackground="red",activeforeground="white",command=client_exit).pack(side = BOTTOM , pady = 10)
root.mainloop()
