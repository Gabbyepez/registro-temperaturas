import pandas as pd  # Librería para trabajar con tablas y CSV

# ============================
# 1️⃣ FUNCIÓN PARA CALCULAR PROMEDIOS
# ============================
def calcular_promedios(temperaturas):
    """
    Calcula el promedio de temperatura por ciudad y semana.
    :param temperaturas: Lista 3D [ciudad][semana][día]
    :return: Lista con promedios por ciudad y semana
    """
    promedios = []  # Lista donde guardaremos los promedios de todas las ciudades

    # Recorremos cada ciudad (temperaturas es una lista de ciudades)
    for ciudad_index, ciudad in enumerate(temperaturas):
        promedios_ciudad = []  # Guardará los promedios de esta ciudad

        # Recorremos cada semana de la ciudad
        for semana in ciudad:
            promedio_semana = sum(semana) / len(semana)  # Calculamos el promedio de esa semana
            promedios_ciudad.append(promedio_semana)  # Lo agregamos a la lista de esta ciudad

        promedios.append(promedios_ciudad)  # Guardamos los promedios de esta ciudad en la lista general

    return promedios


# ============================
# 2️⃣ DATOS DE TEMPERATURA (3 ciudades × 4 semanas × 7 días)
# ============================
temperaturas = [
    [[20, 21, 19, 22, 23, 21, 20],  # Ciudad 1 - Semana 1
     [22, 23, 21, 22, 24, 25, 23],  # Ciudad 1 - Semana 2
     [19, 20, 21, 19, 20, 21, 22],  # Ciudad 1 - Semana 3
     [23, 22, 24, 25, 23, 24, 22]], # Ciudad 1 - Semana 4

    [[25, 24, 26, 27, 25, 24, 26],  # Ciudad 2 - Semana 1
     [26, 27, 25, 26, 28, 29, 27],  # Ciudad 2 - Semana 2
     [24, 23, 25, 26, 24, 23, 25],  # Ciudad 2 - Semana 3
     [27, 26, 28, 29, 27, 26, 28]], # Ciudad 2 - Semana 4

    [[30, 31, 29, 30, 32, 31, 30],  # Ciudad 3 - Semana 1
     [32, 33, 31, 32, 34, 33, 32],  # Ciudad 3 - Semana 2
     [29, 28, 30, 31, 29, 28, 30],  # Ciudad 3 - Semana 3
     [33, 32, 34, 35, 33, 32, 34]]  # Ciudad 3 - Semana 4
]

# ============================
# 3️⃣ USO DE LA FUNCIÓN
# ============================
promedios = calcular_promedios(temperaturas)

# ============================
# 4️⃣ GUARDAR RESULTADO EN CSV
# ============================
df = pd.DataFrame(
    promedios,
    columns=['Semana 1', 'Semana 2', 'Semana 3', 'Semana 4'],
    index=['Ciudad 1', 'Ciudad 2', 'Ciudad 3']
)

df.to_csv('promedios.csv')  # Crea el archivo CSV en tu carpeta del proyecto
print("✅ Archivo 'promedios.csv' generado correctamente")
print(df)  # Muestra en pantalla la tabla con los resultados


