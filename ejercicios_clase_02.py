# EJERCICIOS CLASE 02
#
# =======================================================================================================================================================
# Ejercicio 1. Dar algoritmos para resolver los siguientes problemas y determinar su complejidad temporal y espacial en peor caso
# =======================================================================================================================================================
#
# 
# =======================================================================================================================================================
# Ejercicio 4. [Exponenciación binaria] Dado un número entero x ∈ Z y un natural n ∈ N_0. Queremos calcular la potencia x^n. Por convención, declaramos 
# que x^0 = 1 para todo x ∈ Z.
# Un método ingenuo para calcular la potencia es realizar una sucesión de n multiplicaciones, en tiempo O(n): [((x · x) · x) . . . · x] n veces.
# Se puede calcular x^n de manera más eficiente con el siguiente método, basado en la técnica de D&C:
# • Si n = 0, devolver 1.
# • Si n > 0 y es par, y = (x^(n/2))^2, y devolver y.
# • Si n > 0 y es impar, y = (x^(n-1/2))^2 * x, y devolver y.
# Se pide:
# • Implementar el método en Python y convencerse de que es correcto haciendo tests.
# • Analizar la complejidad temporal en peor caso.
# =======================================================================================================================================================
#
# En este caos, el algoritmo se compone de un blucle se ejecuta n veces. 
# Por lo tanto la complejidad temporal es O(n)
def exponenciacion_metodo_ingenuo(x, n):
    resultado = 0
    if n < 0:
        return "n debe ser un entero no negativo"
    
    if n >= 0:        
        resultado = 1
        for i in range(n):
            resultado *= x

    return resultado

# En este caso, el algoritmo se divide en 2, de manera recursiva, siendo el número de veces que se puede dividir hasta llegar a 1, log(n).
# Por lo tanto, la complejidad temporal es O(log n)
def exponenciacion_binaria(x, n):
    resultado = 0
    if n < 0:
        return "n debe ser un entero no negativo"
    
    if n == 0:
        return 1
    
      # si n es par
    if n % 2 == 0:
        medio_resultado = exponenciacion_binaria(x, n // 2)
        resultado = medio_resultado * medio_resultado
        return resultado
    # si n es impar
    else:  
        medio_resultado = exponenciacion_binaria(x, (n - 1) // 2)
        resultado = medio_resultado * medio_resultado * x
        return resultado

# =======================================================================================================================================================
# Área de ejecucución
# =======================================================================================================================================================

# ...
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 7
print("\n\nEjercicio 7: Exponenciación método ingenuo")
x = 2
n = 7
print(f"\nExponenciación método ingenuo de {x}^{n}:", exponenciacion_metodo_ingenuo(x, n))
print("\n\nEjercicio 7: Exponenciación binaria")
print(f"\nExponenciación binaria {x}^{n}:", exponenciacion_binaria(x, n))