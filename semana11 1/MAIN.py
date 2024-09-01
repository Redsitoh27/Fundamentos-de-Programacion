def buscar_en_matriz(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return (i, j)
    return None

# Matriz de ejemplo 3x3
matriz = [
    [5, 8, 3],
    [6, 7, 1],
    [9, 2, 4]
]

# Pedir al usuario que ingrese el valor a buscar
valor_buscado = int(input("Ingrese el valor a buscar en la matriz: "))

# Búsqueda
resultado = buscar_en_matriz(matriz, valor_buscado)

if resultado:
    print(f"Valor {valor_buscado} encontrado en la posición {resultado}.")
else:
    print(f"Valor {valor_buscado} no encontrado en la matriz.")