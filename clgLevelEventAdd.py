import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
import os
import webbrowser
root=Tk()
root.title("NEW EVENTS.....")
root.config(bg='red')
Label(root, text ='NEW EVENTS', font =('Calibri', 13)).pack(side = TOP, pady = 10)
choices = ['']
eve=[]
def action_add(a):
	print(a)
	os.system('python '+a+'.py')
def feedback_sql():
	feed = tk.Tk()
	feed.geometry("1000x600")
	feed.title("FEEDBACK.....")
	feed.config(bg='gray')
	
	v1=tk.IntVar()
	# Dictionary to create multiple buttons
	values = {"ENTER FEEDBACK" : "1","VIEW FEEDBACK" : "2"}

	# Loop is used to create multiple Radiobuttons
	# rather than creating each button separately
	tk.Radiobutton(feed,text="ENETR FEEDBACK",padx = 20,variable=v1, activebackground="red",activeforeground="white",value=1,command=lambda *args:feedbackEntrySelect(feed)).place(x=0,y=0)
	tk.Radiobutton(feed,text="VIEW FEEDBACK",padx = 20,variable=v1,activebackground="red",activeforeground="white",value=2,command=lambda *args:feedbackShowSelect(feed)).place(x=0,y=50)

def feedbackEntrySelect(feed):
    mainframe = Frame(feed)
    mainframe.pack()
    mainframe.columnconfigure(0, weight = 1)
    mainframe.rowconfigure(0, weight = 1)
    mainframe.pack(pady = 100, padx = 100)

    # Create a Tkinter variable
    tkvar = StringVar(feed)

    # Dictionary with options
    tkvar.set(choices[0]) # set the default option

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
    tkvar.set(choices[0]) # set the default option

    popupMenu = OptionMenu(mainframe, tkvar, *choices)
    Label(mainframe, text="PLEASE HAVE YOUR CHOICE:").grid(row = 1, column = 1)
    popupMenu.grid(row = 2, column =1)
    tk.Button(feed,
            text='show',command=lambda *args: feedbackShow_action(feed,tkvar)).place(x=500,y=180)


def FeedbackEntryPoint(feed,tkvar):
    tk.Label(feed,
            text="Name:").place(x=0,y=100)
    tk.Label(feed,
            text="Feedback:").place(x=0,y=120)
    tk.Label(feed,
            text="Location:").place(x=0,y=140)
    tk.Label(feed,
            text="Phone NO.:").place(x=0,y=160)
    e1 = tk.Entry(feed)
    e2 = tk.Entry(feed)
    e3 = tk.Entry(feed)
    e4 = tk.Entry(feed)
    e1.place(x=90,y=100)
    e2.place(x=90,y=120)
    e3.place(x=90,y=140)
    e4.place(x=90,y=160)
    tk.Button(feed,
            text='ADD',command=lambda *args: feedbackEntry_action(feed,tkvar,e1,e2,e3,e4)).place(x=40,y=180)

def feedbackEntry_action(feed,tkvar,e1,e2,e3,e4):
    
	connection = pymysql.connect(
                host="localhost",
                user="root",
                passwd="",
                database="project"
                )
	if (e1.get()=='' or e2.get()=='' or e3.get()=='' or e4.get()=='' or tkvar.get()==''):
		messagebox.showinfo("ERROR", "Please fill all the entries")
		FeedbackEntryPoint(feed,tkvar)
	elif e4.get().isdigit() and len(e4.get())==10:
		try:
			cursor = connection.cursor()
			sql = "INSERT INTO `feedback_comp_"+tkvar.get()+"` (`Name`,`Feedback`,`Location`,`Phone_no.`) VALUES (%s, %s, %s, %s)"
			# Execute the query
			cursor.execute(sql, (e1.get(),e2.get(),e3.get(),e4.get()))

			# the connection is not autocommited by default. So we must commit to save our changes.
			connection.commit()
			messagebox.showinfo("Conformation", "FEEDBACK SUCCESSFUL")
			feed.destroy()
		except:
			messagebox.showerror("Sorry", "Sorry for inconvinence.\nSomething went wrong please try latter.")
			feed.destroy()
	else:
		messagebox.showinfo("ERROR", "Please feed valid phone number")
		new.destroy()
		feed.destroy()
		FeedbackEntryPoint(feed,tkvar)

def feedbackShow_action(feed,tkvar):
	mydb = pymysql.connect(host="localhost",user="root",passwd="",database="project")
	mycursor = mydb.cursor()
	def on_configure(event):
		canvas.configure(scrollregion=canvas.bbox('all'))



    # --- create canvas with scrollbar ---

	canvas = tk.Canvas(feed)
	canvas.pack(side=tk.RIGHT)

	scrollbar = tk.Scrollbar(feed, command=canvas.yview)
	scrollbar.pack(side=tk.RIGHT, fill='y')

	canvas.configure(yscrollcommand = scrollbar.set)

    # update scrollregion after starting 'mainloop'
    # when all widgets are in canvas
	canvas.bind('<Configure>', on_configure)

	# --- put frame in canvas ---

	frame = tk.Frame(canvas)
	canvas.create_window((0,0), window=frame, anchor='nw')
	quere="SELECT * FROM `feedback_comp_"+tkvar.get()+"`"
	mycursor.execute(quere)
	obj=mycursor.fetchall()

	row_count=len(obj)
	i=0
	Label(frame, text = 'FEEDBACK VIEW WINDOW', font =('Candara Bold Italic', 16)).pack(side = TOP, pady = 10)
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

menu = Menu(root)
root.config(menu=menu)
file = Menu(menu)
menu.add_cascade(label="FEEDBACK", menu=file)
file.add_command(label="Feedback for College_level",activebackground="green",activeforeground="yellow",command=lambda *args:feedback_sql())
	


n=0

