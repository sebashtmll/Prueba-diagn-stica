"""
PROBLEMA 3: CONJETURA DE COLLATZ
Lenguajes y Compiladores - UNEG
Alumno: Sebastián Ortiz.
Verifica la conjetura de Collatz para un intervalo de números enteros
"""

def collatz_paso(n):
    """
    Aplica un paso de la conjetura de Collatz
    """
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def verificar_collatz(n):
    """
    Verifica la conjetura de Collatz para un número n
    """
    if n <= 0:
        return [], 0
    
    secuencia = [n]
    pasos = 0
    
    while n != 1:
        n = collatz_paso(n)
        secuencia.append(n)
        pasos += 1
    
    return secuencia, pasos

def mostrar_secuencia(secuencia, pasos, numero):
    """
    Muestra la secuencia de Collatz
    """
    print(f"n = {numero}:")
    
    # Mostrar secuencia de forma compacta si es muy larga
    if len(secuencia) <= 15:
        secuencia_str = " → ".join(str(x) for x in secuencia)
    else:
        primeros = " → ".join(str(x) for x in secuencia[:6])
        ultimos = " → ".join(str(x) for x in secuencia[-4:])
        secuencia_str = f"{primeros} → ... → {ultimos}"
    
    print(f"   Secuencia: {secuencia_str}")
    print(f"   Pasos hasta llegar a 1: {pasos}")
    
    # Verificar que termina en 1
    if secuencia[-1] == 1:
        print("   ✅ Conjetura CUMPLIDA")
    else:
        print("   ❌ Conjetura NO CUMPLIDA (nunca debería pasar)")

def mostrar_estadisticas_intervalo(secuencias, total_pasos, max_pasos_num, min_pasos_num):
    """
    Muestra estadísticas del intervalo analizado
    """
    print("\n" + "="*70)
    print(" " * 20 + "ESTADÍSTICAS DEL INTERVALO")
    print("="*70)
    print(f"   Total de números analizados: {len(secuencias)}")
    print(f"   Total de pasos acumulados: {total_pasos}")
    print(f"   Promedio de pasos: {total_pasos / len(secuencias):.2f}")
    print(f"   Número con MÁS pasos: {max_pasos_num}")
    print(f"   Número con MENOS pasos: {min_pasos_num}")

def main():
    """Función principal del programa"""
    print("\n" + "="*70)
    print(" " * 20 + "PROBLEMA 3: CONJETURA DE COLLATZ")
    print("="*70)
    
    print("\n📌 ¿QUÉ ES LA CONJETURA DE COLLATZ?")
    print("   Para cualquier número entero positivo n se cumple que:")
    print("   • Si n es par → n = n / 2")
    print("   • Si n es impar → n = 3n + 1")
    print("   • Siempre se llega a 1 sin importar el número inicial")
    print("-"*70)
    print("⚠️  REGLA DE DEMOSTRACIÓN: q ≥ 100p")
    print("   (El límite superior debe ser al menos 100 veces el límite inferior)")
    print("="*70)
    
    while True:
        try:
            print("\n" + "-"*40)
            p = int(input("Ingrese el límite inferior p (entero positivo): "))
            q = int(input("Ingrese el límite superior q (entero positivo): "))
            
            # Validar números positivos
            if p <= 0 or q <= 0:
                print("\n❌ ERROR: Los números deben ser enteros positivos (mayores que 0)")
                continue
            
            # Validar que p sea menor o igual a q
            if p > q:
                print("\n❌ ERROR: El límite inferior (p) debe ser menor o igual al límite superior (q)")
                continue
            
            # Verificar regla q ≥ 100p
            if q >= 100 * p:
                print(f"\n✅ Regla cumplida: {q} ≥ {100*p}")
            else:
                print(f"\n⚠️  ADVERTENCIA: La regla NO se cumple ({q} < {100*p})")
                print("   La demostración matemática puede no ser concluyente")
                
                continuar = input("   ¿Desea continuar de todas formas? (s/n): ").lower()
                if continuar != 's':
                    continue
            
            break
            
        except ValueError:
            print("\n❌ ERROR: Por favor ingrese números enteros válidos")
    
    print("\n" + "="*70)
    print(" " * 15 + "VERIFICANDO LA CONJETURA DE COLLATZ")
    print("="*70)
    print(f"\n🔍 Analizando intervalo: [{p}, {q}]")
    print("   Esto puede tomar un momento...")
    
    secuencias = []
    total_pasos = 0
    max_pasos = -1
    min_pasos = float('inf')
    max_pasos_num = None
    min_pasos_num = None
    
    for numero in range(p, q + 1):
        secuencia, pasos = verificar_collatz(numero)
        secuencias.append(secuencia)
        total_pasos += pasos
        
        if pasos > max_pasos:
            max_pasos = pasos
            max_pasos_num = numero
        
        if pasos < min_pasos:
            min_pasos = pasos
            min_pasos_num = numero
        
        mostrar_secuencia(secuencia, pasos, numero)
    
    # Mostrar estadísticas
    mostrar_estadisticas_intervalo(secuencias, total_pasos, max_pasos_num, min_pasos_num)
    
    # Conclusión
    print("\n" + "="*70)
    print(" " * 15 + "CONCLUSIÓN FINAL")
    print("="*70)
    print("\n✅ La conjetura de Collatz se CUMPLE para todos los números")
    print(f"   analizados en el intervalo [{p}, {q}]")
    print("\n   Todos los números analizados llegaron a 1 después de")
    print("   aplicar repetidamente las reglas:")
    print("   • Si es par → dividir entre 2")
    print("   • Si es impar → multiplicar por 3 y sumar 1")
    print("="*70)
    
    input("\n📌 Presione Enter para salir...")

if __name__ == "__main__":
    main()
    
