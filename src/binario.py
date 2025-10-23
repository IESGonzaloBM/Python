# ===================================================================================================
#   Sumador de 2 numeros binarios
#
#   - Input: Dos numeros binarios
#   - Output: Suma y/o resta de los numeros binarios
#
#   By: Gonzalo Blanco
# ===================================================================================================
from sys import argv, exit


def bin2decimal(bin: str | int) -> int:
    """
    Convierte un numero binario a decimal.

    Args:
        bin (str | int): Numero binario.
    Returns:
        int: Numero decimal.
    """

    bin_str = str(bin).strip()

    n = 0
    for bin in bin_str:
        n = n * 2 + int(bin)
    return n


def get_param() -> tuple[str, list[int], list[int]]:
    """
    Obtiene los parametros dados por terminal, gestiona y controla los posibles errores.

    Analiza si se han pasado 3 argumentos (bin1, operador, bin2) o 2 argumentos (bin1, bin2).

    Returns:
        tuple[str, list[int], list[int]]: Tupla con el operador ('+' o '-' o 'all') y los dos numeros binarios.
    Raises:
        Exception: Lanza un tipo de error generico, en formato: "[ERROR] <error interpretado>".
    """
    # El nombre del script es el primer argumento (argv[0]), por lo que
    # len(argv) == 4 es para 'py file.py bin1 op bin2'
    # len(argv) == 3 es para 'py file.py bin1 bin2'
    if len(argv) not in [3, 4]:
        raise Exception("[ERROR]: Formato incorrecto. Debe ser: py <file.py> [bin1] <+|-> [bin2] O: py <file.py> [bin1] [bin2].")

    # Verifica si se ha pasado un operador
    if len(argv) == 4:
        operator = argv[2]
        bin_str_1 = argv[1]
        bin_str_2 = argv[3]

        if operator not in ['+', '-']:
            raise Exception("[ERROR]: Formato incorrecto, operador + o - ,debe ser: py <file.py> [bin1] <+|-> [bin2].")
    else:
        operator = 'all'
        bin_str_1 = argv[1]
        bin_str_2 = argv[2]

    # any() devuelve True si minimo 1 valor se evalua como tal. Usamos bucles anidados en formato de compresión
    # de matrices (sin matrices) para extraer la informacion de argvs e iterar sobre los bin (str). Es una forma elegante y optima de hacerlo
    if any(bit not in "01" for arg in (bin_str_1, bin_str_2) for bit in arg):
        raise Exception("Entrada inválida. Los valores deben ser solamente binarios [0, 1].")
    if bin2decimal(bin_str_1) < bin2decimal(bin_str_2):
        raise Exception("[ERROR]: Formato incorrecto, param1 es menor que param2 ,debe ser: py <file.py> [param1] <+|-> [param2], param1 >= param2.")
    if len(bin_str_1) > 8 or len(bin_str_2) > 8:
        raise Exception("[ERROR]: Uno de los valores introducidos excede la longitud máxima de 8 bits.")

    try:
        # Usamos comprension de matrices y slicing para convertir los inputs a matrices y mutar los datos.
        # Una comprension de matrices, itera sobre el objeto dado y automaticamente lo almacena en una matriz.
        array_bin_1 = [int(x) for x in bin_str_1]
        array_bin_2 = [int(x) for x in bin_str_2]
    except Exception:
        raise Exception(f"[ERROR]: Todos los valores deben ser solamente [0, 1]")

    # De ser menor a base-8, rellenamos con 0, sino tomamos el maximo, es decir, 8. Realmente podriamos usar el metodo <str>.zfill(n) para rellenar con 0 a la izquierda n digitos.
    # (aunque la validación de longitud ya lo previene pero es para poder usar ternarios)
    array_bin_1 = ([0] * (8 - len(array_bin_1)) + array_bin_1 if len(array_bin_1) < 8 else array_bin_1[:8])
    array_bin_2 = ([0] * (8 - len(array_bin_2)) + array_bin_2 if len(array_bin_2) < 8 else array_bin_2[:8])

    return operator, array_bin_1, array_bin_2


def bin_sum(bin_1: list[int], bin_2: list[int]) -> list[int]:
    """
    Realiza la suma binaria de dos números representados como listas de enteros.

    Args:
        bin_1 (list[int]): ArrayList del primer numero binario.
        bin_2 (list[int]): ArrayList del segundo numero binario.
    Returns:
        list[int]: Numero binario sumado.
    """

    def algorithm(bit_1: int, bit_2: int, acarreo: int) -> tuple[int, int]:
        """
        Suma binaria por bit con acarreo.

        Args:
            bit_1 (int): Primer valor de entrada numero binario.
            bit_2 (int): Segundo valor de entrada numero binario.
            acarreo (int): Acarreo previo (0 o 1).
        Returns:
            tuple[int, int]: (bit_resultante, acarreo_resultante).
        """

        diff = bit_1 + bit_2 + acarreo
        if diff <= 1:
            return diff, 0
        else:
            return diff - 2, 1

    # Invertirtimos la matriz usando sclincing para empezar por el bit menos significativo
    bin_1_inverted = bin_1[::-1]
    bin_2_inverted = bin_2[::-1]

    acarreo = 0
    data_array = []
    for i in range(max(len(bin_1), len(bin_2))):
        bit, acarreo = algorithm(bin_1_inverted[i], bin_2_inverted[i], acarreo)
        data_array.append(bit)

    if acarreo == 1:
        data_array.append(1)

    return data_array[::-1]


def bin_rest(bin_1: list[int], bin_2: list[int]) -> list[int]:
    """
    Realiza la resta binaria de dos números representados como listas de enteros (bin_1 - bin_2).

    Args:
        bin_1 (list[int]): ArrayList del primer numero binario.
        bin_2 (list[int]): ArrayList del segundo numero binario.
    Returns:
        list[int]: Numero binario restado.
    """

    def algorithm(bit_1: int, bit_2: int, acarreo: int) -> tuple[int, int]:
        """
        Resta binaria por bit con acarreo (préstamo).

        Args:
            bit_1 (int): Primer valor de entrada numero binario (Minuendo).
            bit_2 (int): Segundo valor de entrada numero binario (Sustraendo).
            acarreo (int): Acarreo (préstamo) previo (0 o 1).
        Returns:
            tuple[int, int]: Devuelve el bit y el acarreo (préstamo) resultante.
        """

        diff = bit_1 - bit_2 - acarreo
        if diff >= 0:
            return diff, 0
        else:
            return diff + 2, 1

    bin_1_inverted = bin_1[::-1]
    bin_2_inverted = bin_2[::-1]

    acarreo = 0
    data_array = []
    for i in range(max(len(bin_1), len(bin_2))):
        bit, acarreo = algorithm(bin_1_inverted[i], bin_2_inverted[i], acarreo)
        data_array.append(bit)

    return data_array[::-1]


def print_bin(operator: str, bin_1: list[int], bin_2: list[int]):
    """
    Ejecuta y muestra el resultado de la suma, la resta, o ambas, dependiendo del operador.

    Args:
        operator (str): Operador a ejecutar ('+', '-', 'all').
        bin_1 (list[int]): Primer numero binario.
        bin_2 (list[int]): Segundo numero binario.
    """

    if operator == "+":
        bin_sum_array = bin_sum(bin_1, bin_2)
        # Usamos list comprehension para convertir el dato iterado en string y concatenarlo
        bin_sum_str = "".join(str(bit) for bit in bin_sum_array)
        print(f"Suma: {bin_sum_str}, Longitud: {len(str(bin_sum_str))} bits")
    elif operator == "-":
        bin_rest_array = bin_rest(bin_1, bin_2)
        bin_rest_str = "".join(str(bit) for bit in bin_rest_array)
        print(f"Resta: {bin_rest_str}, Longitud: {len(str(bin_rest_str))} bits")
    elif operator == "all":
        bin_sum_array = bin_sum(bin_1, bin_2)
        bin_rest_array = bin_rest(bin_1, bin_2)

        bin_sum_str = "".join(str(bit) for bit in bin_sum_array)
        bin_rest_str = "".join(str(bit) for bit in bin_rest_array)

        print(f"Suma: {bin_sum_str}, Longitud: {len(bin_sum_str)} bits")
        print(f"Resta: {bin_rest_str}, Longitud: {len(bin_rest_str)} bits")


if __name__ == "__main__":
    try:
        operator, bin_1, bin_2 = get_param()
    except Exception as error:
        print(error)
        exit(1)

    print_bin(operator, bin_1, bin_2)