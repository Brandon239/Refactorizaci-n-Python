def menu_principal():
    while True:
        print('Seleccione el proceso que desea realizar:')
        print('1: Ingresar puntos de evaluación y comentario')
        print('2: Verificar resultados hasta ahora')
        print('3: Salir')
        num = input()

        if num.isdecimal():
            num = int(num)
            if num == 1:
                ingresar_evaluacion()
            elif num == 2:
                mostrar_resultados()
            elif num == 3:
                print('Salir')
                break
            else:
                print('Por favor, ingrese un número del 1 al 3')
        else:
            print('Por favor, ingrese un número del 1 al 3')

def ingresar_evaluacion():
    while True:
        print('Ingrese una evaluación del 1 al 5:')
        puntos = input()
        if puntos.isdecimal():
            puntos = int(puntos)
            if puntos <= 0 or puntos > 5:
                print('Por favor, ingrese un número del 1 al 5')
            else:
                print('Ingrese un comentario:')
                comentario = input()
                post = f'Puntos: {puntos} Comentario: {comentario}'
                with open("data.txt", 'a') as file:
                    file.write(f'{post}\n')
                break
        else:
            print('El punto de evaluación debe ser un número')

def mostrar_resultados():
    print('Resultados hasta ahora:')
    try:
        with open("data.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print('No hay resultados anteriores.')

if __name__ == "__main__":
    menu_principal()
