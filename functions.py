lista_vehiculos = []

def menu():
    print("======== Menú ========")
    print("1. Agregar Vehículo")
    print("2. Buscar Vehículo")
    print("3. Eliminar Vehículo")
    print("4. Actualizar Disponibilidad")
    print("5. Mostrar Vehículos")
    print("6. Salir")

def leer_opcion():
    try:
        opcion = int(input("Ingrese opción: \n"))
        if opcion > 0 and opcion <= 6:
            return opcion
        else:
            print("Opción debe estar entre 1 y 6")
    except:
        print("Valor debe ser numérico")

def _validar_str(string):
    if len(string) > 0:
        return True
    return False

def _validar_anio(numero):
    if numero > 1900 and numero <= 2026:
        return True
    return False

def _validar_precio(numero):
    if numero > 0:
        return True
    return False

def _validar_lista(lista_vehiculos):
    if len(lista_vehiculos) > 0:
        return True
    return False

def agregar_vehiculo(lista_vehiculos):
    while True:
        modelo = input("Ingrese modelo del vehículo: \n").strip()
        if _validar_str(modelo):
            break
        else:
            print("Modelo no debe venir vacio")
    while True:
        anio = int(input("Ingrese año del vehículo: \n"))
        if _validar_anio(anio):
            break
        else:
            print("Año debe ser mayor que 1900")
    while True:
        precio = float(input("Ingrese precio del vehículo: \n$ "))
        if _validar_precio(precio):
            break
        else:
            print("Precio debe ser mayor a 0")
    auto = {
        "modelo" : modelo,
        "anio" : anio,
        "precio" : precio,
        "disponible" : False
    }
    lista_vehiculos.append(auto)
    print("Vehículo Agregado")

def buscar_vehiculo(lista_vehiculos, modelo):
    for v in range(len(lista_vehiculos)):
        if lista_vehiculos[v]["modelo"] == modelo:
            return v
    return -1

def actualizar_disponibilidad(lista_vehiculos):
    if _validar_lista(lista_vehiculos) == False:
        print("No hay vehículos en la lista")
        return
    for v in lista_vehiculos:
        if v["anio"] >= 2020:
            v["disponible"] = True
        else:
            v["disponible"] = False
    print("Disponibilidad Actualizada")

def mostrar_vehiculos(lista_vehiculos):
    if _validar_lista(lista_vehiculos) == False:
        print("No hay vehículos en la lista")
        return
    actualizar_disponibilidad(lista_vehiculos)
    print("=== Lista de Vehículos ===")
    for v in lista_vehiculos:
        print(f"Modelo: {v["modelo"]}")
        print(f"Año: {v["anio"]}")
        print(f"Precio: ${v["precio"]}")
        if v["disponible"] == True:
            print("Estado: Disponible")
        else:
            print("Estado: No Disponible")
        print("*************************************")