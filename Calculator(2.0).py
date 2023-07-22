from tkinter import *
import os
import customtkinter


root=customtkinter.CTk()
root.geometry("400x500+500+100")
root.title("Calculator")

def on_closing():
	os._exit(0)
root.protocol("WM_DELETE_WINDOW", on_closing)

data=StringVar(value="")
val=""
re=0

result=StringVar(value="")

input_label=customtkinter.CTkLabel(root,textvariable=data,bg_color="white",text_color="black",font=("arial",30),anchor=E)
input_label.pack(side=TOP,expand=TRUE,fill=BOTH)
output_label=customtkinter.CTkLabel(root,textvariable=result,bg_color="white",text_color="black",font=("arial",20),anchor=E)
output_label.pack(side=TOP,expand=TRUE,fill=BOTH)

def number_clicked(number):
	global val,re
	if (val=="" and number=="0"):
		return
	elif (( val != "" and val[-1] in "+-/*") and number=="0"):
		return

	val+=number
	data.set(val)
	try:
		re=eval(val)
		result.set(re)
	except Exception as e:
		pass
        

def clear():
	global val,re
	val=""
	re=""
	data.set(val)
	result.set(val)
	
def delete():
	global val,re
	if (val==""):
		return
	val=val[:-1]
	data.set(val)
	if (val==""):
		result.set("")
		return
	try:
		re=eval(val)
		result.set(re)
	except Exception as e:
		re=eval(val[:-1])
		result.set(re)

	

def opeators(op):
	global val
	if (val==""):
		return
	if (val[-1] in "-+/*" ):
		val=val[:-1]
		data.set(val)
	val+=op
	data.set(val)
	
	
def output():
	global val,re
	val=str(re)
	data.set(val)
	
# -----------------------------------------------------------

row1=customtkinter.CTkFrame(root)
row1.pack(expand=TRUE,fill=BOTH)

btn1=customtkinter.CTkButton(row1,text="1",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("1"))
btn1.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn2=customtkinter.CTkButton(row1,text="2",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("2"))
btn2.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn3=customtkinter.CTkButton(row1,text="3",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("3"))
btn3.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn4=customtkinter.CTkButton(row1,text="+",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:opeators("+"))
btn4.pack(side=LEFT,expand=TRUE,fill=BOTH)

# -------------------------------------------------------------


row2=customtkinter.CTkFrame(root)
row2.pack(expand=TRUE,fill=BOTH)


btn1=customtkinter.CTkButton(row2,text="4",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("4"))
btn1.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn2=customtkinter.CTkButton(row2,text="5",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("5"))
btn2.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn3=customtkinter.CTkButton(row2,text="6",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("6"))
btn3.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn4=customtkinter.CTkButton(row2,text="-",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:opeators("-"))
btn4.pack(side=LEFT,expand=TRUE,fill=BOTH)

# --------------------------------------------------------------

row3=customtkinter.CTkFrame(root)
row3.pack(expand=TRUE,fill=BOTH)


btn1=customtkinter.CTkButton(row3,text="7",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("7"))
btn1.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn2=customtkinter.CTkButton(row3,text="8",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("8"))
btn2.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn3=customtkinter.CTkButton(row3,text="9",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("9"))
btn3.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn4=customtkinter.CTkButton(row3,text="/",width=50,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:opeators("/"))
btn4.pack(side=LEFT,expand=TRUE,fill=BOTH)

# ---------------------------------------------------------------

row4=customtkinter.CTkFrame(root)
row4.pack(expand=TRUE,fill=BOTH)


btn1=customtkinter.CTkButton(row4,text="C",width=79.6,corner_radius=0,anchor=CENTER,font=("ariel",20),command=clear)
btn1.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn2=customtkinter.CTkButton(row4,text="0",width=79.6,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:number_clicked("0"))
btn2.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn3=customtkinter.CTkButton(row4,text="=",width=79.6,corner_radius=0,anchor=CENTER,font=("ariel",20),command=output)
btn3.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn4=customtkinter.CTkButton(row4,text="*",width=79.6,corner_radius=0,anchor=CENTER,font=("ariel",20),command=lambda:opeators("*"))
btn4.pack(side=LEFT,expand=TRUE,fill=BOTH)

btn5=customtkinter.CTkButton(row4,text="Del",width=79.6,corner_radius=0,anchor=CENTER,font=("ariel",20),command=delete)
btn5.pack(side=LEFT,expand=TRUE,fill=BOTH)


root.mainloop()