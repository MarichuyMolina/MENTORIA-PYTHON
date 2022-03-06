def ValidarFecha(dia, mes, año):
      
    if dia => 1 or dia <= 31
    elif mes => 1 or mes <= 12
        print("Fecha incorrecta")
    elif año => 0 or año <= 10000

    else: 
        return "Verdadero"

    dia = int(input('Dia: '))
    mes = int(input('mes: '))
    año = int(input('año: '))
    ValidarFecha(dia, mes, año)
    
