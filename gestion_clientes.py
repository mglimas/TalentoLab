# ==========================================
# Programa: Procesamiento de Clientes
# Empresa: TalentoLab - Clase 06
# ==========================================

def procesar_lista_clientes():
    # Parte 1: Creación de la lista de nombres
    # Incluimos ejemplos variados para testear la validación y el formato
    clientes = ["ana", "JUAN", "", "mArIa", "  ", "pedro"]

    print("--- INICIO DE PROCESAMIENTO ---")

    # Parte 1.2: Recorrido con bucle for y range()
    # Usamos range(len(lista)) para obtener los índices numéricos
    for i in range(len(clientes)):
        # Limpiamos espacios laterales y verificamos si está vacío
        nombre_actual = clientes[i].strip()
        posicion = i + 1  # Ajustamos para que empiece en 1 y no en 0

        # Parte 1.3: Validación de nombre vacío
        if nombre_actual == "":
            print(f"Cliente {posicion}: [ALERTA] Nombre no válido")
        else:
            # Parte 2 (Optativa): Normalización con .capitalize()[cite: 4]
            nombre_formateado = nombre_actual.capitalize()
            print(f"Cliente {posicion}: {nombre_formateado}")

    print("--- FIN DEL PROCESAMIENTO ---")

if __name__ == "__main__":
    procesar_lista_clientes()
    