from tkinter import *

window = Tk()
window.title("Arithmetic Calculator")
window.geometry("500x230")
window.config(bg="#F0FFFF")

def button_clicked():
    entry1.delete(0,END)
    
def button_backspace_clicked():
    entry1.delete(len(entry1.get())-1, END)

def button_number_clicked(number):
    current_text = entry1.get()
    entry1.delete(0, END)
    entry1.insert(0, current_text + str(number))

def button_operator(operator):
    current_text = entry1.get()
    entry1.delete(0,END)
    entry1.insert(0, current_text + str(operator))

def button_equals_clicked():
    try:
        result = eval(entry1.get())
        entry1.delete(0, END)
        entry1.insert(0, result)
    except:
        entry1.delete(0, END)
        entry1.insert(0, "Error")
    
    

frame = Frame(window)
frame.pack()

entry1 = Entry(frame,font=("Arial",10))
entry1.config(width=74)
entry1.grid(row=0, column=0, columnspan=4)

button_clear = Button(frame, text="Clear", font=("Arial Bold", 15),command=button_clicked)
button_clear.config(width=21,bg="#CDE2EA")
button_clear.grid(row=1, column=0, columnspan=2)

button_backspace = Button(frame, text="⌫", font=("Arial Bold", 15),command=button_backspace_clicked)
button_backspace.config(width=10 ,bg="#CDE2EA")
button_backspace.grid(row=1, column=2)

button_divide = Button(frame, text="÷", font=("Arial Bold", 15),command=lambda:button_operator("/"))
button_divide.config(width=10 ,bg="#CDE2EA")
button_divide.grid(row=1, column=3)

button7 = Button(frame, text="7", font=("Arial Bold", 15),command=lambda:button_number_clicked(7))
button7.config(width=10 ,bg="#CDE2EA")
button7.grid(row=2, column=0)

button8 = Button(frame, text="8", font=("Arial Bold", 15),command=lambda: button_number_clicked(8))
button8.config(width=10 ,bg="#CDE2EA")
button8.grid(row=2, column=1)

button9 = Button(frame, text="9", font=("Arial Bold", 15),command=lambda:button_number_clicked(9))
button9.config(width=10 ,bg="#CDE2EA")
button9.grid(row=2, column=2)

button_multiply = Button(frame, text="x", font=("Arial Bold", 15),command=lambda:button_operator("*"))
button_multiply.config(width=10 ,bg="#CDE2EA")
button_multiply.grid(row=2, column=3)

button4 = Button(frame, text="4", font=("Arial Bold", 15),command=lambda:button_number_clicked(4))
button4.config(width=10 ,bg="#CDE2EA")
button4.grid(row=3, column=0)

button5 = Button(frame, text="5", font=("Arial Bold", 15),command=lambda:button_number_clicked(5))
button5.config(width=10 ,bg="#CDE2EA")
button5.grid(row=3, column=1)

button6 = Button(frame, text="6", font=("Arial Bold", 15),command=lambda:button_number_clicked(6))
button6.config(width=10 ,bg="#CDE2EA")
button6.grid(row=3, column=2)

button_subtract = Button(frame, text="-", font=("Arial Bold", 15),command=lambda:button_operator("-"))
button_subtract.config(width=10 ,bg="#CDE2EA")
button_subtract.grid(row=3, column=3)

button1 = Button(frame, text="1", font=("Arial Bold", 15),command=lambda:button_number_clicked(1))
button1.config(width=10 ,bg="#CDE2EA")
button1.grid(row=4, column=0)

button2 = Button(frame, text="2", font=("Arial Bold", 15),command=lambda:button_number_clicked(2))
button2.config(width=10 ,bg="#CDE2EA")
button2.grid(row=4, column=1)

button3 = Button(frame, text="3", font=("Arial Bold", 15),command=lambda:button_number_clicked(3))
button3.config(width=10 ,bg="#CDE2EA")
button3.grid(row=4, column=2)

button_add = Button(frame, text="+", font=("Arial Bold", 15),command=lambda:button_operator("+"))
button_add.config(width=10 ,bg="#CDE2EA")
button_add.grid(row=4, column=3)

button0 = Button(frame, text="0", font=("Arial Bold", 15),command=lambda:button_number_clicked(0))
button0.config(width=10 ,bg="#CDE2EA")
button0.grid(row=5, column=0)

button_decimal = Button(frame, text=".", font=("Arial Bold", 15),command=lambda:button_operator("."))
button_decimal.config(width=10 ,bg="#CDE2EA")
button_decimal.grid(row=5, column=1)

button_equals = Button(frame, text="=", font=("Arial Bold", 15),command=button_equals_clicked)
button_equals.config(width=21 ,bg="#CDE2EA")
button_equals.grid(row=5, column=2, columnspan=2)

window.mainloop()
