import random

def sorteo_amigo_invisible(nombres):
    # 1. Normalizar
    nombres = [n.strip() for n in nombres]

    # 2. Validaciones
    if len(nombres) < 3:
        return "Debe haber al menos 3 participantes."
    if len(set([n.lower() for n in nombres])) != len(nombres):
        return "No debe haber nombres duplicados."

    # 3. Crear copia mezclada y repetir hasta que nadie se tenga a sí mismo
    asignados = nombres[:]
    while True:
        random.shuffle(asignados)
        if all(n != a for n, a in zip(nombres, asignados)):
            break

    # 4. Guardar pares
    resultado = []
    for n, a in zip(nombres, asignados):
        resultado.append((n, a))

    return resultado