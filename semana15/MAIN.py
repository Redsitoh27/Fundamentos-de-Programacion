# Crear un Diccionario para almacenar información personal
informacion_personal = {
    "nombre": "Ana López",  # Nombre de la persona
    "edad": 28,             # Edad de la persona
    "ciudad": "Valencia",   # Ciudad donde reside
    "profesion": "Diseñadora Gráfica"  # Profesión de la persona
}

# Acceder y Modificar Valores
# Modificar el valor asociado con la clave "ciudad"
informacion_personal["ciudad"] = "Sevilla"  # Cambiar la ciudad a Sevilla

# Cambiar la profesión a una nueva
informacion_personal["profesion"] = "Desarrolladora Web"  # Actualizar la profesión

# Verificar Existencia de Claves
# Comprobar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    # Si no existe, agregar la clave "telefono" con un número ficticio
    informacion_personal["telefono"] = "678-123-456"  # Número de teléfono ficticio

# Eliminar una Clave
# Eliminar la clave "edad" del diccionario
if "edad" in informacion_personal:
    del informacion_personal["edad"]  # Borrar la clave "edad" ya que no es necesaria

# Imprimir el Diccionario Final
print(informacion_personal)  # Mostrar el diccionario resultante