import tkinter as tk
import math

# Funciones para la calculadora
def clear():
    pantalla.delete(0, tk.END)

def button_click(valor):
    pantalla.insert(tk.END, valor)

def calculate():
    try:
        expresion = pantalla.get()
        resultado = eval(expresion)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, resultado)
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

def calculate_raiz():
    try:
        num = float(pantalla.get())
        resultado = math.sqrt(num)
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, resultado)
    except ValueError:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

def calculate_potencia():
    try:
        expresion = pantalla.get()
        resultado = eval(expresion + "**2")
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, resultado)
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

def calculate_seno():
    try:
        num = float(pantalla.get())
        resultado = math.sin(math.radians(num))
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, resultado)
    except ValueError:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

def memoria_guardar():
    try:
        memoria.set(pantalla.get())
        pantalla.delete(0, tk.END)
    except Exception as e:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

def memoria_sumar():
    try:
        valor = float(pantalla.get())
        memoria_actual = float(memoria.get())
        resultado = valor + memoria_actual
        memoria.set(str(resultado))
    except ValueError:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

def memoria_restar():
    try:
        valor = float(pantalla.get())
        memoria_actual = float(memoria.get())
        resultado = memoria_actual - valor
        memoria.set(str(resultado))
    except ValueError:
        pantalla.delete(0, tk.END)
        pantalla.insert(tk.END, "Error")

def memoria_mostrar():
    pantalla.delete(0, tk.END)
    pantalla.insert(tk.END, memoria.get())

# Crear ventana
ventana = tk.Tk()
ventana.title("Calculadora Científica")

# Pantalla de la calculadora
pantalla = tk.Entry(ventana, width=30, font=('Arial', 16))
pantalla.grid(row=0, column=0, columnspan=4)

# Variable de memoria
memoria = tk.StringVar()

# Definir botones
botones = [
    {'text': 'MC', 'row': 1, 'column': 0},
    {'text': 'MR', 'row': 1, 'column': 1},
    {'text': 'M+', 'row': 1, 'column': 2},
    {'text': 'M-', 'row': 1, 'column': 3},
    {'text': 'C', 'row': 2, 'column': 0},
    {'text': '√', 'row': 2, 'column': 1},
    {'text': 'x^2', 'row': 2, 'column': 2},
    {'text': '/', 'row': 2, 'column': 3},
    {'text': '7', 'row': 3, 'column': 0},
    {'text': '8', 'row': 3, 'column': 1},
    {'text': '9', 'row': 3, 'column': 2},
    {'text': '*', 'row': 3, 'column': 3},
    {'text': '4', 'row': 4, 'column': 0},
    {'text': '5', 'row': 4, 'column': 1},
    {'text': '6', 'row': 4, 'column': 2},
    {'text': '-', 'row': 4, 'column': 3},
    {'text': '1', 'row': 5, 'column': 0},
    {'text': '2', 'row': 5, 'column': 1},
    {'text': '3', 'row': 5, 'column': 2},
    {'text': '+', 'row': 5, 'column': 3},
    {'text': '0', 'row': 6, 'column': 0, 'columnspan': 2},
    {'text': '.', 'row': 6, 'column': 2},
    {'text': '=', 'row': 6, 'column': 3}
]

# Crear botones en la ventana
for boton in botones:
    if boton['text'] == '=':
        tk.Button(ventana, text=boton['text'], width=11, height=2, command=calculate).grid(row=boton['row'], column=boton['column'], columnspan=boton.get('columnspan', 1))
    elif boton['text'] == 'C':
        tk.Button(ventana, text=boton['text'], width=5, height=2, command=clear).grid(row=boton['row'], column=boton['column'], columnspan=boton.get('columnspan', 1))
    elif boton['text'] == '√':
        tk.Button(ventana, text=boton['text'], width=5, height=2, command=calculate_raiz).grid(row=boton['row'], column=boton['column'])
    elif boton['text'] == 'x^2':
        tk.Button(ventana, text=boton['text'], width=5, height=2, command=calculate_potencia).grid(row=boton['row'], column=boton['column'])
    elif boton['text'] == 'MC':
        tk.Button(ventana, text=boton['text'], width=5, height=2, command=memoria_guardar).grid(row=boton['row'], column=boton['column'])
    elif boton['text'] == 'M+':
        tk.Button(ventana, text=boton['text'], width=5, height=2, command=memoria_sumar).grid(row=boton['row'], column=boton['column'])
    elif boton['text'] == 'M-':
        tk.Button(ventana, text=boton['text'], width=5, height=2, command=memoria_restar).grid(row=boton['row'], column=boton['column'])
    elif boton['text'] == 'MR':
        tk.Button(ventana, text=boton['text'], width=5, height=2, command=memoria_mostrar).grid(row=boton['row'], column=boton['column'])
    else:
        tk.Button(ventana, text=boton['text'], width=5, height=2, command=lambda valor=boton['text']: button_click(valor)).grid(row=boton['row'], column=boton['column'])

# Configuración adicional
pantalla.focus()  # Hacer que el cursor aparezca en la calculadora

# Función para reconocer la tecla Enter
def enter_key(event):
    calculate()

ventana.bind('<Return>', enter_key)  # Vincular la tecla Enter a la función enter_key

# Ejecutar bucle de eventos
ventana.mainloop()
