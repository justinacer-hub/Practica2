def analisis(posts):
    hashtags = []
    for post in posts:
        palabras = post.split()
        for palabra in palabras:
            if palabra.startswith("#"):
                hashtags.append(palabra)

    conteo = {}
    for tag in hashtags:
        if tag in conteo:
            conteo[tag] += 1
        else:
            conteo[tag] = 1

    return conteo
