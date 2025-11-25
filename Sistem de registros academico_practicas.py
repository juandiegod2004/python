# ----------------------------------------------------
#   REGISTRO ACADÉMICO BÁSICO
# Diseñe en Python un sistema básico
# que permita registrar varios estudiantes utilizando estructuras 
# de datos como listas y diccionarios. El programa debe almacenar
# el nombre del estudiante, su grado y su nota final. Posteriormente,
# el sistema debe mostrar en pantalla todos los registros almacenados 
# de forma organizada. Esta actividad busca comprender cómo Python puede
# utilizarse para representar, manipular y analizar información académica
# dentro de un entorno educativo
# ----------------------------------------------------



import sqlite3

print("=== Registro Académico con Base de Datos ===\n")

# 1. Conexión a la base de datos (si no existe, se crea)
conexion = sqlite3.connect("estudiantes.db")
cursor = conexion.cursor()

# 2. Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudiantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    grado TEXT NOT NULL,
    nota_final REAL NOT NULL
)
""")

conexion.commit()


# Función para registrar un estudiante
def registrar_estudiante():
    print("\n--- Nuevo Estudiante ---")
    nombre = input("Nombre del estudiante: ")
    grado = input("Grado: ")

    # Validación de la nota
    while True:
        try:
            nota = float(input("Nota final (0.0 - 5.0): "))
            if 0.0 <= nota <= 5.0:
                break
            else:
                print("⚠️ La nota debe estar entre 0.0 y 5.0.")
        except ValueError:
            print("❌ Ingrese un número válido.")

    nota = round(nota, 2)

    # Insertar en la base de datos
    cursor.execute("""
        INSERT INTO estudiantes (nombre, grado, nota_final)
        VALUES (?, ?, ?)
    """, (nombre, grado, nota))

    conexion.commit()
    print("✔ Estudiante guardado en la base de datos.\n")


# Bucle principal de registro
while True:
    registrar_estudiante()
    
    continuar = input("¿Desea registrar otro estudiante? (s/n): ").lower()
    if continuar != "s":
        break


# Mostrar reporte final desde la base de datos
print("\n===== REPORTE FINAL DE ESTUDIANTES (BD) =====")

cursor.execute("SELECT * FROM estudiantes")
resultados = cursor.fetchall()

for est in resultados:
    print(f"""
ID: {est[0]}
Nombre: {est[1]}
Grado: {est[2]}
Nota final: {est[3]:.2f}
------------------------------
""")


# Cerrar conexión
conexion.close()
print("Proceso finalizado. Base de datos actualizada.\n")
