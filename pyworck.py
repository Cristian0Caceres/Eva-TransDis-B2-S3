#nucleeo
import math
ang=float(input("ingrese el valor de uno de los angulos"))
masa=float(input("ingrese el valor de la masa del objeto"))
mu=float(input("ingrese el coeficiente de roce"))
g=9.8
peso=(masa * g)
print(f"peso:{peso}")
radianes=(ang*math.pi)/180
sen=math.sin(radianes)
cos=math.cos(radianes)
pesox=(sen*peso)
pesoy=(cos*peso)
N = pesoy
roce=(N*mu)
Fneta = (pesox-roce)
print(f"sen es {sen}")
print(f"cos es {cos}")
print(f"pesox es {pesox}")
print(f"pesoy es {pesoy}")
aceleracion=round((Fneta/masa),2)
print(aceleracion)
