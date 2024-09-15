def calcular_promedio_ciudad(temperaturas):
    """
    Calcula el promedio de temperatura para cada ciudad durante todo el período.

    :param temperaturas: Lista 3D de temperaturas [ciudades][semanas][días].
    :return: Diccionario con los nombres de las ciudades y sus promedios.
    """
    # Diccionario para almacenar los promedios de cada ciudad
    promedio_ciudades = {}

    # Iterar sobre cada ciudad en la matriz de temperaturas
    for i, ciudad in enumerate(temperaturas):
        total_temperaturas = 0  # Almacena la suma total de temperaturas para la ciudad actual
        total_dias = 0  # Cuenta el número total de días para la ciudad actual

        # Iterar sobre las semanas de la ciudad actual
        for semana in ciudad:
            # Sumar todas las temperaturas de los días en la semana actual
            total_temperaturas += sum(semana)
            # Aumentar el total de días con el número de días de la semana
            total_dias += len(semana)

        # Calcular el promedio de temperaturas para la ciudad actual
        promedio = total_temperaturas / total_dias
        # Almacenar el promedio en el diccionario, asignando el nombre "Ciudad1", "Ciudad2", etc.
        promedio_ciudades[f"Ciudad{i + 1}"] = promedio

    # Devolver el diccionario que contiene el promedio de cada ciudad
    return promedio_ciudades


# Crear una matriz de temperaturas para 3 ciudades, 4 semanas y 7 días.
import random

# Definimos 3 ciudades, 4 semanas y 7 días por semana
ciudades = 3
semanas = 4
dias = 7

# Generar la matriz 3D de temperaturas con valores aleatorios (entre 10 y 35 grados)
# para las 3 ciudades, 4 semanas y 7 días por semana
temperaturas = [[[random.randint(10, 35) for _ in range(dias)] for _ in range(semanas)] for _ in range(ciudades)]

# Llamar a la función para calcular los promedios
promedios = calcular_promedio_ciudad(temperaturas)

# Mostrar los resultados: promedio de temperaturas para cada ciudad
for ciudad, promedio in promedios.items():
    print(f"El promedio de temperaturas en {ciudad} durante todo el período es: {promedio:.2f} grados")
