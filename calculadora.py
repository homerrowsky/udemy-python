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

    # Nueva operacion o Mantiene resultado anterior para seguir realizando operaciones
    if previa == 0:
        ecuacion = input('Teclea la operacion: ')
    else:
        ecuacion = input(str(previa))


    # Salir si usuario teclea "salir"
    # Mediante regex se filtra lo tecleado para evitar ejecucion arbitraria
    # de código. Se evalúa expresión y se almacena en var 'previa' ( en caso
    # de que ya exista, se reusa para añadirle la expresión tecleada)
    if ecuacion == "salir":
        print('\n\nCerrando...... Hasta pronto!!')
        run = False
    else:
        ecuacion = re.sub('[a-zA-Z,:\'()" "]', '', ecuacion)
        if previa == 0:
           previa = eval(ecuacion)
        else:
            previa = eval(str(previa) + ecuacion)
        print(previa)

# Empieza ejecución
while run:
    realizaCalculo()
