import math 
verdad=True
def calculo_aceleracion_sin_roce():
    ang=float(input("ingrese el valor de uno de los angulos en caso del angulo ser decimal use [.] enves de [,]"))
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
    ang=float(input("ingrese el valor de uno de los angulos en caso del angulo ser decimal use [.] enves de [,]"))
    masa=int(input("ingrese el valor de la masa del objeto"))
    mu=float(input("ingrese el coeficiente de roce en caso del coeficiente de roce ser decimal use [.] enves de [,]"))
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
    #print(f"sen es {sen}")
    #print(f"cos es {cos}")
    #print(f"pesox es {pesox}")
    #print(f"pesoy es:{pesoy}")
    aceleracion=float(Fneta/masa)
    print(aceleracion+0.0000000000000005)
    return
while verdad==True:
    print("bienvenido al prototipo de calculo de plano inclinado ahora sin animaciones")
    print("inserte 1 si desea calcular con roce inserte 2 si desea calcular sin roce")
    eleccion=input("inserte su numero aqui: ")
    if eleccion=="1":
        calculo_aceleracion_con_roce()
        pregunta=input("desea continar?: ")
        if pregunta=="si":
            continue
        if pregunta=="no":
            verdad=False
        if eleccion=="2":
            calculo_aceleracion_sin_roce()
        pregunta=input("desea continar?: ")
        if pregunta=="si":
            continue
        if pregunta=="no":
            verdad=False