# Ejercicio 2: Obtener elemento en posición específica

def get_element(lista, indice):
    """
    Retorna el elemento en la posición indicada.
    Si el índice está fuera de rango, retorna None.

    Args:
        lista: Una lista de cualquier tipo de elementos
        indice: Índice del elemento a obtener

    Returns:
        El elemento en la posición indicada o None si está fuera de rango
    """
    if indice >= 0:
        if len(lista) >= (indice + 1):
            return lista[indice]
        else:
            return None
    elif indice < 0:
        if abs(indice) <= len(lista):
            return lista[indice]
        else:
            return None
