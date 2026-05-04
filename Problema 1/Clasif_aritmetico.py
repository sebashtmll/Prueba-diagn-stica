"""
PROBLEMA 1: CLASIFICADOR DE EXPRESIONES ARITMÉTICAS
Lenguajes y Compiladores - UNEG
Clasifica cada componente de una expresión aritmética
"""

import re

def clasificar_expresion(expresion):

    # El strip() es para eliminar los espacios al inicio y al final
    expresion = expresion.strip()
    
    # Patrones de reconocimiento con regex y tokens 
    patrones = [
        (r'^(\d+(?:\.\d+)?)', 'NUMERO'),      # Números enteros o reales
        (r'^([+\-*/])', 'OPERADOR'),           # Operadores + - * /
        (r'^(\()', 'PAREN_IZQ'),               # Paréntesis izquierdo
        (r'^(\))', 'PAREN_DER'),               # Paréntesis derecho
        (r'^([a-zA-Z_][a-zA-Z0-9_]*)', 'OPERANDO'),  # Identificadores válidos
        (r'^(\S+)', 'ERROR')                   # Cualquier otro carácter
    ]
    
    posicion = 0
    componentes = []
    parentesis_balance = 0
    
    while posicion < len(expresion):
        # Saltar espacios en blanco
        if expresion[posicion] == ' ':
            posicion += 1
            continue
            
        # Tomar la subcadena desde la posición actual
        subcadena = expresion[posicion:]
        encontrado = False
        
        for patron, tipo in patrones:
            match = re.match(patron, subcadena)
            if match:
                token = match.group(1)
                componentes.append((tipo, token))
                posicion += len(token)
                encontrado = True
                
                # Contar paréntesis para balanceo
                if tipo == 'PAREN_IZQ':
                    parentesis_balance += 1
                elif tipo == 'PAREN_DER':
                    parentesis_balance -= 1
                break
        
        if not encontrado:
            print("\n❌ Error: Carácter no reconocido en la expresión")
            return None
    
    return componentes, parentesis_balance

def mostrar_resultado(componentes, balance):

    print("\n" + "="*70)
    print(" " * 20 + "RESULTADO DEL ANÁLISIS LÉXICO")
    print("="*70)
    print(f"{'TIPO':<15} {'TOKEN':<20}")
    print("-"*70)
    
    for tipo, token in componentes:
        print(f"{tipo:<15} {token:<20}")
    
    print("-"*70)
    
    # Mostrar balance de paréntesis
    if balance == 0:
        print("✅ PARÉNTESIS BALANCEADOS")
    elif balance > 0:
        print(f"❌ FALTAN {balance} PARÉNTESIS DERECHO(S)")
    else:
        print(f"❌ SOBRAN {abs(balance)} PARÉNTESIS DERECHO(S)")
    
    print("="*70)

def main():
    """Función principal del programa"""
    print("\n" + "="*70)
    print(" " * 15 + "CLASIFICADOR DE EXPRESIONES")
    print("="*70)
    print("\n EXPRESIONES A CLASIFICAR:")
    print("   • NUMERO: Entero o real con '.' (sin signo)")
    print("   • OPERANDO: No inicia con número (ej: VALOR, A, CONT)")
    print("   • OPERADOR: + - * /")
    print("   • PAREN_IZQ: (")
    print("   • PAREN_DER: )")
    print("-"*70)
    
    while True:
        expresion = input("\nIngrese la expresión aritmética (o 'salir' para terminar): ")
        
        if expresion.lower() == 'salir':
            print("\n👋 ¡Hasta luego!")
            break
        
        if not expresion.strip():
            print("❌ Expresión vacía. Intente de nuevo.")
            continue
        
        resultado = clasificar_expresion(expresion)
        
        if resultado:
            componentes, balance = resultado
            mostrar_resultado(componentes, balance)

if __name__ == "__main__":
    main()