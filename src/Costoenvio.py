def costo_envio(peso, zona):
    zona = zona.lower()

    if zona not in ["local", "regional", "nacional"]:
        return "Zona no válida. Las zonas disponibles son: local, regional, nacional."

    if peso <= 1:
        if zona == "local":
            costo = 500
        elif zona == "regional":
            costo = 1000
        else:
            costo = 2000
    elif peso <= 5:
        if zona == "local":
            costo = 1000
        elif zona == "regional":
            costo = 2500
        else:
            costo = 4500
    else:
        if zona == "local":
            costo = 2000
        elif zona == "regional":
            costo = 5000
        else:
            costo = 8000

    return f"Ingrese el peso del paquete (kg): {peso}\nIngrese la zona de destino (local/regional/nacional): {zona}\nCosto de envío: ${costo}"