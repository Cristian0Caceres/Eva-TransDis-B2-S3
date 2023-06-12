import math
import tkinter as tk
from tkinter import messagebox

def calcular_aceleracion(angulo, masa, coeficiente_roce=0):
    g = 9.8
    peso = masa * g
    radianes = (angulo * math.pi) / 180
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    pesox = seno * peso
    pesoy = coseno * peso

    if coeficiente_roce < 0 or coeficiente_roce > 1:
        raise ValueError("El coeficiente de roce debe estar entre 0 y 1")
    if angulo < 1 or angulo > 90:
        raise ValueError("El angulo debe estar entre 1 y 89 grados")
    
    N = pesoy
    roce = round(N * coeficiente_roce, 2)
    # Calcular la fuerza neta (componente x del peso menos la fuerza de roce)
    fuerza_neta = round(pesox - roce, 2)
    fuerza_neta = max(fuerza_neta, 0)
    # Calcular la aceleración con roce
    aceleracion = round(fuerza_neta / masa, 2)

    return aceleracion, round(masa, 2), angulo, roce, fuerza_neta, round(pesox, 2), round(pesoy, 2)

def dibujar_triangulo(angulo):
    canvas.delete("triangulo")  # Borra cualquier triángulo dibujado previamente

    # Convertir el ángulo a radianes
    radianes = math.radians(angulo)

    # Coordenadas del vértice del ángulo agudo
    x1 = 50
    y1 = 200

    # Longitud del cateto adyacente y cateto opuesto
    cateto_adyacente = 150
    cateto_opuesto = cateto_adyacente * math.tan(radianes)

    # Coordenadas del segundo vértice (en el cateto adyacente)
    x2 = x1 + cateto_adyacente
    y2 = y1

    # Coordenadas del tercer vértice (en el cateto opuesto)
    x3 = x1
    y3 = y1 - cateto_opuesto

    # Dibujar el triángulo en el lienzo
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black", fill="lightblue", tags="triangulo")

def calcular_button_click():
    try:
        angulo = float(angulo_entry.get())
        masa = float(masa_entry.get())
        coeficiente_roce = float(coeficiente_roce_entry.get())

        aceleracion, masa_objeto, angulo_objeto, roce, fuerza_neta, pesox, pesoy = calcular_aceleracion(angulo, masa, coeficiente_roce)

        resultado_text.set(f"Aceleración: {aceleracion}\n"
                           f"Masa: {masa_objeto}\n"
                           f"Ángulo: {angulo_objeto}\n"
                           f"Fuerza de Roce: {roce}\n"
                           f"Fuerza Neta: {fuerza_neta}\n"
                           f"Peso en X: {pesox}\n"
                           f"Peso en Y: {pesoy}")
        
        dibujar_triangulo(angulo)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
window = tk.Tk()
window.title("Cálculo de Aceleración")

# Etiqueta y campo de entrada para el ángulo
angulo_label = tk.Label(window, text="Ángulo:")
angulo_label.pack()
angulo_entry = tk.Entry(window)
angulo_entry.pack()

# Etiqueta y campo de entrada para la masa
masa_label = tk.Label(window, text="Masa:")
masa_label.pack()
masa_entry = tk.Entry(window)
masa_entry.pack()

# Etiqueta y campo de entrada para el coeficiente de roce
coeficiente_roce_label = tk.Label(window, text="Coeficiente de Roce:")
coeficiente_roce_label.pack()
coeficiente_roce_entry = tk.Entry(window)
coeficiente_roce_entry.pack()

# Botón de cálculo
calcular_button = tk.Button(window, text="Calcular", command=calcular_button_click)
calcular_button.pack()

# Variable de texto para mostrar el resultado
resultado_text = tk.StringVar()
resultado_label = tk.Label(window, textvariable=resultado_text)
resultado_label.pack()

canvas = tk.Canvas(window, width=300, height=250)
canvas.pack()

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop() 