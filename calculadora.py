import re

print('Calculadora en python')
print('Teclea "salir" para terminar')

previous = 0
run = True

def realizaCalculo():
    
    # Accesar a variable run global para que pueda parar ejecucion al teclear 'salir'
    global run

    ecuacion = input('Teclea la operacion: ')
    if ecuacion == "salir":
        print('\n\nCerrando...... Hasta pronto!!')
        run = False
    else:
        print('Tecleaste la operacion: ', ecuacion)

# Empieza ejecución
while run:
    realizaCalculo()
