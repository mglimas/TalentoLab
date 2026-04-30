# ==========================================
# Programa: Generador de Tarjeta Digital
# Empresa: TalentoLab
# ==========================================

print("--- SISTEMA DE REGISTRO DE TALENTOLAB ---")
print("Por favor, ingrese los datos del cliente.\n")

# PASO 1: ENTRADA Y ALMACENAMIENTO
# input() solicita datos por consola y los devuelve como string (texto).
nombre_cliente = input("Ingrese el nombre: ")
apellido_cliente = input("Ingrese el apellido: ")
correo_cliente = input("Ingrese el correo electrónico: ")

# PASO 2: CONVERSIÓN DE TIPOS (Casting)
# La edad debe ser un valor numérico para futuras operaciones.
# Convertimos el string ingresado a un número entero (int).
edad_texto = input("Ingrese la edad: ")
edad_cliente = int(edad_texto)

print("\nGenerando tarjeta de presentación...\n")

# PASO 3: SALIDA DE DATOS Y FORMATO VISUAL
# Utilizamos multiplicaciones de strings para los bordes y \t (tabulación)
# para alinear los datos en columnas de forma prolija.
print("=" * 40)
print("\tTARJETA DE PRESENTACIÓN")
print("=" * 40)
print(f"Nombre:\t\t{nombre_cliente} {apellido_cliente}")
print(f"Edad:\t\t{edad_cliente} años")
print(f"Contacto:\t{correo_cliente}")
print("=" * 40)