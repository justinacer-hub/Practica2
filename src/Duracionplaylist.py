def duracion_playlist(playlist):
    total_segundos = 0
    duraciones = []

    for cancion in playlist:
        partes = cancion["duration"].split(":")  # separo m y s
        minutos = int(partes[0])
        segundos = int(partes[1])
        segundos_totales = minutos * 60 + segundos

        # guardo título y duración en segundos
        duraciones.append((cancion["title"], segundos_totales, cancion["duration"]))
        total_segundos += segundos_totales

    # convierto a m y s
    total_minutos = total_segundos // 60
    resto_segundos = total_segundos % 60

    # max y min de canciones
    mas_larga = max(duraciones, key=lambda x: x[1])
    mas_corta = min(duraciones, key=lambda x: x[1])

    print(f"Duración total: {total_minutos}m {resto_segundos}s")
    print(f"Canción más larga: \"{mas_larga[0]}\" ({mas_larga[2]})")
    print(f"Canción más corta: \"{mas_corta[0]}\" ({mas_corta[2]})")
