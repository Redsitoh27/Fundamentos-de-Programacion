def ordenar_fila(matriz, fila):
    # Usaremos Bubble Sort para ordenar la fila
    for i in range(len(matriz[fila])):
        for j in range(0, len(matriz[fila]) - i - 1):
            if matriz[fila][j] > matriz[fila][j + 1]:
                matriz[fila][j], matriz[fila][j + 1] = matriz[fila][j + 1], matriz[fila][j]

# Matriz de ejemplo 3x3
matriz = [
    [5, 8, 3],
    [6, 7, 1],
    [9, 2, 4]
]

# Mostrar matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Pedir al usuario que ingrese el índice de la fila a ordenar
fila_a_ordenar = int(input("Ingrese el número de la fila a ordenar (0 para la primera fila, 1 para la segunda, etc.): "))

# Verificar que el índice de la fila sea válido
if 0 <= fila_a_ordenar < len(matriz):
    # Ordenar la fila
    ordenar_fila(matriz, fila_a_ordenar)

    # Mostrar matriz con la fila ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in matriz:
        print(fila)
else:
    print("Índice de fila inválido. Por favor, ingrese un número entre 0 y", len(matriz) - 1)