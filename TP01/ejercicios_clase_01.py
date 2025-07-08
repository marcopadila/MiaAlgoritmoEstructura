# EJERCICIOS CLASE 01
#
# =======================================================================================================================================================
# Ejercicio 1. Dar algoritmos para resolver los siguientes problemas y determinar su complejidad temporal y espacial en peor caso
# =======================================================================================================================================================
#
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# a) Hallar el máximo de un arreglo de n enteros.
#
def hallar_maximo_arreglo(arreglo):
    if not arreglo:
        return None
    
    maximo = arreglo[0]
    for item in arreglo:
        if item > maximo:
            maximo = item
    return maximo
#
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# b) Hallar los k números más grandes de un arreglo de n enteros.
#
def hallar_k_maximos_arreglo(arreglo, k):
    if not arreglo or k <= 0:
        return []
    
    n = len(arreglo)
    for i in range(n):
        for j in range(i + 1, n):
            if arreglo[i] < arreglo[j]:
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
    
    return arreglo[:k]
#
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# c) Dados dos arreglos de enteros A y B, determinar cuál es más largo.
#
def arreglo_mas_largo(arreglo_1, arreglo_2):
    if not arreglo_1 and not arreglo_2:
        return None
    if not arreglo_1:
        return arreglo_2
    if not arreglo_2:
        return arreglo_1
    
    if len(arreglo_1) >= len(arreglo_2):
        return arreglo_1
    else:
        return arreglo_2
#
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# d) Dados dos arreglos de enteros A y B, determinar cuántos elementos de A aparecen también en B.
#
def elementos_comunes(arreglo_1, arreglo_2):
    if not arreglo_1 or not arreglo_2:
        return []
    
    elementos_comunes = []
    for item in arreglo_1:
        if item in arreglo_2 and item not in elementos_comunes:
            elementos_comunes.append(item)
    
    return len(elementos_comunes)
#
# =======================================================================================================================================================
# Ejercicio 4. Diseñar un tipo de datos VectorConUndo con la siguiente interfaz, respetando las complejidades temporales en peor caso indicadas:
# • inicializar(n) — crea un vector de tamaño n, cuyos elementos son todos 0.
#   >>>  Precondición: se asume que n ≥ 0. Complejidad: O(n).
# • leer(i) — devuelve el valor en la posición i.
#   >>>  Precondición: se asume que 0 ≤ i < n. Complejidad: O(1).
# • escribir(i, x) — sobreescribe el elemento en la posición i con el valor x.
#   >>>  Precondición: se asume que 0 ≤ i < n. Complejidad: O(1).
# • ctrlZ() — deshace la última operación de escritura. Si no hubo escrituras, esta operación no tiene efecto.
#   >>>  Complejidad: O(1).
# =======================================================================================================================================================
#
class VectorConUndo:
    def __init__(self, n):
        self.vector = self.inicializar(n)
        self.n = n
        # creo este vector para ir guardando los cambios al escribir
        self.memoria = []

    # Complejidad temporal: O(n)
    def inicializar(self, n):
        vector = []
        for i in range(n):
            vector.append(0)

        return vector   

    # Complejidad temporal: O(1)
    def leer(self, i):
        return self.vector[i]

    # Complejidad temporal: O(1)
    def escribir(self, i, x):
        # guardo el valor anterior antes de sobrescribir
        self.memoria.append((i, self.vector[i]))
        # piso el valor anterior con el valor nuevo (x)
        self.vector[i] = x

    # Complejidad temporal: O(1)
    def ctrlZ(self):
        if self.memoria:
            # recupero de la memoria, el último valor guardado
            (i, valor_anterior) = self.memoria.pop()
            # devuevlo el útimo valor guardado a la posición i del vector
            self.vector[i] = valor_anterior

# =======================================================================================================================================================
# Área de ejecucución
# =======================================================================================================================================================

# 1.a) Hallar el máximo de un arreglo de n enteros.
arreglo = [199, 2, 43, 1, 18, 55, 23, 32, 99]
print("\n1.a) El máximo del arreglo es:", hallar_maximo_arreglo(arreglo))
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.b) Hallar los k números más grandes de un arreglo de n enteros.
arreglo = [199, 2, 43, 1, 18, 55, 23, 32, 99, 300]
k = 3
print(f"\n1.b) Los {k} máximos del arreglo son:", hallar_k_maximos_arreglo(arreglo, k))
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.c) Dados dos arreglos de enteros A y B, determinar cuál es más largo.
arreglo_1 = [199, 2, 43, 1, 18, 55, 23, 32, 99, 300]
arreglo_2 = [33, 2, 1, 19]
print("\n1.c) El arreglo más largo es:", arreglo_mas_largo(arreglo_1, arreglo_2))
# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.d) Dados dos arreglos de enteros A y B, determinar cuántos elementos de A aparecen también en B.
arreglo_1 = [199, 2, 43, 1, 18, 55, 23, 32, 99, 300]
arreglo_2 = [33, 2, 1, 19, 199]
print("\n1.d) Los elementos comunes son:", elementos_comunes(arreglo_1, arreglo_2))
# -------------------------------------------------------------------------------------------------------------------------------------------------------


# ...


# -------------------------------------------------------------------------------------------------------------------------------------------------------
# 4
print("\n\nEjercicio 4: VectorConUndo")
vectorConUndo = VectorConUndo(5)
print("\n>>> Inicializado:", vectorConUndo.vector)
vectorConUndo.escribir(2, 5)
print("\n>>> Después de escribir 5 en posición 2:", vectorConUndo.vector)
vectorConUndo.escribir(3, 15)
print("\n>>> Después de escribir 15 en posición 3:", vectorConUndo.vector)
vectorConUndo.escribir(3, 8)
print("\n>>> Después de escribir 8 en posición 3:", vectorConUndo.vector)
print("\n>>> Memoria:", vectorConUndo.memoria)
vectorConUndo.ctrlZ()
print("\n>>> Después de ctrlZ:", vectorConUndo.vector)
print("\n>>> Memoria:", vectorConUndo.memoria)
# -------------------------------------------------------------------------------------------------------------------------------------------------------