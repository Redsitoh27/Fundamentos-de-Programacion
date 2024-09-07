# Definir la matriz de temperaturas 3D [ciudades][semanas][días]
# Supongamos que hay 3 ciudades, 2 semanas y 7 días por semana.
import random

# Inicializamos la matriz con valores aleatorios de temperatura (entre 10 y 35 grados).
ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
semanas = 2
dias = 7

# Crear una matriz de temperaturas para las 3 ciudades, 2 semanas y 7 días.
temperaturas = [[[random.randint(10, 35) for _ in range(dias)] for _ in range(semanas)] for _ in range(len(ciudades))]

# Calcular y mostrar el promedio de temperaturas por ciudad y semana.
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        suma_temperaturas = sum(temperaturas[i][semana])
        promedio = suma_temperaturas / dias
        print(f"  Semana {semana + 1}: {promedio:.2f} grados")