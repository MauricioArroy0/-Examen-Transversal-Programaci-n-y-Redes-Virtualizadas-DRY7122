integrantes = [
    ("mauricio", "Arroyo", "Cantillana")
    
]

lista_nombres_apellidos = []

for nombre, apellido, apellidos in integrantes:
    nombre_completo = nombre + " " + apellido + " " + apellidos
    lista_nombres_apellidos.append(nombre_completo)

print(lista_nombres_apellidos)