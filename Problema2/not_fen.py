"""
PROBLEMA 2: VALIDADOR DE NOTACIÓN FEN (Forsyth-Edwards Notation)
Lenguajes y Compiladores - UNEG
Valida si una cadena cumple con el formato FEN de ajedrez
"""

import re

def validar_posicion_piezas(campo_posicion):
    """ 
    valida que la posición de las piezas en el tablero sea correcta
    """

    # Dividir en 8 filas
    filas = campo_posicion.split('/')
    
    # Verificar que haya exactamente 8 filas
    if len(filas) != 8:
        return False, f"Debe tener 8 filas, tiene {len(filas)}"
    
    # Conjunto de piezas válidas
    piezas_validas = set('prnbqkPRNBQK')
    
    for i, fila in enumerate(filas, 1):
        contador_casillas = 0
        
        for caracter in fila:
            if caracter.isdigit():
                # Los números indican casillas vacías consecutivas
                contador_casillas += int(caracter)
            elif caracter in piezas_validas:
                # Pieza válida
                contador_casillas += 1
            else:
                return False, f"Carácter '{caracter}' inválido en fila {i}"
        
        # Cada fila debe tener exactamente 8 casillas
        if contador_casillas != 8:
            return False, f"Fila {i} tiene {contador_casillas} casillas, debe tener 8"
    
    return True, "Posición de piezas válida"


def validar_fen(cadena_fen):
    """
    Valida si una cadena está en notación FEN (Forsyth-Edwards Notation)
    """
    # Limpiar la cadena
    cadena_fen = cadena_fen.strip()
    
    # Una cadena FEN válida tiene exactamente 6 campos separados por espacios
    partes = cadena_fen.split()
    
    if len(partes) != 6:
        return False, f"❌ Debe tener exactamente 6 campos, tiene {len(partes)}"
    
    # 1. Validar POSICIÓN DE LAS PIEZAS
    valido, mensaje = validar_posicion_piezas(partes[0])
    if not valido:
        return False, f"❌ Error en posición de piezas: {mensaje}"
    
    # 2. Validar QUIÉN JUEGA (w = blancas, b = negras)
    turno = partes[1]
    if turno not in ['w', 'b']:
        return False, "❌ Turno debe ser 'w' (blancas) o 'b' (negras)"
    
    # 3. Validar ENROQUE (KQkq o -)
    enroque = partes[2]
    caracteres_validos_enroque = set('KQkq')
    if enroque != '-':
        for c in enroque:
            if c not in caracteres_validos_enroque:
                return False, f"❌ Enroque inválido: '{enroque}'"
    
    # 4. Validar CASILLA AL PASO
    al_paso = partes[3]
    # Patrón: letra a-h seguida de 3 o 6, o -
    patron_al_paso = r'^([a-h][36]|-$)'
    if not re.match(patron_al_paso, al_paso):
        return False, f"❌ Casilla al paso inválida: '{al_paso}'"
    
    # 5. Validar CONTADOR DE MEDIO MOVIMIENTOS
    medio_movimiento = partes[4]
    if not medio_movimiento.isdigit():
        return False, "❌ Contador medio movimiento debe ser número entero"
    
    # 6. Validar NÚMERO DE MOVIMIENTO COMPLETO
    movimiento_completo = partes[5]
    if not (movimiento_completo.isdigit() and int(movimiento_completo) >= 1):
        return False, "❌ Número de movimiento debe ser entero positivo (≥ 1)"
    
    return True, "✅ Cadena FEN VÁLIDA"

def mostrar_informacion_fen(cadena_fen):
    """
    Muestra información detallada de una cadena FEN válida
    """
    partes = cadena_fen.strip().split()
    
    print("\n" + "="*70)
    print(" " * 20 + "INFORMACIÓN DE LA CADENA FEN")
    print("="*70)
    
    # Mostrar tablero visualmente
    print("\n📋 TABLERO:")
    print("-"*50)
    filas = partes[0].split('/')
    nombres_filas = ['8', '7', '6', '5', '4', '3', '2', '1']
    
    for i, (fila, nombre) in enumerate(zip(filas, nombres_filas)):
        fila_visual = ""
        for caracter in fila:
            if caracter.isdigit():
                fila_visual += "." * int(caracter)
            else:
                # Mapear piezas a símbolos
                simbolos = {
                    'p': '♟', 'r': '♜', 'n': '♞', 'b': '♝', 'q': '♛', 'k': '♚',
                    'P': '♙', 'R': '♖', 'N': '♘', 'B': '♗', 'Q': '♕', 'K': '♔'
                }
                fila_visual += simbolos.get(caracter, caracter)
        print(f"   {nombre} │ {fila_visual}")
    print("-"*50)
    
    # Mostrar otros campos
    turno_display = "Blancas" if partes[1] == 'w' else "Negras"
    print(f"\n🎲 TURNO: {turno_display}")
    print(f"🏰 ENROQUE: {partes[2] if partes[2] != '-' else 'No disponible'}")
    print(f"🎯 AL PASO: {partes[3] if partes[3] != '-' else 'No disponible'}")
    print(f"⏱️  MEDIO MOVIMIENTO: {partes[4]}")
    print(f"🔢 MOVIMIENTO COMPLETO: {partes[5]}")
    print("="*70)

def main():
    """Función principal del programa"""
    print("\n" + "="*70)
    print(" " * 15 + "PROBLEMA 2: VALIDADOR DE NOTACIÓN FEN")
    print("="*70)
    
    print("\n📌 ¿QUÉ ES FEN?")
    print("   Forsyth-Edwards Notation - Notación estándar para posiciones de ajedrez")
    print("\n📋 FORMATO (6 campos):")
    print("   1. Posición piezas (8 filas separadas por /)")
    print("   2. Turno (w = blancas, b = negras)")
    print("   3. Enroque (KQkq = disponibles, - = ninguno)")
    print("   4. Casilla al paso (ej: a3, b6, -)")
    print("   5. Contador medio movimiento (desde último avance de peón o captura)")
    print("   6. Movimiento completo (inicia en 1)")
    print("-"*70)
    
    print("\n📝 EJEMPLO VÁLIDO (Posición inicial):")
    print("   rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    print("-"*70)
    
    while True:
        print("\n" + "-"*70)
        cadena_fen = input("\nIngrese la cadena FEN a validar (o 'salir' para terminar): ")
        
        if cadena_fen.lower() == 'salir':
            print("\n👋 ¡Hasta luego!")
            break
        
        if not cadena_fen.strip():
            print("❌ Cadena vacía. Intente de nuevo.")
            continue
        
        valido, mensaje = validar_fen(cadena_fen)
        
        print("\n" + "="*70)
        print(" " * 20 + "RESULTADO DE VALIDACIÓN")
        print("="*70)
        
        if valido:
            print(f"✅ {mensaje}")
            mostrar_informacion_fen(cadena_fen)
        else:
            print(f"❌ {mensaje}")

if __name__ == "__main__":
    main()
    
    #r1bqkbnr/pppp1ppp/2n5/1B2p3/4P3/5N2/PPPP1PPP/RNBQK2R b KQkq - 3 3 
    #8/8/4k3/8/2K5/5Q2/8/8 w - - 0 1 
    #2rq1rk1/pp1bppbp/3p2p1/8/2P1P1n1/1PN2P2/P2QB1PP/2R1NRK1 w - - 1 15