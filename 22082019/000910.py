minuto 9:10-10:20
#tarea
#can you compute all multiples of 3 , 5 
#that are less than 100
# con el programa que se hizo se sumo todos los elemnto multiplo de 3 y de 5
print(list(range(1,100)))
total4=0
for i in range(1,100):
    if i%3==0 and i%5==0:
        total4+=i
print(total4)
        
