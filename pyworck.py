import math
<<<<<<< Updated upstream
import tkinter as tk
=======
import customtkinter as tk
from customtkinter import *
>>>>>>> Stashed changes
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

<<<<<<< Updated upstream
=======
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
    imagen = "anguloplanoej1.png"
    imagen = Image.open(imagen)
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
    
>>>>>>> Stashed changes
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
