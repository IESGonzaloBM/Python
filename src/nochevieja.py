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

from sys import exit

def inputs_management(hora: str) -> list[int, int]:
    if not isinstance(hora, str):
        raise Exception("[ERROR] Tipo de dato invaido")
    if hora.find(":") == -1:
        raise Exception("[ERROR] Formato invalido, debe de estar separado por :, XX:XX")

    hora_list = hora.split(":")
    for i in hora_list:
        if not i.isnumeric():
            raise Exception("[ERROR] Tipo de dato invalido, formato 24h, XX:XX")
    if 0 > int(hora_list[0]) > 23 or 0 > int(hora_list[1]) > 59:
        raise Exception("[ERROR] El primer dato debe ser entre 0 y 23")

if __name__ == "__main__":
    try:
        hora = input("Hora: ").strip()
        inputs_management(hora)
    except Exception as error:
        # print(error)
        exit(1)