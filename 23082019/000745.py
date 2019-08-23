#minuto 7:45-9:55
 # se estar recorriendo con un ciclo for sumado los elemento positivos de la lista
given_list2=[5,4,4,3,1,-2,-3,-5]
total4=0
for element in given_list2:
    if element <=0:
        break
    total4+=element
print(total4)
