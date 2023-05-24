def costo_llamadas(nacionales_linea_1, internacionales_linea_1, nacionales_linea_2, internacionales_linea_2):
    costo_nacional = 500
    costo_internacional = 1000
    costo_total_nacional = costo_nacional * \
        (nacionales_linea_1 + nacionales_linea_2)
    costo_total_internacional = costo_internacional * \
        (internacionales_linea_1 + internacionales_linea_2)
    costo_total = costo_total_nacional + costo_total_internacional
    return costo_total_nacional, costo_total_internacional, costo_total


while True:
    try:
        nacional_linea_1_min = int(
            input("Ingress los minutos totales en la linea 1 a nivel nacional: "))
        internacional_linea_1_min = int(
            input("Ingress los minutos totales en la linea 1 a nivel internacional: "))
        nacional_linea_2_min = int(
            input("Ingress los minutos totales en la linea 2 a nivel nacional: "))
        internacional_linea_2_min = int(
            input("Ingress los minutos totales en la linea 1 a nivel nacional: "))

        if nacional_linea_1_min < 0 or nacional_linea_2_min < 0 or internacional_linea_1_min < 0 or internacional_linea_1_min < 0:
            print("No recibe numeros negativos.")
        else:
            break
    except ValueError:
        print("Valores invalidos, ingreselos nuevamente.")
    # Ejemplo de uso
costo_nacional, costo_internacional, costo_total = costo_llamadas(
    nacional_linea_1_min, internacional_linea_1_min, nacional_linea_2_min, internacional_linea_2_min)
print("Costo de llamadas nacionales:", costo_nacional)
print("Costo de llamadas internacionales:", costo_internacional)
print("Costo total de todas las llamadas:", costo_total)
