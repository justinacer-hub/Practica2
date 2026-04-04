def limpiar_registros(students):
    # 1 y 2: eliminar registros inválidos
    limpios = []
    for s in students:
        if s["name"] and s["grade"] is not None:
            nombre = s["name"].strip().title()
            estado = s["status"].lower()
            limpios.append({"name": nombre, "grade": s["grade"], "status": estado})

    # 3 y 4: eliminar duplicados, quedando con la nota más alta
    final = {}
    for s in limpios:
        nombre = s["name"]
        if nombre not in final or s["grade"] > final[nombre]["grade"]:
            final[nombre] = s

    # 5: ordenar por nombre
    ordenados = sorted(final.values(), key=lambda x: x["name"])
    return ordenados
