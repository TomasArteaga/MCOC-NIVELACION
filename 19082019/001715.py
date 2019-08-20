#minuto 17:15-19:15
name="YK"
height_m=2
weight_kg=73

bmi=weight_kg/(height_m**2)
print("bmi: ")
print(bmi)
if bmi<24:
    print(name)
    print("is not overweight")
else:
    print(name)
    print("is overweight")
