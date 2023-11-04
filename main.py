from tkinter import Tk, Button, Entry

# Configuración ventana principal
root = Tk()
root.title("Calculadora POO")
root.resizable(0,0)
root.geometry("300x250")

# Configuración pantalla de salida 
pantalla = Entry(root, width=40, bg="black", fg="white", borderwidth=0, font=("arial", 18, "bold"))
pantalla.grid(row=0, column=0, columnspan=100, padx=1, pady=1)

#Que evento?
def presionar_boton(char):
    current = pantalla.get()
    pantalla.insert(len(pantalla.get()),char)
def igual():
    estring = pantalla.get()
    if len(estring.split("+"))>1:
        num1 = float(estring.split("+")[0])
        num2 = float(estring.split("+")[1])
        resultado = num1 + num2
        pantalla.delete(0,len(pantalla.get()))
        pantalla.insert(0,str(resultado))
    elif len(estring.split("-"))>1:
        num1 = float(estring.split("-")[0])
        num2 = float(estring.split("-")[1])
        resultado = num1 - num2
        pantalla.delete(0,len(pantalla.get()))
        pantalla.insert(0,str(resultado))
    elif len(estring.split("*"))>1:
        num1 = float(estring.split("*")[0])
        num2 = float(estring.split("*")[1])
        resultado = num1 * num2
        pantalla.delete(0,len(pantalla.get()))
        pantalla.insert(0,str(resultado))
    elif len(estring.split("/"))>1:
        num1 = float(estring.split("/")[0])
        num2 = float(estring.split("/")[1])
        resultado = num1 / num2
        pantalla.delete(0,len(pantalla.get()))
        pantalla.insert(0,str(resultado))

# Configuración botones
boton_1 = Button(root, text="1", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="1": presionar_boton(button)).grid(row=1, column=0, padx=1, pady=1)
boton_2 = Button(root, text="2", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="2": presionar_boton(button)).grid(row=1, column=1, padx=1, pady=1)
boton_3 = Button(root, text="3", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="3": presionar_boton(button)).grid(row=1, column=2, padx=1, pady=1)
boton_4 = Button(root, text="4", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="4": presionar_boton(button)).grid(row=2, column=0, padx=1, pady=1)
boton_5 = Button(root, text="5", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="5": presionar_boton(button)).grid(row=2, column=1, padx=1, pady=1)
boton_6 = Button(root, text="6", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="6": presionar_boton(button)).grid(row=2, column=2, padx=1, pady=1)
boton_7 = Button(root, text="7", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="7": presionar_boton(button)).grid(row=3, column=0, padx=1, pady=1)
boton_8 = Button(root, text="8", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="8": presionar_boton(button)).grid(row=3, column=1, padx=1, pady=1)
boton_9 = Button(root, text="9", width=9, height=3, bg="white", fg="red", borderwidth=0, cursor="hand2",command=lambda button="9": presionar_boton(button)).grid(row=3, column=2, padx=1, pady=1)
boton_igual = Button(root, text="=", width=20, height=3, bg="red", fg="white", borderwidth=0, cursor="hand2",command=igual).grid(row=4, column=0, columnspan=2, padx=1, pady=1)
boton_punto = Button(root, text=".", width=9, height=3, bg="spring green", fg="black", cursor="hand2",command=lambda button=".": presionar_boton(button), borderwidth=0).grid(row=4, column=2, padx=1, pady=1)
boton_mas = Button(root, text="+", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda button="+": presionar_boton(button)).grid(row=1, column=3, padx=1, pady=1)
boton_menos = Button(root, text="-", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda button="-": presionar_boton(button)).grid(row=2, column=3, padx=1, pady=1)
boton_multiplicacion = Button(root, text="*",  width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda button="*": presionar_boton(button)).grid(row=3, column=3, padx=1, pady=1)
boton_division = Button(root, text="/", width=9, height=3, bg="deep sky blue", fg="black", borderwidth=0, cursor="hand2",command=lambda button="/": presionar_boton(button)).grid(row=4, column=3, padx=1, pady=1)

root.mainloop()