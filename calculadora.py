import re

print('Calculadora en python')

previous = 0
run = True

def realizaCalculo():
    ecuacion = input('Teclea la operacion: ')
    print('Tecleaste la operacion: ', ecuacion)

while run:
    realizaCalculo()
