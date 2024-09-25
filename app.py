# Funciones de cálculo
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    else:
        return a / b

# Función para manejar la interacción con el usuario
def ejecutar_calculadora():
    while True:
        mostrar_menu()
        
        opcion = input("Ingrese el número de la opcion deseada: ")
        
        if opcion == '5':
            print("Saliendo de la calculadora.")
            break
        
        if opcion in ['1', '2', '3', '4']:
            try:
                a = float(input("Ingrese el primer numero: "))
                b = float(input("Ingrese el segundo numero: "))
                
                if opcion == '1':
                    resultado = sumar(a, b)
                    operacion = "sumar"
                elif opcion == '2':
                    resultado = restar(a, b)
                    operacion = "restar"
                elif opcion == '3':
                    resultado = multiplicar(a, b)
                    operacion = "multiplicar"
                elif opcion == '4':
                    resultado = dividir(a, b)
                    operacion = "dividir"
                
                print(f"El resultado de {operacion} {a} y {b} es: {resultado}")
            except ValueError:
                print("Por favor, ingrese valores numéricos validos.")
        else:
            print("Opcion no valida, intente de nuevo.")

# Función para mostrar el menú
def mostrar_menu():
    print("Seleccione una operacion:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

# Bloque para ejecutar la calculadora interactiva
if __name__ == "__main__":
    ejecutar_calculadora()
