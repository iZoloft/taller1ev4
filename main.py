from functions import *

while True:
    menu()
    opcion =  leer_opcion()
    if opcion == 1:
        agregar_vehiculo(lista_vehiculos)
    elif opcion == 2:
        modelo = input("Ingrese modelo a buscar: \n").strip()
        posicion = buscar_vehiculo(lista_vehiculos, modelo)
        if posicion != -1:
            print(f"Vehículo encontrado en la posición {posicion}")
            print(f"Modelo: {lista_vehiculos[posicion]["modelo"]}")
            print(f"Año: {lista_vehiculos[posicion]["anio"]}")
            print(f"Precio: ${lista_vehiculos[posicion]["precio"]}")
            if lista_vehiculos[posicion]["disponible"] == True:
                print("Estado: Disponible")
            else:
                print("Estado: No Disponible")
        else:
            print("Vehículo no encontrado")
    elif opcion == 3:
        modelo = input("Ingrese vehículo a eliminar: \n")
        posicion = buscar_vehiculo(lista_vehiculos, modelo)
        if posicion != -1:
            lista_vehiculos.pop(posicion)
        else:
            print(f"El vehículo {modelo} no se encuentra registrado")
    elif opcion == 4:
        actualizar_disponibilidad(lista_vehiculos)
    elif opcion == 5:
        mostrar_vehiculos(lista_vehiculos)
    elif opcion ==  6:
        print("Gracias por usar el sistema. Vuelva Pronto")
        break