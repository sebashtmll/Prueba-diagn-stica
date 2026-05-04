# Proyecto: Lenguajes y Compiladores - UNEG 🎓

Este repositorio contiene la resolución de tres problemas prácticos en Python para la asignatura de **Lenguajes y Compiladores** de la Universidad Nacional Experimental de Guayana (UNEG).

## 👨‍💻 Autor
* **Sebastián Ortiz**

## 🚀 Contenido del Proyecto

El proyecto consta de tres scripts independientes, cada uno resolviendo un problema específico mediante análisis léxico, validación de cadenas y lógica matemática:

### 1. Clasificador de Expresiones Aritméticas (`Clasif_aritmetico.py`)
Un analizador léxico que toma una expresión aritmética y clasifica cada uno de sus componentes mediante expresiones regulares.
* **Tokens reconocidos:** `NUMERO`, `OPERADOR`, `PAREN_IZQ`, `PAREN_DER`, `OPERANDO`, `ERROR`.
* Verifica el balance correcto de los paréntesis.

### 2. Validador de Notación FEN (`not_fen.py`)
Un programa que valida si una cadena cumple estrictamente con el formato FEN (Forsyth-Edwards Notation), utilizado para describir posiciones en un tablero de ajedrez.
* Valida los 6 campos del estándar FEN.
* Muestra una representación visual del tablero en consola.

### 3. Conjetura de Collatz (`conjetura_collatz.py`)
Verifica la famosa conjetura matemática de Collatz para un intervalo de números enteros positivos `[p, q]`.
* Aplica las reglas de n/2 (para pares) y 3n+1 (para impares).
* Genera estadísticas de pasos, máximos y mínimos dentro del rango ingresado.

## 🛠️ Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Bibliotecas:** `re` (Estándar de Python, no requiere instalación externa).

## 📦 Instalación y Uso

Dado que el proyecto utiliza únicamente bibliotecas nativas de Python, no es necesario instalar dependencias adicionales. Solo necesitas tener **Python 3.x** instalado en tu sistema.

### Para ejecutar manualmente:
Clona este repositorio y ejecuta el script que desees usando la terminal:

```bash
git clone 
cd tu-repositorio

# Ejecutar el Problema 1
python Clasif_aritmetico.py

# Ejecutar el Problema 2
python not_fen.py

# Ejecutar el Problema 3
python conjetura_collatz.py