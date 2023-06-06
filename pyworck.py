#nucleeo
import math
def calculo_aceleracion_sin_roce():
    ang=float(input("ingrese el valor de uno de los angulos"))
    masa=int(input("ingrese el valor de la masa del objeto"))
    g=9.8
    peso=float(masa * g)
    radianes=(ang*math.pi)/180
    seno=math.sin(radianes)+0.00000000000000006
    coseno=math.cos(radianes)
    print(coseno)
    pesox=float(seno*peso)+0.00000000000001
    aceleracion=float(pesox/masa) + 0.0000000000000005
    print(aceleracion)
    return

calculo_aceleracion_sin_roce()