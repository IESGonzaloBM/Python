#=========================================================================================
#   La entrada consiste en una serie de horas, cada una en una línea. Cada hora está formada por las horas y los minutos
#   separados por : y utilizando siempre dos dígitos. Se utiliza una representación en formato 24 horas (es decir, desde 00:00 a 23:59).
#   La entrada termina cuando la hora es la medianoche (00:00), que no debe procesarse.
#
#   PreCondicion: Hora en formato 24h, XX:XX
#   PostCondicion: Numero de minutos que faltan para media noche
#
#   By: Gonzalo Blanco Mosteiro
#=========================================================================================

def inputs_management(hora: str) -> list[int]:
    """
    Gestiona y controla los posibles errores de entrada, como: tipo de dato, formato (XX:XX), rango de datos admitidos etc..

    Args:
        hora (str): input del usuario
    Returns:
        list[int]: Lista con los valores del usuario comprobados
    Raises:
        Exception: Lanza un tipo de error generico, en formato: "[ERROR] <error interpretado/mensaje>"
    """
    if not isinstance(hora, str):
        raise Exception("[ERROR] Tipo de dato invaido")
    if hora.find(":") == -1:
        raise Exception("[ERROR] Formato invalido, debe de estar separado por :, XX:XX")

    hora_list = hora.split(":")
    for i in hora_list:
        if not i.isnumeric():
            raise Exception("[ERROR] Tipo de dato invalido, formato 24h, XX:XX")
    if (0 > int(hora_list[0]) or 23 < int(hora_list[0])) or (0 > int(hora_list[1]) or 59 < int(hora_list[1])):
        raise Exception("[ERROR] El primer dato debe ser entre 0 y 23, el segundo entre 0 y 59")

    return [int(hora_list[0]), int(hora_list[1])]

def calculate_minutes(hora: list[int]) -> int:
    """
    Calcula los minutos que faltan hasta fin del dia (23:59)

    Args:
        hora (list[int]): Input del usuario ya parseado a lista con 2 valores
    Returns:
        int: Calcula los minutos restantes para el fin del dia (23:59)
    """
    minutes = 0

    while hora[0] < 24:
        for i in range(hora[1], 60):
            minutes += 1

        hora[0] += 1
        hora[1] = 0

    return minutes

if __name__ == "__main__":
    try:
        hora = input("Hora: ").strip()
        hora_list = inputs_management(hora)
        minutes = calculate_minutes(hora_list)
        print(f"Minutos: {minutes}")
    except Exception as error:
        print(error)