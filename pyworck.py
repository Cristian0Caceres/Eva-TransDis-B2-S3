import math
import pygame as py
import tkinter as tk
import sys
from tkinter import messagebox
def calcular_aceleracion(angulo, masa, coeficiente_roce=0):
    # Gravedad
    g = 9.8
    # Calcular el peso del objeto
    peso = masa * g
    # Convertir el ángulo a radianes
    radianes = (angulo * math.pi) / 180
    # Calcular el seno y el coseno del ángulo
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    # Calcular las componentes x e y del peso
    pesox = seno * peso
    pesoy = coseno * peso


    if coeficiente_roce < 0 or coeficiente_roce > 1:
        raise ValueError("El coeficiente de roce debe estar entre 0 y 1")
    if angulo < 1 or angulo > 90:
        raise ValueError("El angulo debe estar entre 1 y 89 grados")
    # Calcular la normal (componente y del peso)
    N = pesoy
    # Calcular la fuerza de roce
    roce = round(N * coeficiente_roce, 2)
    # Calcular la fuerza neta (componente x del peso menos la fuerza de roce)
    fuerza_neta = round(pesox - roce, 2)
    # Calcular la aceleración con roce
    aceleracion = round(fuerza_neta / masa, 2)

    return aceleracion, round(masa, 2), angulo, roce, fuerza_neta, round(pesox, 2), round(pesoy, 2)

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

# Iniciar el bucle principal de la interfaz gráfica
window.mainloop()

py.init()

width=640
height=480
screen=py.display.set_mode((width,height))

py.display.set_caption("My Mame")

while True:
    for event in py.event.get():
        if event.type==py.quit:
            py.quit()
            sys.exit()

    py.display.update()
