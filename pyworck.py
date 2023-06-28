#Se importan las librerias necesarias para realizar el codigo.
import math
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont

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

#Se crea una funcion en la cual se centrara en la visualizacion del triangulo rectangulo y la masa del plano inclinado.
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
    background_color = window.cget("bg")

    if angulo > 50:
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black", fill=background_color, tags="triangulo")
    else:
        canvas.create_polygon(x1, y1, x2, y2, x3, y3, outline="black", fill="lightblue", tags="triangulo")

    masa_size = 75
    masa_distance = 0.519  # Porcentaje de la hipotenusa donde se ubicará el cuadrado

    masa_x = x1 + cateto_adyacente * masa_distance - masa_size * 0.5
    masa_y = y1 - cateto_opuesto * masa_distance - masa_size

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
        outline="black", fill="pink", tags="triangulo"
    )

    # Dibujar las fuerzas en la masa cuadrada
    # Dibujar la fuerza normal
    fuerza_normal_x = masa_x + masa_size * 1.68
    fuerza_normal_y = masa_y - 50
    canvas.create_line(masa_x + masa_size / 2, masa_y + masa_size / 2, fuerza_normal_x, fuerza_normal_y, arrow=tk.LAST, fill='red')
    canvas.create_text(fuerza_normal_x, fuerza_normal_y - 10, text="Fuerza normal")

    # Dibujar la fuerza de roce
    fuerza_roce_x = masa_x - 50
    fuerza_roce_y = masa_y + masa_size / 120.50
    canvas.create_line(masa_x + masa_size / 2, masa_y + masa_size / 2, fuerza_roce_x, fuerza_roce_y, arrow=tk.LAST, fill='green')
    canvas.create_text(fuerza_roce_x - 50, fuerza_roce_y, text="Fuerza de roce")

    # Dibujar la fuerza peso
    fuerza_peso_x = masa_x + masa_size / 2
    fuerza_peso_y = masa_y + masa_size + 50
    canvas.create_line(masa_x + masa_size / 2, masa_y + masa_size / 2, fuerza_peso_x, fuerza_peso_y, arrow=tk.LAST, fill='blue')
    canvas.create_text(fuerza_peso_x, fuerza_peso_y + 10, text="Fuerza peso")

def rotate_point(x, y, cx, cy, theta):
    # Aplica la fórmula de rotación a un punto
    cos_theta = math.cos(math.radians(theta))
    sin_theta = math.sin(math.radians(theta))

    nx = (x - cx) * cos_theta - (y - cy) * sin_theta + cx
    ny = (x - cx) * sin_theta + (y - cy) * cos_theta + cy

    return nx, ny


def on_mass_change(event):
    mass = mass_scale.get()
    update_arrows(mass)

def update_arrows(mass):
    canvas.delete("arrow")

    for angle in angles:
        arrow_length = mass * 10  # Ajusta el factor de escala según tus necesidades
        x = arrow_length * math.cos(math.radians(angle))
        y = arrow_length * math.sin(math.radians(angle))
        canvas.create_line(center_x, center_y, center_x + x, center_y + y, arrow="last", tags="arrow")

def clear_arrows():
    for arrow_id in arrow_ids:
        canvas.delete(arrow_id)
    arrow_ids.clear()

root = Tk()

canvas = Canvas(root, width=400, height=400)
canvas.pack()

mass_scale = Scale(root, from_=1, to=10, orient=HORIZONTAL, command=on_mass_change)
mass_scale.pack()

angles = [45, 90, 135, 180, 225, 270, 315, 360]
center_x, center_y = 200, 200

update_arrows(1)  # Inicialmente, la masa es 1

root.mainloop()

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

def abrir_ventana_ayuda_angulo():
    ventana_ayuda = tk.Toplevel(window)
    ventana_ayuda.title("¿Qué es el ángulo?")
    ventana_ayuda.geometry("450x350")  # Ajusta las dimensiones de la ventana según tus necesidades

    # Contenido textual
    titulo_label = tk.Label(ventana_ayuda, text="¿Qué representa el ángulo?", font=("Arial", 20, "bold"))
    titulo_label.pack()

    contenido_text = tk.Label(ventana_ayuda, justify="left", font=("Arial", 16))

    #Párrafo
    contenido_text.configure(text=contenido_text.cget("text") + "\n\nLa función del angulo en el plano inclinado es determinar la facilidad")
    contenido_text.configure(text=contenido_text.cget("text") + "\n\ncon la cual el objeto se desliza por el plano (no es el unico que lo determina)")
    contenido_text.configure(text=contenido_text.cget("text") + "\n\nentre mayor sea el angulo, mas facil sera para el objeto deslizarce ")
    contenido_text.configure(text=contenido_text.cget("text") + "\n\ny entre menor sea, mas dificil se le hara, este angulo puede llegar a los 360 grados")
    contenido_text.configure(text=contenido_text.cget("text") + "\n\npero en el caso del plano inclinado solo hasta los 90 grados")
    contenido_text.configure(text=contenido_text.cget("text") + "\n")
    contenido_text.configure(text=contenido_text.cget("text") + "\n\nEjemplo visual del como efecta el angulo a la masa:")
    
    contenido_text.pack()

    #Imagen
    imagen_path = "anguloplanoej1.png"  # Reemplaza con la ruta de tu imagen
    imagen = Image.open(imagen_path)
    imagen = imagen.resize((800, 300))  # Ajusta el tamaño de la imagen según tus necesidades
    imagen_tk = ImageTk.PhotoImage(imagen)
    imagen_label = tk.Label(ventana_ayuda, image=imagen_tk)
    imagen_label.image = imagen_tk  # Mantén una referencia a la imagen para evitar que sea eliminada por el recolector de basura
    imagen_label.pack()

    # Ajustar tamaño de la ventana al contenido
    ventana_ayuda.update_idletasks()
    ventana_ayuda.geometry(f"{ventana_ayuda.winfo_width()*2}x{ventana_ayuda.winfo_height()*2}")

    
def abrir_ventana_ayuda_masa():
    ventana_ayuda = tk.Toplevel(window)
    ventana_ayuda.title("¿Que es la masa?")
    ayuda_texto = tk.Text(ventana_ayuda)
    ayuda_texto.insert(tk.END, "aqui debe estar la ayuda")
    ayuda_texto.pack()

def abrir_ventana_ayuda_coeficiente_roce():
    ventana_ayuda = tk.Toplevel(window)
    ventana_ayuda.title("¿Que es el Coeficiente de Roce?")
    ayuda_texto = tk.Text(ventana_ayuda)
    ayuda_texto.insert(tk.END, "aqui debe estar la ayuda")
    ayuda_texto.pack()


def create_round_button(master, command=None):
    # Crear una imagen redonda con un signo de interrogación blanco en el centro
    size = 30
    background_color = "#4AC0CD"
    question_mark_color = "white"
    
    image = Image.new("RGBA", (size, size), background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial", 18)
    text = "?"
    text_width, text_height = draw.textsize(text, font=font)
    text_position = ((image.width - text_width) // 2, (image.height - text_height) // 2)
    draw.text(text_position, text, fill=question_mark_color, font=font)

    # Crear una máscara redonda
    mask = Image.new("L", (size, size), 0)
    draw_mask = ImageDraw.Draw(mask)
    draw_mask.ellipse((0, 0, size, size), fill=255)

    # Aplicar la máscara a la imagen
    image.putalpha(mask)

    # Convertir la imagen de Pillow a un objeto PhotoImage de Tkinter
    photo = ImageTk.PhotoImage(image)

    # Crear el botón y asignar la imagen
    button = tk.Button(master, image=photo, relief="flat", bd=0, command=command)
    button.image = photo

    return button
    
# Crear la ventana principal
window = tk.Tk()
window.title("Cálculo de Aceleración")

# Frame para los campos de entrada y botones
input_frame = tk.Frame(window)
input_frame.pack(side="top", pady=10)

# Grupo para el ángulo
angulo_group = tk.Frame(input_frame)
angulo_label = tk.Label(angulo_group, text="Ángulo:")
angulo_entry = tk.Entry(angulo_group)
round_button1 = create_round_button(angulo_group, command=abrir_ventana_ayuda_angulo)
angulo_group.pack(side="top"), angulo_label.pack(side="top"), angulo_entry.pack(side="top"), round_button1.pack(side="top")


# Grupo para la masa
masa_group = tk.Frame(input_frame)
masa_label = tk.Label(masa_group, text="Masa:")
masa_entry = tk.Entry(masa_group)
round_button2 = create_round_button(masa_group, command=abrir_ventana_ayuda_masa)
masa_group.pack(side="top"), masa_label.pack(side="top"), masa_entry.pack(side="top"), round_button2.pack(side="top")

# Grupo para el coeficiente de roce
coeficiente_roce_group = tk.Frame(input_frame)
coeficiente_roce_label = tk.Label(coeficiente_roce_group, text="Coeficiente de Roce:")
coeficiente_roce_entry = tk.Entry(coeficiente_roce_group)
round_button3 = create_round_button(coeficiente_roce_group, command=abrir_ventana_ayuda_coeficiente_roce)
coeficiente_roce_group.pack(side="top"), coeficiente_roce_label.pack(side="top"), coeficiente_roce_entry.pack(side="top"), round_button3.pack(side="top")

#Botón de cálculo
calcular_button = tk.Button(window, text="Calcular", command=calcular_button_click)
calcular_button.pack()

#Variable de texto para mostrar el resultado
resultado_text = tk.StringVar()
resultado_label = tk.Label(window, textvariable=resultado_text)
resultado_label.pack()

canvas = tk.Canvas(window, width=600, height=450)
canvas.pack()

dibujar_triangulo(45)

#Se utiliza un loop para crear el bucle principal de la interfaz gráfica.
window.mainloop() 