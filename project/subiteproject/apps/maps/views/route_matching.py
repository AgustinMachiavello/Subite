"""Algoritmos para comparar si dos rutas son compatibles para un viajero que quiere viajar de A a B"""

def unformat_coordinates(a):
    """Cambia el formato de una coordenada de String a List"""
    a = a.split(",")
    b = []
    for i in range(len(a)):
        if i != len(a)-1:
            b.append([float(a[i]), float(a[i+1])])
    return b

def match_routes(user_array, driver_array, max_difference=0.006, first_only=False):
    """Determina si dos rutas con compatibles
    
    first_only: Si es True, devuelve sólo la primera coordenada que coincida
    max_difference: diferencia máxima entre coordenadas (latitud y loguitud)
    Por defecto es 0.006, que representa aproximadamente 300 metros"""
    matching_points = []
    if len(user_array) >= len(driver_array):
        main_array, second_array = user_array, driver_array
    else:
        main_array, second_array = driver_array, user_array
    for i in range(len(second_array)):
        a = abs(abs(main_array[i][0]) - abs(second_array[i][0]))
        b = abs(abs(main_array[i][1]) - abs(second_array[i][1]))
        if (a + b) <= max_difference:
            matching_points.append([main_array[i][0], main_array[i][1]])
    if len(matching_points) > 0 and first_only:
        return [matching_points[0]]
    return matching_points