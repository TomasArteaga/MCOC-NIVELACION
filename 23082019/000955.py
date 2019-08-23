 #minuto 9:55-12:30      
# se esta recorriendo con while true los elementos de la lista positivos 
given_list2=[5,4,4,3,1,-2,-3,-5] 
total5=0
i=0
while True:
    total5+=given_list2[i]
    i+=1
    if given_list2[i] <=0:
        break
print (total5)
