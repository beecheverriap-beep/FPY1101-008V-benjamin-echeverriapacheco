print("\n Bienvenidos al Sistema Medico")

while True:
    try:
        totalMedicos = int(input("\nIngrese el total de medicos: "))
        if totalMedicos < 0:
            print("Registro Medico invalido. Ingresa un numero entero positivo para continuar.")
        else:
            break
    except ValueError:
        print("Error: por favor, ingrese un número entero válido.")


medResidentes = 0
medEspecialistas = 0

for i in range(totalMedicos):
    

    while True:
        nombreMedico = input(f"\nIngrese el nombre del medico {i + 1} (6 caracteres o mas, no debe incluir espacios): ")
        if (len(nombreMedico) < 6) or (" " in nombreMedico):
            print("Registro medico invalido, el nombre del medico debe tener al menos 6 caracteres y no debe incluir espacios. Por favor, intente nuevamente.")
        else:
            break


    while True:
        try:
            anosExperiencia = int(input(f"\nIngrese los años de experiencia del medico {i + 1}: "))
            if anosExperiencia < 0:
                print("Error clinico: ingresa un numero entero positivo para la experiencia.")
            else:
                if anosExperiencia <= 5:
                    medResidentes += 1
                else:
                    medEspecialistas += 1
                break
        except ValueError:
            print("Error: por favor, ingrese un numero mayor o igual a 0.")

print(f"\nEl hospital cuenta con {medResidentes} Especialistas Junior y {medEspecialistas} especialistas Senior.")