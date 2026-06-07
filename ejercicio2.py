def menuPrincipal():
    print("\nMenu Principal")
    print("1. Libros disponibles")
    print("2. Libros prestados")
    print("3. Devolver Préstamo")
    print("4. Historial de Préstamos")
    print("5. Salir")

maxLibros = 120       
stockLibros = 120
historialPrestamos = 0

while True:
    menuPrincipal()
    try:
        opcion = int(input("\nSeleccione una opción (1-5): "))
        if opcion < 1 or opcion > 5:
            print("Opción inválida. Por favor, seleccione una opción entre 1 y 5.")
            continue 

    except ValueError:
        print("Error: por favor, ingrese un número entero válido para seleccionar una opción.")
        continue


    if opcion == 1:
        print("\n=== Libros disponibles ===")
        print(f"Actualmente hay {stockLibros} libros disponibles en la biblioteca.")


    elif opcion == 2:
        print("\n=== Registrar Préstamo ===")
        try:
            numeroPrestamos = int(input("Ingrese el número de libros a prestar: "))
            
            if numeroPrestamos < 1:
                print("Error: el número de libros a prestar debe ser al menos 1.")
            elif numeroPrestamos > stockLibros:
                print(f"Error: no hay suficientes libros disponibles. Actualmente hay {stockLibros} libros.")
            else:
                stockLibros -= numeroPrestamos
                historialPrestamos += numeroPrestamos
                print(f"¡Préstamo exitoso! Has prestado {numeroPrestamos} libros.")
                print(f"Quedan {stockLibros} libros disponibles en la biblioteca.")
        except ValueError:
            print("Error: por favor, ingrese un número entero válido.")


    elif opcion == 3:
        print("\n=== Devolver Préstamo ===")
        try:
            numeroDevoluciones = int(input("Ingrese el número de libros a devolver: "))
            if numeroDevoluciones < 1:
                print("Error: el número de libros a devolver debe ser al menos 1.")
            elif stockLibros + numeroDevoluciones > maxLibros:
                print(f"Error: no se pueden devolver más libros del límite máximo. El stock no puede superar los {maxLibros} libros.")
            else:
                stockLibros += numeroDevoluciones
                print(f"¡Devolución exitosa! Has devuelto {numeroDevoluciones} libros.")
                print(f"Ahora hay {stockLibros} libros disponibles en la biblioteca.")
        except ValueError:
            print("Error: por favor, ingrese un número entero válido.")


    elif opcion == 4:
        print("\n=== Historial de Préstamos ===")
        print(f"Total de préstamos realizados: {historialPrestamos} libros prestados históricamente.")


    elif opcion == 5:
        print("\nGracias por usar el sistema de biblioteca. ¡Hasta luego!\n")
        break