# ============================================================
# PROYECTO: JUSTA TIERRA - ALIMENTOS COOPERATIVOS JUNÍN
# SISTEMA DE GESTIÓN DE INVENTARIO (PRE-ENTREGA)
# ============================================================

def ejecutar_sistema():
    # Estructura obligatoria: Lista de sublistas
    inventario_justa_tierra = []

    while True:
        # Menú principal solicitado por la consigna
        print("\n" + "="*45)
        print("   JUSTA TIERRA - PANEL DE CONTROL")
        print("="*45)
        print("1. Agregar producto")
        print("2. Mostrar stock completo")
        print("3. Buscar producto por nombre")
        print("4. Eliminar producto")
        print("5. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == "1":
            # --- ALTA DE PRODUCTOS ---[cite: 1]
            nombre = input("Nombre del producto: ").strip().title() # title() queda mejor para nombres compuestos
            categoria = input("Categoría: ").strip().capitalize()
            
            # Validación de campos vacíos[cite: 1]
            if not nombre or not categoria:
                print("[!] Error: No se pueden registrar datos vacíos.")
                continue

            try:
                precio = int(input("Precio (sin centavos): "))
                if precio < 0:
                    print("[!] El precio debe ser un valor positivo.")
                    continue
                
                # Guardamos como sublista[cite: 1]
                inventario_justa_tierra.append([nombre, categoria, precio])
                print(f"[*] '{nombre}' agregado exitosamente.")
            except ValueError:
                print("[!] Error: El precio debe ser un número entero.")

        elif opcion == "2":
            # --- VISUALIZACIÓN NUMERADA ---[cite: 1]
            if not inventario_justa_tierra:
                print("\n[i] No hay productos en el inventario.")
            else:
                print("\n--- STOCK ACTUAL JUSTA TIERRA ---")
                for i, prod in enumerate(inventario_justa_tierra, start=1):
                    # Formato: Nombre - Categoría - $Precio[cite: 1]
                    print(f"{i}. {prod[0]} | Rubro: {prod[1]} | ${prod[2]}")

        elif opcion == "3":
            # --- BÚSQUEDA ROBUSTA ---[cite: 1]
            busqueda = input("¿Qué producto busca?: ").strip().lower()
            encontrados = False
            
            if not busqueda:
                print("[!] Ingrese un texto para buscar.")
                continue

            print(f"\nResultados para '{busqueda}':")
            for prod in inventario_justa_tierra:
                # Comparamos ambos en minúsculas para que encuentre 'Grapia' aunque busques 'a'[cite: 1]
                if busqueda in prod[0].lower():
                    print(f"-> {prod[0]} | Categoría: {prod[1]} | ${prod[2]}")
                    encontrados = True
            
            if not encontrados:
                print(f"[!] No se encontró nada que coincida con '{busqueda}'.")

        elif opcion == "4":
            # --- ELIMINACIÓN POR POSICIÓN (POP) ---[cite: 1]
            if not inventario_justa_tierra:
                print("\n[!] No hay productos para eliminar.")
                continue
                
            try:
                pos = int(input("Ingrese el número del producto a eliminar: "))
                indice = pos - 1
                
                # Validamos que el índice exista para evitar errores del programa[cite: 1]
                if 0 <= indice < len(inventario_justa_tierra):
                    eliminado = inventario_justa_tierra.pop(indice)
                    print(f"[*] Se ha eliminado: {eliminado[0]}")
                else:
                    print("[!] Posición inválida. Verifique el listado.")
            except ValueError:
                print("[!] Error: Ingrese un número de posición válido.")

        elif opcion == "5":
            print("\nCerrando sistema de Justa Tierra. ¡Hasta la próxima!")
            break
        else:
            print("[!] Opción no válida.")

if __name__ == "__main__":
    ejecutar_sistema()