#nucleeo
import math
angulo=float(input("ingrese el valor de uno de los angulos"))
masa=int(input("ingrese el valor de la masa del objeto"))
coero=int(input("ingrese el coeficiente de roce"))
Gravedad=9.8
peso=float(masa * Gravedad)
print(peso)
radianes=(angulo*math.pi)/180
seno=math.sin(radianes)
print(seno+0.00000000000000006)
coseno=math.cos(angulo)
newtons=float(seno*peso)
print(newtons+0.00000000000001)
aceleracion=float(newtons/masa)
print(aceleracion+0.0000000000000005)

##
#FORMULAS CON ROCE

# Conversión de grados a radianes
angulo_rad = math.radians(angulo)

# Cálculo de la fuerza normal y el coeficiente de rozamiento
peso_y = peso * math.cos(angulo_rad)

# Cálculo de la fuerza de fricción
fuerza_friccion = coeficiente_roce * peso_y

# Impresión de resultados
print("Fuerza normal:", peso_y)
print("Coeficiente de rozamiento:", coeficiente_roce)
print("Fuerza de fricción:", fuerza_friccion)

# Gráfico del plano inclinado
x = np.array([0, math.sin(angulo_rad)])
y = np.array([0, math.cos(angulo_rad)])

plt.plot(x, y)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.xlabel("Distancia horizontal")
plt.ylabel("Distancia vertical")
plt.title("Plano inclinado")
plt.show()

