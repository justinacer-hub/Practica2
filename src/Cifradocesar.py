def cifrar_cesar(texto, desplazamiento):
    resultado = ""
    for char in texto:
        if char.isalpha():  # si es letra
            base = ord('A') if char.isupper() else ord('a')
            # mover dentro del rango 0-25
            nuevo = (ord(char) - base + desplazamiento) % 26 + base
            resultado += chr(nuevo)
        else:
            resultado += char
    return resultado