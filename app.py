from tkinter import *

#Windows
root = Tk()
root.title('Conversor')

def calcular(*args):
    try:
        value = float(dolar.get())
        p = float(value*200) 
        peso.set(p) #Le seteo el valor de P a pesos como variable y luego la muestro.
    except ValueError:
        peso.set('ERROR')

#Box
frame = Frame(root,padx=15,pady=15)
frame.grid(row=0,column=0)

dolar = StringVar() #We have 
dolar_input = Entry(frame,width=7, textvariable=dolar)
dolar_input.grid(column=1,row=0)

peso = StringVar()
peso.set('24242')
Label(frame, textvariable=peso).grid(column=1,row=1)


Button(frame,text='Calculate',command=calcular).grid(column=2,row=0,padx=10,pady=10)
Label(frame,text='Dolars').grid(column=0,row=0)
Label(frame,text='es igual a').grid(column=0,row=1)
Label(frame,text='pesos argentinos').grid(column=3,row=1)

dolar_input.focus() #Focusear el Inputs
root.bind("<Return>", calcular)

root.mainloop()