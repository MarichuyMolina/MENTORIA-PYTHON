from datetime import datetime

while True:
    try:
        fecha = input("Ingresa una fecha en el formato YYY-MM-DD: ")
        datetime.strptime(fecha, '%Y-%m-%D')
        print("Verdadero")

    except ValueError:
        print("Falso")
    