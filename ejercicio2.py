def asignar_recursos(tipo str, destino: str, general: str) -> dict:
    # Asignar prioridad a la misión
    if general in ["Palpatine", "Darth Vader"]:
        prioridad = "alta"
    else:
        prioridad = "baja"

    if prioridad == "alta": #prioridad
        # Asignación manual de recursos
        pass
    elif prioridad == "baja":
        if tipo == "exploración": #tipo de misión
            stormtroopers = 15
            vehiculos = ["speeder bike"]
        elif tipo == "contención":
            stormtroopers = 30
            vehiculos = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST"]
        elif tipo == "ataque":
            stormtroopers = 50
            vehiculos = ["AT-AT", "AT-RT", "AT-TE", "AT-DP", "AT-ST", "AT-M6", "AT-MP", "AT-DT"]
        else:
            raise ValueError("Tipo de misión no reconocido")
    else:
        raise ValueError("Prioridad de misión no reconocida")
    
    # Devolver diccionario con los recursos asignados
    return {
        "stormtroopers": stormtroopers,
        "vehículos": vehiculos
    }

def total_recursos():
    t_stormtroopers = 0
    t_vehiculos = 0
    for mision in misiones:
        t_stormtroopers += mision['recursos']['stormtroopers']
        t_vehiculos += len(mision['recursos']['vehículos'])
    return {
        "stormtroopers": total_stormtroopers,
        "vehículos": total_vehiculos
    }
