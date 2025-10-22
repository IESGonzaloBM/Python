
def main():
    lista = [3, 7, 2, 9, 4, 1]
    lista_ordenada = []

    max_val = 0
    for i in range(0, len(lista)):
        for val in lista:
            max_val = val if max_val <= val else max_val
        lista_ordenada.append(max_val)
        lista.remove(max_val)
        max_val = 0
    print(lista_ordenada)

if __name__ == "__main__":
    main()