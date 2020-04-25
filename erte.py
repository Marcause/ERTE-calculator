def get_base(): #define la base de cotización
    print("Por favor, introduce tu base salarial de los últimos 180 días (lo que ganas normalmente)")
    base = int(input())
    while base <= 0:
        ("La base debe ser superior a 0")
        base = int(input())
    return base

def get_percent():  #define el % de ERTE 
    print("Indica el % de reducción de jornada, si no estás trabajando tu reducción es del 100%")
    percent = int(input())
    while percent not in range(0,101):
        print("El valor debe estar entre 0 y 100")
        percent = int(input())
    return percent

def get_pagas(porcentaje): #define en cuántas pagas tiene el trabajador
    if porcentaje == 1:
        return 12
    print("Indica en cuantas pagas se divide tu nómina, normalmente 12 ó 14")
    pagas = int(input())
    while pagas not in range(12,16):
        print("El valor debe estar entre 12 y 15")
        pagas = int(input())
    return pagas

def get_base_max(base): #define si su base supera el límite o no y devuelve la base correcta
    print("¿Cuántos hijos tienes?")
    hijos = int(input())
    while hijos < 0:
        print("No puedes tener menos de 0")
        hijos = int(input())
    if hijos == 0:
        base_max = 1098.09
    elif hijos ==1:
        base_max = 1254.96
    else:
        base_max = 1411.83
    return base_max if (base/12 > base_max) else base/12

def paga_final(): #te da los dineros que te corresponden
    base = get_base()
    percent = get_percent()/100
    base_max = get_base_max(base)
    pagas = get_pagas(percent)

    dinero_estado = base_max*percent
    dinero_empresa = base/pagas*(1-percent)
    total = dinero_estado+dinero_empresa
    print("En este caso te corresponden {}€".format(round(total,2)))
    print("{} € corresponden al estado".format(round(dinero_estado,2)))
    print("{} € los paga tu empresa".format(round(dinero_empresa,2)))

if __name__ == "__main__":
    # execute only if run as a script
    paga_final()