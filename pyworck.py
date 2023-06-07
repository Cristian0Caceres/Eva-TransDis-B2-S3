#nucleeo
import math
def calculo_aceleracion_sin_roce():
    ang=float(input("ingrese el valor de uno de los angulos"))
    masa=int(input("ingrese el valor de la masa del objeto"))
    g=9.8
    peso=float(masa * g)
    radianes=(ang*math.pi)/180
    seno=math.sin(radianes)+0.00000000000000006

    pesox=float(seno*peso)+0.00000000000001
    aceleracion=float(pesox/masa) + 0.0000000000000005
    print(aceleracion)
    return

def calculo_aceleracion_con_roce():
    import math
    ang=float(input("ingrese el valor de uno de los angulos"))
    masa=int(input("ingrese el valor de la masa del objeto"))
    mu=float(input("ingrese el coeficiente de roce"))
    g=9.8
    peso=float(masa * g)
    #print(f"peso:{peso}")
    radianes=(ang*math.pi)/180
    sen=math.sin(radianes)+0.00000000000000006
    cos=math.cos(radianes)
    pesox=float(sen*peso)+0.00000000000001
    pesoy=float(cos*peso)
    N = pesoy
    roce=float(N*mu)
    Fneta=(pesox-roce)
    roce=float(N*mu)
    #print(f"sen es {sen}")
    #print(f"cos es {cos}")
    #print(f"pesox es {pesox}")
    #print(f"pesoy es:{pesoy}")
    aceleracion=float(Fneta/masa)
    print(aceleracion+0.0000000000000005)
    return

print("¿desea hacer el calculo con o sin roce?")
print("ingrese '1' se lo desea con roce o '2' si lo desea sin este")
opcion = int(input())
if opcion == 1:
    calculo_aceleracion_con_roce()
elif opcion == 2:
    calculo_aceleracion_sin_roce()