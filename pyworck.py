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