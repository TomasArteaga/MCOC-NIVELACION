#minutos 10:30-14:10
#bmi_calculadora
nombre1="yo"
altura1_metros=1.72
peso1_kg=72
nombre2="hermana"
altura2_metros=1.67
peso2_kg=65
nombre3="hermano"
altura3_metros=1.73
peso3_kg=75
def bmi_calculadora(nombre,altura_metros,peso_kg):
    bmi=peso_kg/(altura_metros**2)
    print("bmi:")
    print (bmi)
    if bmi<25:
        return nombre+ "no esta en sobrepeso"
    else:
        return nombre+ "si esta en sobrepeso"
resultado1=bmi_calculadora(nombre1,altura1_metros,peso1_kg)
resultado2=bmi_calculadora(nombre2,altura2_metros,peso2_kg)
resultado3=bmi_calculadora(nombre3,altura3_metros,peso3_kg)
print(resultado1)
print(resultado2)
print(resultado3)
