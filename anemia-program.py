#Nombre del estudiante: Annye Julyeth Araque Acero
#Grupo: 213022_566
#Programa: Ingenieria Electrónica
#Código Fuente: autoría propia

#Consultorio medico: 
#Determinar si una persona tiene anemia según su edad, sexo y nivel de hemoglobina.

nombre_paciente = str(input("Ingrese el nombre del paciente: "));
edad = int(input("Ingrese la edad del paciente: "));
sexo = str(input("Ingrese el sexo del paciente: "));
hemoglobina = float(input("Ingrese el nivel de hemoglobina del paciente: "));

def determinar_anemia(edad, sexo, hemoglobina):
    # 1. Definir los rangos de hemoglobina según la tabla
    rangos = {
        (0, 1, "meses"): (13.0, 26.0),
        (1, 6, "meses"): (10.0, 18.0),
        (6, 12, "meses"): (11.0, 15.0),
        (1, 5, "años"): (11.5, 15.0),
        (5, 10, "años"): (12.6, 15.5),
        (10, 15, "años"): (13.0, 15.5),
        ("mujeres",): (12.0, 16.0),
        ("hombres",): (14.0, 18.0),
    }

    # 2. Validar las entradas
    if not isinstance(edad, (int, float)) or edad < 0:
        return "Error: La edad debe ser un número positivo."
    if sexo not in ("masculino", "femenino"):
        return "Error: El sexo debe ser 'masculino' o 'femenino'."
    if not isinstance(hemoglobina, (int, float)) or hemoglobina < 0:
        return "Error: El nivel de hemoglobina debe ser un número positivo."

    # 3. Determinar el rango de hemoglobina correspondiente
    if edad <= 1:
        if edad == 0:
            rango = rangos[(0, 1, "meses")]
        elif edad <= 6 / 12:
            rango = rangos[(1, 6, "meses")]
        else:
            rango = rangos[(6, 12, "meses")]
    elif edad <= 5:
        rango = rangos[(1, 5, "años")]
    elif edad <= 10:
        rango = rangos[(5, 10, "años")]
    elif edad <= 15:
        rango = rangos[(10, 15, "años")]
    else:
        rango = rangos[("mujeres",)] if sexo == "femenino" else rangos[("hombres",)]

    # 4. Comparar el nivel de hemoglobina con el rango
    if hemoglobina < rango[0]:
        return "Positivo"  # Anemia
    else:
        return "Negativo"  # No anemia


#5. Mostrar resultado positivo o negativo
resultado = determinar_anemia(edad, sexo, hemoglobina)
print(f"Resultado anemia: {resultado}")
