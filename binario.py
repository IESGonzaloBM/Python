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

bin_1 = 10101101 # input("Ingrese 1º binario: ")
bin_2 = 11011100 # input("Ingrese 2º binario: ")

# Usamos comprension de listas y slicing para convertir los inputs a arrays y mutar los datos
array_bin_1 = [int(x) for x in str(bin_1)][::-1]
array_bin_2 = [int(x) for x in str(bin_2)][::-1]

# Comprobación de errores en los inputs
if not bin_1.is_integer() or not bin_2.is_integer(): # Cambiar a bit
    print("Uno o ambos no son tipo primitivo de dato int")
if not bin_1 > 0 or not bin_2 > 0:
    print("El tipo de dato introduccido es negativo")
if len(array_bin_1) != 8 or len(array_bin_2) != 8:
    print("El valor introduccido no es 8")
for i in range(len(array_bin_1) - 1, 0):
    if array_bin_1[i] != (0, 1) or array_bin_2[i] != (0, 1):
        print("Los valores introduccidos deben ser 0 o 1")

# Tabla logica x ^ y
def bin_sum(x:int, y:int) -> tuple[int, bool] | None:
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
data_array = data_array[::-1]
print(data_array) # Output: 110001001