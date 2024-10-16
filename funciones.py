existencias = []

def cargar(existencias):
    guardar_existencias = []
    provincia = input("Ingrese la provincia: ")
    tipo_juguete = input("Ingrese el tipo de juguete: ")
    cantidad = int(input("Ingrese la cantidad: "))
    guardar_existencias = [provincia,tipo_juguete,cantidad]
    existencias = [guardar_existencias]
    return existencias

def calcular_total_juguetes(existencias):
    total = 0
    for juguete in existencias:
        total += juguete[2]
    return total

def menor_a_500 ():
    juguetes_faltantes = []
    for juguetes in existencias:
        if juguetes[2] < 500:
            juguetes_faltantes += [juguetes[1]]
    return juguetes_faltantes

def maxima_cantidad_por_juguete_sin_metodos(existencias):
    max_cantidades = []

    for juguete in existencias:
        provincia, tipo_juguete, cantidad = juguete[0], juguete[1], juguete[2]
        encontrado = False

        for i in range(len(max_cantidades)):
            if max_cantidades[i][0] == tipo_juguete:
                encontrado = True
                if cantidad > max_cantidades[i][2]:
                    max_cantidades[i] = [tipo_juguete, provincia, cantidad]
                break
        
        if not encontrado:
            max_cantidades += [[tipo_juguete, provincia, cantidad]]
    
    return max_cantidades

precios = [["Trenes", 100], ["Auto", 200], ["Muñeca", 150], ["Peluches", 300], ["Spinners", 50], ["Cartas", 25]]
def calcular_deposito_mayor_recaudacion(existencias, precios):
    recaudaciones = []
    provincias = []

    for juguete in existencias:
        provincia = juguete[0]
        tipo_juguete = juguete[1]
        cantidad = juguete[2]

        if tipo_juguete == "Trenes":
            precio = precios[0][1]
        elif tipo_juguete == "Auto":
            precio = precios[1][1]
        elif tipo_juguete == "Muñeca":
            precio = precios[2][1]
        elif tipo_juguete == "Peluches":
            precio = precios[3][1]
        elif tipo_juguete == "Spinners":
            precio = precios[4][1]
        elif tipo_juguete == "Cartas":
            precio = precios[5][1]
        else:
            precio = 0
        
        recaudacion = cantidad * precio

        index_provincia = -1
        for i in range(len(provincia)):
            if provincias[i] == provincia:
                index_provincia = 1
                break
        
        if index_provincia == -1:
            provincias += [[provincia]]
            recaudaciones += [[recaudacion]]
        else:
            recaudaciones[index_provincia][0] += recaudacion

    mayor_recaudacion = 0
    provincia_mayor_recaudacion = ""

    for i in range(len(recaudaciones)):
        if recaudaciones[i][0] > mayor_recaudacion:
            mayor_recaudacion = recaudaciones[i][0]
            provincia_mayor_recaudacion = provincia[i][0]
        
    print("Provincia con mayor recaudacion: ", provincia_mayor_recaudacion, "con $", mayor_recaudacion)

def mostrar_provincias_con_mas_de_50000(existencias):
    provincias = []
    total_por_provincia = []

    for i in existencias:
        provincia = i[0]
        cantidad = i[2]

        index_provincia = -1
        for i in range(len(provincias)):
            if provincias[1] == provincia:
                index_provincia = i
                break
        if index_provincia == -1:
            provincias += [[provincia]]
            total_por_provincia += [[cantidad]]
        else:
            total_por_provincia[index_provincia][0] += cantidad

    print("Provincias con mas de 50.000 unidades almacenadas: ")
    for i in range(len(total_por_provincia)):
        if total_por_provincia[i][0] > 50000:
            print(f"{provincias[i][0]}, con, {total_por_provincia[i][0]}, unidades")

def calcular_porcentaje_juguetes_por_tipo(existencias):
    total_juguetes = 0
    tipos_juguetes = []
    cantidades_tipos = []
    tipo_count = 0

    for juguete in existencias:
        tipo_juguete = juguete[1]
        cantidad = juguete[2]

        total_juguetes += cantidad

        existe = False
        for i in range(tipo_count):
            if tipos_juguetes[i] == tipo_juguete:
                cantidades_tipos[i] += cantidad
                existe = True
                break
        if not existe:
            tipos_juguetes[tipo_count] = tipo_juguete
            cantidades_tipos[tipo_count] = cantidad
            tipo_count += 1
    print("Porcentaje de juguetes de cada tipo: ")
    for i in range(tipo_count):
        porcentaje = (cantidades_tipos[i] / total_juguetes) * 100 if total_juguetes > 0 else 0
        porcentaje_redondeado = float(porcentaje * 100) / 100
        print(str(tipos_juguetes[i]) + ": " + str(porcentaje_redondeado) + "%")

def menu():
    """Muestra las opciones del menu"""   
    print("""
          Sistema de almacenamiento y distribucion de juguetes
          
          [1] Cargar juguetes
          [2] Calcular total
          [3] Maxima cantidad
          [4] Calcular
          [5] Mostrar provincias
          [6] Calcular porcentaje
          [7] Salir
          """)
    seleccion = int(input("."))
    return seleccion


def seleccion_menu() -> None:
    """Funcion para la seleccion de la funcion que desea usar"""
    seguir = "s"
    while seguir == "s":
        num = menu()
        match num:
            case 1: cargar(existencias)
            case 2: calcular_total_juguetes(existencias)
            case 3: maxima_cantidad_por_juguete_sin_metodos(existencias)
            case 4: calcular_deposito_mayor_recaudacion(existencias, precios)
            case 5: mostrar_provincias_con_mas_de_50000(existencias)
            case 6: calcular_porcentaje_juguetes_por_tipo(existencias)
            case 7: seguir = "n"
            case _: print("Ingresar una opcion valida")

seleccion_menu()