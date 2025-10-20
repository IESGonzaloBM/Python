from sys import exit

def input_errors(entrada: str):
    if not entrada.isdigit():
        raise Exception("[ERROR] Tipo de dato invalido, valor numerico negativo")
    elif isinstance(entrada, str) and entrada != "fin":
        raise Exception("[ERROR] Tipo de dato invalido")

def inputs() -> list[int] | None:
    msg = ""
    lista_numeros = []

    while msg != "fin":
        numero_palabra = input("Ingresa un numero o la palabra 'fin': ")

        try:
            input_errors(numero_palabra)
        except Exception as error:
            print(error)
            exit(1)

        if numero_palabra.isdigit():
            lista_numeros.append(int(numero_palabra))
            print(numero_palabra)
        else:
            msg = numero_palabra

    return lista_numeros

def calcular(data: list[int]) -> list[int]:
    total = 0
    cantidad = 0
    for i in data:
        cantidad += 1
        total += i
    media = total / cantidad

    return [total, cantidad, media]

if __name__ == "__main__":
    data = inputs()
    total, cantidad, media = calcular(data)
    print(f"Total: {total} \nCantidad: {cantidad} \nMedia: {media}")
