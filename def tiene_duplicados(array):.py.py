def tiene_duplicados(array):
    vistos = set()
    for numero in array:
        if numero in vistos:
            return True
        vistos.add(numero)
    return False
print(tiene_duplicados([1, 2, 3, 4]))
print(tiene_duplicados([1, 2, 3, 1]))