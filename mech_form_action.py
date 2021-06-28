import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
import os
import subprocess as sp
import MechanicalEventAdd
import webbrowser

org,co='nun','nun'
a=''
root = tk.Tk()
root.geometry("1000x600")
root.config(bg='pink')
root.title("Mechanical DEPARTMENT")
Label(root, text = 'Smt. Indira Gandhi College Of Engineering Events', font =('Verdana', 15)).pack(side = TOP, pady = 10)
Label(root, text = 'Mechanical DEPARTMENT', font =('Calibri', 13)).pack(side = TOP, pady = 10)
def action_add(a):
    os.system('python '+a+'.py')

def adding(event,e1):
	print(e1.get())
	a=e1.get()
	fileName = a+'Mechanical.py'
	f=open(fileName,"w+")
	f1=open(fileName,"a")
	f.write("import tkinter as tk\nfrom tkinter import *\nroot = tk.Tk()\nroot.geometry('1000x600')\nroot.config(bg='yellow')\nroot.title('Mechanical DEPARTMENT')\n\n#please enter event information between ' '\n\nLabel(root, text = ' '")
	f.close()
	connection = pymysql.connect(host="localhost",user="root",passwd="",database="project")

	cursor = connection.cursor()
	sql = "CREATE TABLE `project`.`feedback_mechanical_"+a+"` (`Name` VARCHAR(20) NOT NULL ,`Feedback` varchar(50) NOT NULL ,`Location` VARCHAR(50) NOT NULL,`Phone_no.` varchar(10) NOT NULL)"
	print(sql)
	cursor.execute(sql)
	Button(root, text=a,height = 1, width = 40,command=lambda *args: action_add(a)).pack(side = TOP , pady = 10)
	programName = "notepad.exe"
	fileName = a+".py"
	sp.Popen([programName, fileName])
	f1.write(", font =('Verdana', 15)).pack(side = TOP, pady = 10)\nmainloop()\n\n#please save file after entering info.")
	f1.close()
	fele=open("MechanicalEventAdd.py","a")
	fele.write("\n")
	tran=''
	tran="a='"+a+"'"
	fele.write(tran)
	fele.write("\n\nchoices.append(a)\neve.append(a)\nButton(root, text=a,height = 1, width = 40,command=lambda *args: action_add(a)).pack(side = TOP , pady = 10)\nn=n+1")
	event.destroy()
def addEvent(event,e1,e2):
	if e1.get()=='eventAdd' and e2.get()=='sigce':
		event.destroy()
		event=tk.Tk()
		root.geometry("1000x600")
		root.title("New Event")
		tk.Label(event,text="Event Name").grid(row=0)
		e1 = tk.Entry(event)
		e1.grid(row=0, column=1)
		tk.Button(event,text='ADD',command=lambda *args: adding(e1)).grid(row=3,column=1,pady=4)
	else:
		event.destroy()
		login(1)
def login(s):
	if s==1:
		messagebox.showinfo("Conformation", "Login Unsuccessful\nuser id or password wrong")
	event=tk.Tk()
	event.title("Login")
	tk.Label(event,
         text="user id").grid(row=0)
	e1 = tk.Entry(event)
	tk.Label(event,
         text="Password").grid(row=1)
	e2 = tk.Entry(event)
	e1.grid(row=0, column=1)
	e2.grid(row=1, column=1)
	tk.Button(event,
          text='Login',command=lambda *args: addEvent(event,e1,e2)).grid(row=3,
                                                       column=1,
                                                       pady=4)

#****************************************************SQL Starts***************************************************************
def feedback_sql(fed):
    feed = tk.Tk()
    feed.geometry("1000x600")
    feed.title("FEEDBACK.....")
    feed.config(bg='gray')

    if (fed=='sem' or fed=='spor' or fed=='tech'):
        v1=tk.IntVar()
        # Dictionary to create multiple buttons
        values = {"ENTER FEEDBACK" : "1",
                "VIEW FEEDBACK" : "2"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        tk.Radiobutton(feed,
              text="ENETR FEEDBACK",
              padx = 20,
              variable=v1, activebackground="red",activeforeground="white",value=1,command=lambda *args:feedbackEntrySelect(feed)).place(x=0,y=0)
        tk.Radiobutton(feed,
              text="VIEW FEEDBACK",
              padx = 20,
              variable=v1,activebackground="red",activeforeground="white",
              value=2,command=lambda *args:feedbackShowSelect(feed)).place(x=0,y=50)
    elif fed=='mechanical':
        v1=tk.IntVar()
        # Dictionary to create multiple buttons
        values = {"ENTER FEEDBACK" : "1",
                "VIEW FEEDBACK" : "2"}

        # Loop is used to create multiple Radiobuttons
        # rather than creating each button separately
        tk.Radiobutton(feed, 
              text="ENETR FEEDBACK",
              padx = 20, 
              variable=v1, activebackground="red",activeforeground="white",value=1,command=lambda *args:FeedbackEntryPoint(feed,'mechanical')).place(x=0,y=0)
        tk.Radiobutton(feed, 
              text="VIEW FEEDBACK",
              padx = 20, 
              variable=v1,activebackground="red",activeforeground="white", 
              value=2,command=lambda *args:feedbackShow_action(feed,'mechanical')).place(x=0,y=50)

def feedbackEntrySelect(feed):
    mainframe = Frame(feed)
    mainframe.pack()
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)

    # Create a Tkinter variable
    tkvar = StringVar(feed)

    # Dictionary with options
    choices = [ 'sports','tech-fest','seminar']
    tkvar.set('sports') # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="PLEASE HAVE YOUR CHOICE:").grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)
    FeedbackEntryPoint(feed,tkvar)
def feedbackShowSelect(feed):
    mainframe = Frame(feed)
    mainframe.pack()
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)

    # Create a Tkinter variable
    tkvar = StringVar(feed)

    # Dictionary with options
    choices = [ 'sports','tech-fest','seminar']
    tkvar.set('sports') # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="PLEASE HAVE YOUR CHOICE:").grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)
    tk.Button(feed,
            text='show',command=lambda *args: feedbackShow_action(feed,tkvar)).place(x=500,y=180)


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
		
def FeedbackEntryPoint(feed,tkvar):
	if tkvar == 'mechanical':
		new=tk.Tk()
		new.geometry("1000x600")
		root.title("Feedback")
		h='Feedback For Mechanical Department'
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
		tk.Button(new,text='ADD',command=lambda *args: feedbackEntry_action(new,feed,tkvar,e1,e2,e3,e4,e5),width=30).place(x=40,y=340)
	else:
		new=tk.Tk()
		new.geometry("1000x600")
		root.title("Feedback")
		h='Feedback For '+tkvar.get()+' Management'
		Label(new, text = h, font =('Verdana', 15)).pack(side = TOP, pady = 10)
		tk.Label(new,text="Name:").place(x=0,y=100)
		
		tk.Label(new,text="Location:").place(x=0,y=120)
		
		tk.Label(new,text="Phone NO.:").place(x=0,y=140)
		
		t="Please mention the name of "+tkvar.get()+" for which you want to give feedback :"
		tk.Label(new,text=t).place(x=0,y=160)
		
		t="How was the "+tkvar.get()+" organised ?"
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
		t="Was the Co-ordinators helpful ?"
		tk.Label(new,text=t).place(x=0,y=240)
		statRadio5 = tk.Radiobutton(new, text = "Good", variable=v2,value=0,command=lambda *args: radioc('g'), font = 'Calibri 11')
		statRadio5.place(x = 0, y =260, height = 20, width = 100)
		statRadio6 = tk.Radiobutton(new, text = "Very Good", variable=v2,value=1,command=lambda *args: radioc('v'), font = 'Calibri 11')
		statRadio6.place(x = 120, y =260, height = 20, width = 100)
		statRadio7 = tk.Radiobutton(new, text = "Excellent", variable=v2,value=2,command=lambda *args: radioc('e'), font = 'Calibri 11')
		statRadio7.place(x = 260, y =260, height = 20, width = 100)
		statRadio8 = tk.Radiobutton(new, text = "Bad", variable=v2,value=3,command=lambda *args: radioc('b'), font = 'Calibri 11')
		statRadio8.place(x = 380, y =260, height = 20, width = 100)
		statRadio9 = tk.Radiobutton(new, text = "Not known", variable=v2,value=4,command=lambda *args: radioc('n'), font = 'Calibri 11')
		statRadio9.place(x = 480, y =260, height = 20, width = 100)
		
		tk.Label(new,text="Have extra Feedback ?").place(x=0,y=300)
		e1 = tk.Entry(new)
		e2 = tk.Entry(new)
		e3 = tk.Entry(new)
		e4 = tk.Entry(new)
		e5 = tk.Entry(new)

		e1.place(x=90,y=100)
		e2.place(x=90,y=120)
		e3.place(x=90,y=140)
		e4.place(x=0,y=180)
		e5.place(x=0,y=320)
		tk.Button(new,text='ADD',command=lambda *args: feedbackEntry_action(new,feed,tkvar,e1,e2,e3,e4,e5),width=30).place(x=40,y=340)

def feedbackEntry_action(new,feed,tkvar,e1,e2,e3,e4,e5):
	
	if (e1.get()=='' or e2.get()=='' or e3.get()=='' or e4.get()==''):
		messagebox.showinfo("ERROR", "Please fill all the entries")
		feed.destroy()
	elif e3.get().isdigit() and len(e3.get())==10:
		connection = pymysql.connect(host="localhost",user="root",passwd="",database="project")
		if tkvar=='mechanical':
			try:
				if e5.get()=='.!entry5':
					e5='-'
				else:
					e5=e5.get()
				cursor = connection.cursor()
				sql = "INSERT INTO `feedback_"+tkvar+"` (`Name`, `ExtraFeedback`, `Location`, `Phone_no.`, `ManagementOfEvent`, `CoordinatorReview`, `EventName`) VALUES (%s, %s, %s, %s,%s,%s,%s)"
				# Execute the query
				cursor.execute(sql, (e1.get(),e5,e2.get(),e3.get(),org,co,e4.get()))

				# the connection is not autocommited by default. So we must commit to save our changes.
				connection.commit()
				messagebox.showinfo("Conformation", "Thank You !\nFEEDBACK SUCCESSFUL")
				feed.destroy()
				new.destroy()
			except:
				messagebox.showerror("Sorry", "Sorry for inconvinence.\nSomething went wrong please try latter.")
				feed.destroy()
		else:
			try:
				if e5.get()=='.!entry5':
					e5='NULL'
				else:
					e5=e5.get()
				cursor = connection.cursor()
				sql = "INSERT INTO `feedback_mechanical_"+tkvar.get()+"` (`Name`, `ExtraFeedback`, `Location`, `Phone_no.`, `ManagementOfEvent`, `CoordinatorReview`, `EventName`) VALUES (%s, %s, %s, %s,%s,%s,%s)"
				# Execute the query
				cursor.execute(sql, (e1.get(),e5,e2.get(),e3.get(),org,co,e4.get()))

				# the connection is not autocommited by default. So we must commit to save our changes.
				connection.commit()
				messagebox.showinfo("Conformation", "Thank You !\nFEEDBACK SUCCESSFUL")
				feed.destroy()
				new.destroy()
			except:
				messagebox.showerror("Sorry", "Sorry for inconvinence.\nSomething went wrong please try latter.")
				feed.destroy()
	else:
		messagebox.showinfo("ERROR", "Please feed valid phone number")
		feed.destroy()
	
	
def feedbackShow_action(feed,tkvar):
	mydb = pymysql.connect(host="localhost",user="root",passwd="",database="project")

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
	if tkvar=='mechanical':
		mycursor.execute("SELECT * FROM feedback_mechanical")
		obj=mycursor.fetchall()

		row_count=len(obj)
		i=0
		Label(frame, text = 'FEEDBACK VIEW WINDOW of Mechanical Department', font =('Candara Bold Italic', 16)).pack(side = TOP, pady = 10)
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
	elif tkvar.get()=='sports' or tkvar.get()=='seminar' or tkvar.get()=='tech-fest':
		quere="SELECT * FROM feedback_mechanical_"+tkvar.get()
		mycursor.execute(quere)
		obj=mycursor.fetchall()

		row_count=len(obj)
		i=0
		Label(frame, text = 'FEEDBACK VIEW WINDOW of '+tkvar.get(), font =('Candara Bold Italic', 16)).pack(side = TOP, pady = 10)
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

#***********************************************Sql ends******************************************************************************
def img_view(v):
	if v=='bu':
		webbrowser.open_new((""))

		menu = Menu(root)
		root.config(menu=menu)
		file = Menu(menu)
		menu.add_cascade(label="FEEDBACK", menu=file)
		file.add_command(label="Feedback FOR SPORTS", command=lambda *args:feedback_sql('spor'))

def menubar(root,type):
	menu = Menu(root)
	root.config(menu=menu)
	file = Menu(menu)
	menu.add_cascade(label="FEEDBACK", menu=file)
	file.add_command(label="Feedback FOR "+type, command=lambda *args:feedback_sql(type))

def action(n):
    if n==1:
        root = tk.Tk()
        root.geometry("700x420")
        root.title("SEMINAR.......")
    
        menubar(root,'semi')
    
    elif n==2:
        root = tk.Tk()
        root.geometry("1000x900")
        root.title("SPORTS.....")
        
        menubar(root,'spor')
        
        root.config(bg='orange')	
        Label(root,text='',font=('Verdana',15)).pack(pady=10)
        Label(root,text='',font=('Verdana',10)).pack(pady=10)
        Button(root, text="VIEW IMAGES",command=lambda *args: img_view('bu')).place(x=110,y=150)
        Label(root,text='=========================================================================================================================',font=('Verdana',10)).place(x=0,y=190)
    elif n==3:
        root = tk.Tk()
        root.geometry("700x420")
        
        menubar(root,'tech')

        root.title("TECHINCAL.....")
    elif n=='e':
        exit()

menu = Menu(root)
root.config(menu=menu)
file = Menu(menu)
menu.add_cascade(label="FEEDBACK", menu=file)
file.add_command(label="Feedback for Mechanical Department",activebackground="green",activeforeground="yellow",command=lambda *args:feedback_sql('mechanical'))
Button(root, text="ADD",height = 1, width = 40,command= lambda *args: login(0)).pack(side = BOTTOM , pady = 10)
Button(root, text="Seminar",height = 1, width = 40,command=lambda *args: action(1)).pack(side = TOP , pady = 10)
Button(root, text="Sports Events",height = 1, width = 40,activebackground="red",activeforeground="yellow",command=lambda *args: action(2)).pack(side = TOP , pady = 10)
Button(root, text="Techincal Events",height = 1, width = 40,command=lambda *args: action(3)).pack(side = TOP , pady = 10)
Button(root, text="BACK TO DEPARTMENT MENU", height = 1, width = 40,activebackground="red",activeforeground="white",command=lambda *args: action('e')).pack(side=BOTTOM,pady = 10)

mainloop()
