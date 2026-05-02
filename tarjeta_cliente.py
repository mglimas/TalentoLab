# ==========================================
# Programa: Generador de Tarjeta Digital
# Empresa: TalentoLab
# ==========================================

print("--- SISTEMA DE REGISTRO DE TALENTOLAB ---")
print("Por favor, ingrese los datos del cliente.\n")

# PASO 1: ENTRADA Y ALMACENAMIENTO
nombre_cliente = input("Ingrese el nombre: ")
apellido_cliente = input("Ingrese el apellido: ")
correo_cliente = input("Ingrese el correo electrónico: ")

# PASO 2: CONVERSIÓN DE TIPOS (Casting)
edad_texto = input("Ingrese la edad: ")
edad_cliente = int(edad_texto)

# PASO 3: PROCESAMIENTO REQUERIDO (Jornada 4)
# 1. Formateo de texto: Capitalización correcta
nombre_cliente = nombre_cliente.strip().title()
apellido_cliente = apellido_cliente.strip().title()

# 2. Validación de correo: Sin espacios y con una sola @
if " " not in correo_cliente and correo_cliente.count("@") == 1:
    estado_correo = "Válido"
else:
    estado_correo = "Inválido"

# 3. Clasificación etaria
if edad_cliente < 15:
    rango_etario = "Niño/a"
elif 15 <= edad_cliente <= 18:
    rango_etario = "Adolescente"
else:
    rango_etario = "Adulto/a"

print("\nGenerando tarjeta de presentación...\n")

# PASO 4: SALIDA DE DATOS ACTUALIZADA
print("=" * 40)
print("\tTARJETA DE PRESENTACIÓN")
print("=" * 40)
print(f"Nombre:\t\t{nombre_cliente} {apellido_cliente}")
print(f"Edad:\t\t{edad_cliente} años ({rango_etario})")
print(f"Contacto:\t{correo_cliente}")
print(f"Estado Email:\t{estado_correo}")
print("=" * 40)