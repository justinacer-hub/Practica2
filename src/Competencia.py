def inicializar_totales(participantes: list):
    return {
        participante: {"total": 0, "ganadas": 0, "mejor_ronda": 0, "rondas": []}
        for participante in participantes
    }


def calcular_puntaje_ronda(scores: dict):
    return {
        participante: sum(jueces.values())
        for participante, jueces in scores.items()
    }


def obtener_ganador_ronda(puntajes_ronda: dict):
    ganador = max(puntajes_ronda, key=lambda p: puntajes_ronda[p])
    return ganador, puntajes_ronda[ganador]


def actualizar_totales(totales: dict, puntajes_ronda: dict, ganador: str):
    for participante, puntaje in puntajes_ronda.items():
        totales[participante]["total"] += puntaje
        totales[participante]["rondas"].append(puntaje)
        totales[participante]["ganadas"] += (1 if participante == ganador else 0)
        if puntaje > totales[participante]["mejor_ronda"]:
            totales[participante]["mejor_ronda"] = puntaje
    return totales


def mostrar_tabla(totales: dict, num_rondas: int):
    print(f"{'Cocinero':<12} {'Puntaje':>8} {'Rondas ganadas':>15} {'Mejor ronda':>12} {'Promedio':>10}")
    print("-" * 62)
    ranking = sorted(totales.items(), key=lambda x: x[1]["total"], reverse=True)
    for participante, datos in ranking:
        promedio = datos["total"] / len(datos["rondas"])
        print(f"{participante:<12} {datos['total']:>8} {datos['ganadas']:>15} {datos['mejor_ronda']:>12} {promedio:>10.1f}")
    print("-" * 62)


def simular_competencia(rounds: list):
    participantes = list(rounds[0]["scores"].keys())
    totales = inicializar_totales(participantes)

    for i, ronda in enumerate(rounds):
        puntajes_ronda = calcular_puntaje_ronda(ronda["scores"])
        ganador, puntaje_ganador = obtener_ganador_ronda(puntajes_ronda)
        totales = actualizar_totales(totales, puntajes_ronda, ganador)

        print(f"\nRonda {i+1} - {ronda['theme']}:")
        print(f"  Ganador: {ganador} ({puntaje_ganador} pts)")
        mostrar_tabla(totales, i + 1)

    print("\nTabla de posiciones final:")
    mostrar_tabla(totales, len(rounds))