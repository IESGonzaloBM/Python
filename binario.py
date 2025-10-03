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

def input() -> tuple[list[int], list[int]] | None: # DEV: Cambiarlo a string cuando el output sean inputs
    """
    Toma el input del usuario, transforma los datos del input en ``list[int]`` y comprueba si los datos son correctos.

    :param a: Primer numero binario
    :param b: Segundo numero binario
    :return: ArrayList de ``a`` y ``b``
    """

    bin_1 = 10101101 # input("Ingrese 1º binario: ")
    bin_2 = 11011100 # input("Ingrese 2º binario: ")

    # Usamos comprension de listas y slicing para convertir los inputs a arrays y mutar los datos
    array_bin_1 = [int(x) for x in str(bin_1)][::-1]
    array_bin_2 = [int(x) for x in str(bin_2)][::-1]

    # Comprobación de errores en los inputs
    if not bin_1.is_integer() or not bin_2.is_integer():  # Cambiar a bit
        print("Uno o ambos no son tipo primitivo de dato int")
        return None
    if not bin_1 > 0 or not bin_2 > 0:
        print("El tipo de dato introduccido es negativo")
        return None
    if len(array_bin_1) != 8 or len(array_bin_2) != 8:
        print("El valor introduccido no es 8")
        return None
    for i in range(len(array_bin_1) - 1, 0):
        if array_bin_1[i] != (0, 1) or array_bin_2[i] != (0, 1):
            print("Los valores introduccidos deben ser 0 o 1")
            return None

    return array_bin_1, array_bin_2

def output(array_bin_1:list[int], array_bin_2:list[int]) -> list[int]:
    """
    Iterando toda la longitud de uno de los dos numero binarios, aplicamos un algoritmo de suma que usa la
    funcion ``bin_sum()`` como tabla logica de conjuncion.

    :param array_bin_1: ArrayList del primer numero binario
    :param array_bin_2: ArrayList del segundo numero binario
    :return: Numero binario sumado en base a ``array_bin_1`` y ``array_bin_2`` en formato ``list[int]``
    """

    def bin_sum(x:int, y:int) -> tuple[int, bool] | None:
        """
        Tabla logica x ^ y

        :param x: Primer valor de entrada numero binario
        :param y: Segundo valor de entrada numero binario
        :return: Tupla de datos en base a la opcion logica detectada ``tuple[int,bool]``, en caso de no devolver nada
        devolveria ``None``
        """

        if x == 0 and y == 0:
            return 0, False
        elif x == 1 and y == 1:
            return 0, True
        elif (x == 1 and y == 0) or (x == 0 and y == 1):
            return 1, False
        return None

    acarreo = False
    data_array = []
    for i in range(0, len(array_bin_1) - 1):
        data_1 = array_bin_1[i]
        data_2 = array_bin_2[i]

        if acarreo:
            # Aplicamos destructuring para almacenar los valores
            data_acarreo, acarreo_1 = bin_sum(data_1, 1)
            bit_sum, acarreo_2 = bin_sum(data_2, data_acarreo)
            accareo = acarreo_1 or acarreo_2
        else:
            bit_sum, acarreo = bin_sum(data_1, data_2)

        data_array.append(bit_sum)

    # Sumamos un digito extra por si tenemos aun acarreo
    if acarreo:
        data_array.append(1)

    # Posicion original usando slicing
    return data_array[::-1]

if __name__ == "__main__":
    print(output(input()))