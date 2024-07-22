estaciones = ["Calle 76", "Calle 72", "Flores", "Calle 63", "Calle 57", "Marly", "Calle 45", "Av. 39", "Profamilia", "Calle 26"]

grafo = {estacion: set() for estacion in estaciones}

rutas = [
    ["Calle 76", "Calle 72", "Flores"],
    ["Flores", "Calle 63", "Calle 57", "Marly"],
    ["Marly", "Calle 45", "Av. 39"],
    ["Av. 39", "Profamilia", "Calle 26"],
    ["Calle 76", "Calle 72", "Calle 63", "Calle 45", "Calle 26"]
]

for ruta in rutas:
    print(f"Procesando ruta: {ruta}")
    for i in range(len(ruta) - 1):
        estacion_origen = ruta[i]
        estacion_destino = ruta[i + 1]
        grafo[estacion_origen].add(estacion_destino)
        grafo[estacion_destino].add(estacion_origen)

for estacion, conexiones in grafo.items():
    print(f"{estacion}: {', '.join(conexiones)}")