print("===================AFP=============")
nombre=input("Ingrese su Nombre Porfavor:  ")
sb=float(input("Ingrese su salario bruto porfavor:  "))
afp=input("Ingrese el afp al que pertenece porfavor:  ")

afp=integra
afp=profuturo
afp=horizonte

if afp==integra:
    dcto= sb*0.12
else:
    if afp==profuturo:
        dcto=sb*0.13
    else:
        dcto=sb*0.11
sn=sb-dcto

print(f"El sueldo neto del sr(a) {nombre} es", sn)   
