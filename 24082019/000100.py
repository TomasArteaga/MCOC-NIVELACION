# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 18:31:40 2019

@author: tomat
"""
# diccionario
# minuto 1:00-6:57
# lo que se esta haciendo diccionario asinado valores a variable de numeros y palabras 
d={}
# d={"George":24,"Tom":32}
d["George"]=24
d["Tom"]=32
d["Jenny"]=16
print(d["George"])

print(d["Tom"])
print(d["Jenny"])
d["Jenny"]=20
print(d["Jenny"])
d[10]=100
print(d[10])
# how to iterate over key-value pairs?
# se esta iterando los valores con sus nombres respectivos y su cantidad correspondiente
for key, value in d.items():
    print("key")
    print(key)
    print("value")
    print(value)
    print("")
    
