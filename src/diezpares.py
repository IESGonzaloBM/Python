from traceback import print_tb


def main():
    lista = [3, 7, 2, 9, 4, 1]

    max_val = 0
    for i in range(len(lista)):
        for val in lista:
            max_val = val if max_val <= val else max_val
        lista.remove(max_val)
        lista = [max_val] + lista
        max_val = 0
    print(lista)

def main2():
    num = int(input("Ingresa un numero: "))
    msg = ""

    for i in range(1, num + 1):
        print("* " * i)

    for h in range(num):
        for j in range(h + 1):
            msg += "* "
        print(msg)
        msg = ""

def main3():
    colores = ["rojo", "verde", "Azul"]
    tamano = ["S", "M", "L"]

    for i in range(len(colores)):
        for j in range(len(tamano)):
            print(f"Camiseta {colores[i]} talla {tamano[j]}")

def main4():
    num = int(input("Ingresa un numero: "))

    matriz = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    for i in range(len(matriz)):
        if num in matriz[i]:
            print(f"Elemento en Fila: {i + 1} Columna {matriz.index(matriz[i]) + 1} r")
            return
        for j in range(len(matriz[i])):
            if num == matriz[i][j]:
                print(f"Elemento en Fila: {i + 1} Columna {j + 1}")



if __name__ == "__main__":
    main4()