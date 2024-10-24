waiting_list = []
a = 0

while True:
    print("1. Para agregar pacientes a la lista de espera. ")
    print("2. Para modificar la lista de  espera. ")
    print("3. Conocer el turno de una persona. ")
    print("4. Salir del programa. ")

    user_input = int(input("Ingresa que deseas hacer: "))

    if user_input == 1:
        while a != 1:
            name = str(input("Ingresar Nombre: "))
            fila = []
            if name == "":
                a=1
                print("Se ha finalizado la carga de datos de pacientes.")
                break

            urgency = int(input("Ingresar tipo de urgencia (1: CRITICO 2:NORMAL): "))
            fila.append(name)
            fila.append(urgency)

            if urgency == 1:
                waiting_list.insert(0, fila)
                # En caso de desear la lista de espera por orden de llegada
                
                # index = 0
                # for i in range(len(waiting_list)):
                #     if waiting_list[i][1] == 1:
                #         index = i + 1
                # waiting_list.insert(index, fila)
            elif urgency == 2:
                waiting_list.append(fila)

    elif user_input == 2:
        size_w_l = len(waiting_list)
        del_name = str(input("Ingresar Nombre de persona que desea ser eliminada: "))
        found = False

        for i in range (size_w_l):
            if waiting_list[i][0] == del_name:
                del(waiting_list[i])
                found = True
                print(f"{del_name} ha sido eliminado de la lista de espera")
                break
        if not found:
            print(f"{del_name} no se ha encontrado dentro de la lista")
            
    elif user_input == 3:
        orderly_turn = str(input("Ingresar Nombre de persona : "))
        found = False
        
        for i in range(len(waiting_list)):
            if waiting_list[i][0] == orderly_turn:
                print(f"El paciente {waiting_list[i][0]} esta en la posicion {i+1}")
                found = True
                break
            
        if not found:
            print(f"No se ha encontrado el paciente {orderly_turn} en la lista de espera.")

    elif user_input == 4:
        print("Saliendo del programa...")
        break

    else:
        print("Operacion Invalida. Reintentar usando numeros del 1 al 4.")

print(waiting_list)