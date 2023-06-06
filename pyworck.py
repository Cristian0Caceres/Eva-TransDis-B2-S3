import math

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

    if coeficiente_roce == 0:
        # Si no hay roce, la aceleración es la componente x del peso dividida por la masa
        aceleracion = pesox / masa
    else:
        # Calcular la normal (componente y del peso)
        N = pesoy
        # Calcular la fuerza de roce
        roce = N * coeficiente_roce
        # Calcular la fuerza neta (componente x del peso menos la fuerza de roce)
        Fneta = pesox - roce
        # Calcular la aceleración con roce
        aceleracion = Fneta / masa

    return aceleracion, masa, angulo

# Solicitar los datos al usuario
angulo = float(input("Ingrese el valor de uno de los ángulos: "))
masa = int(input("Ingrese el valor de la masa del objeto: "))
coeficiente_roce = float(input("Ingrese el coeficiente de roce (si no hay roce, ingrese 0): "))

# Calcular la aceleración utilizando la función calcular_aceleracion()
aceleracion = calcular_aceleracion(angulo, masa, coeficiente_roce)

# Imprimir el resultado
print(aceleracion)
