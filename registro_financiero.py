# ==========================================
# Programa: Registro Financiero Mensual
# Empresa: TalentoLab - Clase 05
# ==========================================

def main():
    # Inicialización de variables (Conceptos Clase 05)[cite: 1, 2]
    total_acumulado = 0.0  # Acumulador para el total[cite: 1, 2]
    contador_meses = 1     # Contador para controlar el bucle[cite: 1, 2]
    ingresos_lista = []    # Lista para almacenar los valores (opcional)[cite: 1, 2]
    LIMITE_MESES = 6

    print("--- SISTEMA DE REGISTRO FINANCIERO ---")

    # 1. Registro de ingresos mediante bucle while[cite: 1, 2]
    while contador_meses <= LIMITE_MESES:
        try:
            # Entrada de datos
            ingreso = float(input(f"Ingrese los ingresos del mes {contador_meses}: "))

            # Validación de números positivos[cite: 1, 2]
            if ingreso >= 0:
                total_acumulado += ingreso  # Actualización del acumulador
                ingresos_lista.append(ingreso) # Agregamos a la lista[cite: 1, 2]
                contador_meses += 1         # Incremento del contador[cite: 2]
            else:
                # Requerimiento: Mensaje de error y reintento[cite: 1, 2]
                print("[!] Valor no válido. El ingreso debe ser un número positivo.")
        
        except ValueError:
            print("[!] Error de tipo: Por favor, ingrese un valor numérico.")

    # 2. Cálculo de métricas
    promedio_mensual = total_acumulado / LIMITE_MESES

    # 3. Salida de resultados
    print("\n" + "=" * 40)
    print("\tRESUMEN FINANCIERO FINAL")
    print("=" * 40)
    print(f"Total acumulado (6 meses): ${total_acumulado:,.2f}")
    print(f"Promedio mensual:          ${promedio_mensual:,.2f}")
    print("=" * 40)

if __name__ == "__main__":
    main()