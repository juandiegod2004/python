# Realice un programa en Python que permita a un docente registrar el nombre de un estudiante, su grado y tres notas parciales. 
# El programa debe calcular el promedio final del estudiante y determinar si aprueba o reprueba (estándar mínimo: 3.0).
# Finalmente, presente los resultados de manera clara en pantalla.

print("=== Sistema sencillo de notas ===\n")

# Paso 1: Registrar datos del estudiante
nombre = input("Ingrese el nombre del estudiante: ")
grado = input("Ingrese el grado del estudiante: ")

# Paso 2: Ingresar notas con validación
print("\nIngrese las notas del estudiante (0.0 a 5.0):")

def pedir_nota(num):
    while True:
        try:
            nota = float(input(f"Nota {num}: "))
            if 0.0 <= nota <= 5.0:
                return nota
            else:
                print("⚠️ La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("❌ Ingrese un número válido.")

n1 = pedir_nota(1)
n2 = pedir_nota(2)
n3 = pedir_nota(3)

# Paso 3: Calcular promedio flotante con dos decimales
promedio = round((n1 + n2 + n3) / 3, 2)

# Paso 4: Determinar estado académico
estado = "APROBADO" if promedio >= 3.0 else "REPROBADO"

# Paso 5: Mostrar resultados finales
print("\n===== RESULTADOS =====")
print(f"Estudiante: {nombre}")
print(f"Grado: {grado}")
print(f"Notas ingresadas: {n1:.2f}, {n2:.2f}, {n3:.2f}")
print(f"Promedio final: {promedio:.2f}")
print(f"Estado académico: {estado}")

print("\nPrograma finalizado con éxito.\n")

# Mensaje pedagógico de cierre
print("\nEste programa ayuda a los docentes a realizar rápidamente cálculos de notas,")
print("fomenta el uso de herramientas digitales y fortalece el pensamiento computacional.\n")
