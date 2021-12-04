from tkinter import *

#Windows
root = Tk()
root.title('Conversor')
root.geometry('150x200')

def calcular():
    pass


#Box
frame = Frame(root,padx=15,pady=15)
frame.grid(row=0,column=0)

dolar = StringVar()
dolar_input = Entry(frame,width=7, textvariable=dolar)
dolar_input.grid(column=1,row=0)

peso = StringVar()
peso.set('24242')
Label(frame, textvariable=peso).grid(column=1,row=1)


Button(frame,textvariable='Calcular',command=calcular).grid(column=2,row=2)
Label(frame,text='dolares').grid(column=0,row=0)
Label(frame,text='es igual a').grid(column=0,row=1)


root.mainloop()