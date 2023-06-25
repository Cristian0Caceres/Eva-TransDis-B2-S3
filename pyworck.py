#Se importan las librerias necesarias para realizar el codigo.
import math
import tkinter as tk
from tkinter import messagebox

#Se crea una funcion en la cual se ejecuten las formulas necesarias en el plano inclinado, la cual trabaja con el ingreso del angulo, masa y coeficiente de roce.
def calcular_aceleracion(angulo, masa, coeficiente_roce=0):
    g = 9.8
    peso = masa * g
    radianes = (angulo * math.pi) / 180
    seno = math.sin(radianes)
    coseno = math.cos(radianes)
    pesox = seno * peso
    pesoy = coseno * peso

#Se especifican los limites del coeficiente de roce y el angulo, si se salen de esto, genere un error.
    if coeficiente_roce < 0 or coeficiente_roce > 1:
        raise ValueError("El coeficiente de roce debe estar entre 0 y 1")
    if angulo < 1 or angulo > 90:
        raise ValueError("El angulo debe estar entre 1 y 89 grados")
    
    #Se iguala el peso en Y con la fuerza normal.
    N = pesoy
    roce = round(N * coeficiente_roce, 2)
    # Calcular la fuerza neta (componente x del peso menos la fuerza de roce)
    fuerza_neta = round(pesox - roce, 2)
    fuerza_neta = max(fuerza_neta, 0)
    #Calcular la aceleración con roce.
    aceleracion = round(fuerza_neta / masa, 2)

#Se devueleven todos los datos por funcionalidad.
    return aceleracion, round(masa, 2), angulo, roce, fuerza_neta, round(pesox, 2), round(pesoy, 2)

#Se crea una funcion en la cual se centrara en la visualizacion del triangulo rectangulo del plano inclinado.
def dibujar_triangulo(angulo):
    canvas.delete("triangulo")

    radianes = math.radians(angulo)

    x1 = 40
    y1 = 450

    cateto_adyacente = 420
    cateto_opuesto = cateto_adyacente * math.tan(radianes)

    x2 = x1 + cateto_adyacente
    y2 = y1

    x3 = x1
    y3 = y1 - cateto_opuesto

    canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black", fill="lightblue", tags="triangulo")

    masa_size = 75
    masa_x = x1 + cateto_adyacente * 0.5 - masa_size * 0.5
    masa_y = y1 - cateto_opuesto * 0.63 - masa_size * 0.5

    # Calcula el ángulo de inclinación de la masa
    masa_angle = math.degrees(math.atan(cateto_opuesto / cateto_adyacente))

     # Rota la masa utilizando transformaciones de coordenadas
    cx = masa_x + masa_size / 2
    cy = masa_y + masa_size / 2

    canvas.create_polygon(
        rotate_point(masa_x, masa_y, cx, cy, masa_angle),
        rotate_point(masa_x + masa_size, masa_y, cx, cy, masa_angle),
        rotate_point(masa_x + masa_size, masa_y + masa_size, cx, cy, masa_angle),
        rotate_point(masa_x, masa_y + masa_size, cx, cy, masa_angle),
        outline="black", fill="red", tags="triangulo"
    )

def rotate_point(x, y, cx, cy, theta):
    # Aplica la fórmula de rotación a un punto
    cos_theta = math.cos(math.radians(theta))
    sin_theta = math.sin(math.radians(theta))

    nx = (x - cx) * cos_theta - (y - cy) * sin_theta + cx
    ny = (x - cx) * sin_theta + (y - cy) * cos_theta + cy

    return nx, ny     

#Se crea una funcion que se centrara en la ventana de Tkinter en donde el usuario podra ingresar los datos.
def calcular_button_click():
    try:
        angulo = float(angulo_entry.get())
        masa = float(masa_entry.get())
        coeficiente_roce = float(coeficiente_roce_entry.get())

        aceleracion, masa_objeto, angulo_objeto, roce, fuerza_neta, pesox, pesoy = calcular_aceleracion(angulo, masa, coeficiente_roce)

#Se escriben los reslutados con sus respectivas formulas del como se llegaron a estos.
        resultado_text.set(f"Aceleración: {aceleracion} m/s²\n"
                           f"Masa: {masa_objeto} kg \n"
                           f"Ángulo: {angulo_objeto} ° \n"
                           f"Fuerza de Roce = (N x μ) = {roce} N \n"
                           f"Fuerza Neta: P + N + Fr = {fuerza_neta} N \n"
                           f"Peso en X = P x sen(α) = {pesox} N \n"
                           f"Peso en Y = P x cos(α) = {pesoy} N ")
        
        dibujar_triangulo(angulo)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

#Se crea la ventana principal
window = tk.Tk()
window.title("Cálculo de Aceleración")

#Etiqueta y el campo de entrada para el ángulo
angulo_label = tk.Label(window, text="Ángulo:")
angulo_label.pack()
angulo_entry = tk.Entry(window)
angulo_entry.pack()

#Etiqueta y el campo de entrada para la masa
masa_label = tk.Label(window, text="Masa:")
masa_label.pack()
masa_entry = tk.Entry(window)
masa_entry.pack()

#Etiqueta y el campo de entrada para el coeficiente de roce
coeficiente_roce_label = tk.Label(window, text="Coeficiente de Roce:")
coeficiente_roce_label.pack()
coeficiente_roce_entry = tk.Entry(window)
coeficiente_roce_entry.pack()

#Botón de cálculo
calcular_button = tk.Button(window, text="Calcular", command=calcular_button_click)
calcular_button.pack()

#Variable de texto para mostrar el resultado
resultado_text = tk.StringVar()
resultado_label = tk.Label(window, textvariable=resultado_text)
resultado_label.pack()

canvas = tk.Canvas(window, width=500, height=500)
canvas.pack()

dibujar_triangulo(45)

#Se utiliza un loop para crear el bucle principal de la interfaz gráfica.
window.mainloop() 