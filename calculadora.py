import re

print('Calculadora en python')
print('Teclea "salir" para terminar')

previa = 0
run = True

def realizaCalculo():
    
    # Accesar a variable run global para que pueda parar ejecucion al teclear 'salir'
    # y a previa para mantener operacion aritmetica actual
    global run
    global previa

    ecuacion = input('Teclea la operacion: ')
    if ecuacion == "salir":
        print('\n\nCerrando...... Hasta pronto!!')
        run = False
    else:
        ecuacion = re.sub('[a-zA-Z,:.\'()" "]', '', ecuacion)
        previa = eval(ecuacion)
        print('Tecleaste la operacion: ', previa)

# Empieza ejecución
while run:
    realizaCalculo()
