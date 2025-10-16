########################################################################################################
#   Sumador de 2 numeros binarios
#
#   - Input: Dos numeros binarios
#   - Output: Suma de los numeros binarios
#   - PreCondition: None
#   - PostCondition: None
#
#   By: Gonzalo Blanco
########################################################################################################

from sys import argv, exit

def get_param() -> tuple[str, str]:
    """
    Obtiene los parametros dados por terminal

    :param: ``tuple[str,str]``
    :return: ``tuple[str,str]``
    """
    if len(argv) != 3:
        print("[ERROR]: Formato incorrecto, debe ser: py <file.py> [param1] [param2] [...]")
        exit(1)

    return argv[1], argv[2]

def start(bin_1:str, bin_2:str) -> tuple[list[int], list[int]]:
    """
    Toma el input del usuario, transforma los datos del input en ``list[int]`` y comprueba si los datos son correctos.

    :param bin_1: Primer numero binario
    :param bin_2: Segundo numero binario
    :return: ``list[param_data_1,param_data_2]``
    """

    # Comprobación de errores en los inputs
    try:
        # Usamos comprension de matrices y slicing para convertir los inputs a matrices y mutar los datos
        # Una comprension de matrices, itera sobre el objeto dado y automaticamente lo almacena en una matriz, ademas
        # con slicing mutamos los datos, en este caso, revirtiendolo
        array_bin_1 = [int(x) for x in str(bin_1)][::-1]
        array_bin_2 = [int(x) for x in str(bin_2)][::-1]

    except Exception as error:
        print(f"[ERROR]: Todos los valores deben ser solamente [0, 1]a")
        exit(1)
    if len(array_bin_1) != 8 or len(array_bin_2) != 8:
        print("[ERROR]: Uno de los valores introduccidos no es 8")
        exit(1)
    for i in range(len(array_bin_1)):
        if array_bin_1[i] not in (0, 1) or array_bin_2[i] not in (0, 1):
            print("[ERROR]: Todos los valores deben ser solamente [0, 1]b")
            exit(1)

    return array_bin_1, array_bin_2

def bin_sum(array_bin_1:list[int], array_bin_2:list[int]) -> list[int]:
    """
    Iterando toda la longitud de uno de los dos numero binarios, aplicamos un algoritmo de suma que usa la
    funcion ``bin_sum()`` como tabla logica de conjuncion.

    :param array_bin_1: ArrayList del primer numero binario
    :param array_bin_2: ArrayList del segundo numero binario
    :return: Numero binario sumado en base a ``array_bin_1`` y ``array_bin_2`` en formato ``list[int]``
    """

    def conjunction(x:int, y:int) -> tuple[int, bool] | None:
        """
        Tabla logica conjuncion, x ^ y

        :param x: Primer valor de entrada numero binario
        :param y: Segundo valor de entrada numero binario
        :return: ``tuple[int,bool]`` | ``None``
        """

        if x == 0 and y == 0:
            return 0, False
        elif x == 1 and y == 1:
            return 0, True
        elif (x == 1 and y == 0) or (x == 0 and y == 1):
            return 1, False
        return None

    carriage = False
    data_array = []
    for i in range(len(array_bin_1)):
        value_1, value_2 = array_bin_1[i], array_bin_2[i]

        if carriage:
            # Aplicamos destructuring para almacenar los valores
            data_acarreo, acarreo_1 = conjunction(value_1, 1)
            bit_sum, acarreo_2 = conjunction(value_2, data_acarreo)
            carriage = acarreo_1 or acarreo_2
        else:
            bit_sum, carriage = conjunction(value_1, value_2)

        data_array.append(bit_sum)

    # Sumamos un digito extra por si tenemos aun acarreo
    if carriage:
        data_array.append(1)

    # Posicion original usando slicing
    return data_array[::-1]

if __name__ == "__main__":
    data_1, data_2 = get_param()
    array_data_1, array_data_2 = start(data_1, data_2)
    data_sum = bin_sum(array_data_1, array_data_2)

    binario = ""
    for i in range(0, len(data_sum)):
        binario = f"{binario}" + f"{data_sum[i]}"

    print(binario)