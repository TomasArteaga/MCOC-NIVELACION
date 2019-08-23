#minuto 6:10-7:45
 # hubo un problema cuando hacemos una lista con solo numero positivo , por lo tanto este algoritmo nos va a permitir a solucionar esto
given_list=[5,4,4,3,1]
total3=0
i=0
while i<len(given_list) and given_list[i]>0:
    total3 += given_list[i]
    i+=1
print(total3)  
