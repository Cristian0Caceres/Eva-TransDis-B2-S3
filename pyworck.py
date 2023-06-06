#nucleeo
import math
ang=float(input("ingrese el valor de uno de los angulos"))
masa=int(input("ingrese el valor de la masa del objeto"))
mu=float(input("ingrese el coeficiente de roce"))
g=9.8
peso=float(masa * g)
print(f"peso:{peso}")
radianes=(ang*math.pi)/180
sen=math.sin(radianes)+0.00000000000000006
cos=math.cos(ang)
pesox=float(sen*peso)+0.00000000000001
pesoy=float(cos*peso)
N = pesoy
roce=float(N*mu)
print(f"sen es {sen}")
print(f"cos es {cos}")
print(f"pesox es {pesox}")
print(f"pesoy es:{pesoy}")
aceleracion=float(peso/masa)
print(aceleracion+0.0000000000000005)
