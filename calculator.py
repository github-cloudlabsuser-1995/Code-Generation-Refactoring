# Calculadora básica en Python

def sumar(a, b):
    """Devuelve la suma de dos números."""
    return a + b

def restar(a, b):
    """Devuelve la resta de dos números."""
    return a - b

def multiplicar(a, b):
    """Devuelve el producto de dos números."""
    return a * b

def dividir(a, b):
    """Devuelve la división de dos números. Maneja la división por cero."""
    if b == 0:
        return "Error: División por cero no permitida."
    return a / b

def main():
    """Función principal para interactuar con el usuario."""
    print("Bienvenido a la calculadora básica.")
    print("Operaciones disponibles: sumar, restar, multiplicar, dividir")
    
    # Solicitar al usuario la operación y los números
    operacion = input("Introduce la operación que deseas realizar: ").strip().lower()
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
    except ValueError:
        print("Error: Por favor, introduce valores numéricos válidos.")
        return

    # Realizar la operación seleccionada
    if operacion == "sumar":
        print(f"Resultado: {sumar(num1, num2)}")
    elif operacion == "restar":
        print(f"Resultado: {restar(num1, num2)}")
    elif operacion == "multiplicar":
        print(f"Resultado: {multiplicar(num1, num2)}")
    elif operacion == "dividir":
        print(f"Resultado: {dividir(num1, num2)}")
    else:
        print("Error: Operación no reconocida.")

# Ejecutar la función principal
if __name__ == "__main__":
    main()