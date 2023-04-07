import tkinter
from  tkinter import *
window= tkinter.Tk()
window.title("Mile to Kilometer Converter.")
window.minsize(width=500,height=300)
window.config(padx=200,pady=200)
Miles=tkinter.Label(text="Miles",font=("Arial",18))
Miles.grid(column=2,row=0)
km_value=tkinter.Label(text="0",font=("Arial",18))
km_value.grid(column=1,row=1)
km_value.config(pady=25, padx=5)
Km=tkinter.Label(text="Km",font=("Arial",18))
Km.grid(column=2,row=1)
result=tkinter.Label(text="is equal to",font=("Arial",18))
result.grid(column=0,row=1)

def button_clicked():
   input_text=input.get()
   Out_put=round((int(input_text)*1.60934),2)
   km_value.config(text=Out_put)
   print("I got clicked")
button=Button(text="Calculate",command=button_clicked)
button.grid(column=1,row=2)
input=Entry(width=10)
input.grid(column=1,row=0)
print(input.get())









window.mainloop()