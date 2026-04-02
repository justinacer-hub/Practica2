def Filtro (review):
    palabras_spoiler = input("Ingrese las palabras spoiler:")
    lista = [p.strip() for p in palabras_spoiler.split(",")]

    for palabras in lista:
         review = review.replace(palabras, "*" * len(palabras))
         # cubrir variantes en minúsculas y mayúsculas
         review = review.replace(palabras.lower(), "*" * len(palabras))
         review = review.replace(palabras.upper(), "*" * len(palabras))
         review = review.replace(palabras.capitalize(), "*" * len(palabras))
    
    return review