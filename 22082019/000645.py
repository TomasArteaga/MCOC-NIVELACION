#minuto 6:45-9:10
# 1) como se calcula el resto
# 2) se esta condicionando el recorrido de la lista haciendo que se sumen los numeros que tengan resto 0, los numeros de 1 al 7
print(5%3)
print(1%3)
print(6%3)
total3=0
for i in range(1,8):
    if i%3==0:
        total3+=i
print(total3)
