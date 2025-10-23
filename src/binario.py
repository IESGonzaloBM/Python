########################################################################################################
#   Sumador de 2 numeros binarios
#
#   - Input: Dos numeros binarios
#   - Output: Suma de los numeros binarios
#
#   By: Gonzalo Blanco
########################################################################################################

from sys import argv, exit


def bin2decimal(bin: str | int) -> int:
    """
    Convierte un numero binario a decimal

    Args:
        bin (str | int): Numero binario
    Returns:
        int: Numero decimal
    Raises:
        Exception: Lanza un error si la entrada no es un numero binario valido
    """

    bin_str = str(bin).strip()


    n = 0
    for ch in bin_str:
        n = n * 2 + int(ch)
    return n


def get_param() -> tuple[str, list[int], list[int]]:
    """
    Obtiene los parametros dados por terminal, gestiona y controla los posibles errores

    Returns:
        tuple[str, list[int], list[int]]: Tupla con el operador y los dos numeros binarios
    Raises:
        Exception: Lanza un tipo de error generico, en formato: "[ERROR] <error interpretado>"
    """

    if len(argv) != 4:
        raise Exception("[ERROR]: Formato incorrecto, debe ser: py <file.py> <+|-> [param1] [param2] [...], param1 >= param2")
    elif argv[1] not in ['+', '-']:
        raise Exception("[ERROR]: Formato incorrecto, indicador + o - ,debe ser: py <file.py> <+|-> [param1] [param2] [...], param1 >= param2")
    elif any(bit not in "01" for arg in (argv[2], argv[3]) for bit in arg):
        raise Exception("Entrada inválida")
    elif bin2decimal(argv[2]) < bin2decimal(argv[3]):
        raise Exception("[ERROR]: Formato incorrecto, param1 es menor que param2 ,debe ser: py <file.py> <+|-> [param1] [param2] [...]")

    try:
        # Usamos comprension de matrices y slicing para convertir los inputs a matrices y mutar los datos.
        # Una comprension de matrices, itera sobre el objeto dado y automaticamente lo almacena en una matriz, ademas
        # con slicing mutamos los datos, en este caso, revirtiendolo
        array_bin_1 = [int(x) for x in str(argv[2])][::-1]
        array_bin_2 = [int(x) for x in str(argv[3])][::-1]
    except Exception:
        raise Exception(f"[ERROR]: Todos los valores deben ser solamente [0, 1]")

    if len(array_bin_1) != 8 or len(array_bin_2) != 8:
        raise Exception("[ERROR]: Uno de los valores introduccidos no es 8")
    for i in range(len(array_bin_1)):
        if array_bin_1[i] not in (0, 1) or array_bin_2[i] not in (0, 1):
            raise Exception("[ERROR]: Todos los valores deben ser solamente [0, 1]")

    return argv[1], array_bin_1, array_bin_2


def bin_sum(array_bin_1: list[int], array_bin_2: list[int]) -> list[int]:
    """
    Iterando toda la longitud de uno de los dos numeros binarios, aplicamos un algoritmo para saber en que situacion de la tabla logica o de verdad nos encontramos y dar un resultado.

    Args:
        array_bin_1 (list[int]): ArrayList del primer numero binario
        array_bin_2 (list[int]): ArrayList del segundo numero binario
    Returns:
        list[int]: Numero binario sumado
    """

    def algorithm(bit_1: int, bit_2: int, acarreo: int) -> tuple[int, int]:
        """
        Suma binaria por bit con acarreo. Se podria usar una tabla logica o de verdad, pero es mas sencillo asi ademas de mas efeciente, claro y optimo.
        Evaluamos si diff esta contenido en (-inf, 1], si es asi devolvemos el valor y acarreo 0, si no, ajustamos el bit restandole 2 y generamos un nuevo acarreo.

        Args:
            bit_1 (int): Primer valor de entrada numero binario
            bit_2 (int): Segundo valor de entrada numero binario
            acarreo (int): Acarreo previo (0 o 1)
        Returns:
            tuple[int, int]: (bit_resultante, acarreo_resultante)
        """

        diff = bit_1 + bit_2 + acarreo
        if diff <= 1:
            return diff, 0
        else:
            return diff - 2, 1

    acarreo = 0
    data_array = []
    for i in range(max(len(array_bin_1), len(array_bin_2))):
        bit, acarreo = algorithm(array_bin_1[i], array_bin_2[i], acarreo)
        data_array.append(bit)

    if acarreo == 1:
        data_array.append(1)

    return data_array[::-1]


def bin_rest(array_bin_1: list[int], array_bin_2: list[int]) -> list[int]:
    """
    Iterando toda la longitud de uno de los dos numero binarios, aplicamos un algoritmo para saber en que situacion de la tabla logica o de verdad nos encontramos y dar un resultado.

    Args:
        array_bin_1 (list[int]): ArrayList del primer numero binario
        array_bin_2 (list[int]): ArrayList del segundo numero binario
    Returns:
        list[int]: Numero binario sumado
    """

    def algorithm(bit_1: int, bit_2: int, acarreo: int) -> tuple[int, int]:
        """
        Resta binaria por bit con acarreo. Se podria usar una tabla logica o de verdad, pero es mas sencillo asi ademas de mas efeciente, claro y optimo.
        Evaluamos si diff esta contenido en [0, +inf), si es asi devolvemos el valor y acarreo 0, si no, ajustamos el bit sumandole 2 y generamos un nuevo acarreo.

        Args:
            bit_1 (int): Primer valor de entrada numero binario
            bit_2 (int): Segundo valor de entrada numero binario
            acarreo (int): Acarreo previo (0 o 1)
        Returns:
            tuple[int, int]: Devuelve el bit y el acarreo resultante
        """

        diff = bit_1 - bit_2 - acarreo
        if diff >= 0:
            return diff, 0
        else:
            return diff + 2, 1  # Le sumamos 2 para ajustar el bit y generamos un nuevo acarreo

    acarreo = 0
    data_array = []
    for i in range(max(len(array_bin_1), len(array_bin_2))):
        bit, acarreo = algorithm(array_bin_1[i], array_bin_2[i], acarreo)
        data_array.append(bit)

    return data_array[::-1]


def print_bin(operator: str, bin_1: list[int], bin_2: list[int]):
    if operator == "+":
        bin_sum_array = bin_sum(bin_1, bin_2)

        # Usamos comprension de matrices para convertir el dato iterado en string y concatenarlo
        bin_sum_str = "".join(str(bit) for bit in bin_sum_array)

        print(f"Suma: {bin_sum_str}, Longitud: {len(str(bin_sum_str))} bits")
    elif operator == "-":
        bin_rest_array = bin_rest(bin_1, bin_2)
        bin_rest_str = "".join(str(bit) for bit in bin_rest_array)
        print(f"Resta: {bin_rest_str}, Longitud: {len(str(bin_rest_str))} bits")
    else:
        bin_sum_array = bin_sum(bin_1, bin_2)
        bin_rest_array = bin_rest(bin_1, bin_2)

        bin_sum_str = "".join(str(bit) for bit in bin_sum_array)
        bin_rest_str = "".join(str(bit) for bit in bin_rest_array)

        max_len = max(len(str(bin_sum_str)), len(str(bin_rest_str)))

        print(f"Suma: {bin_sum_str}\nResta: {bin_rest_str}, Longitud: {max_len} bits")


if __name__ == "__main__":
    try:
        operator, bin_1, bin_2 = get_param()
    except Exception as error:
        print(error)
        exit(1)
    print_bin(operator, bin_1, bin_2)
