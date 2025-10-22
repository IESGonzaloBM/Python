

def error_management(param: str):
    pass

def saca_vocales(name: str) -> str:
    try:
        error_management(name)
    except Exception:
        print("")

    vocal = ""
    for i in name.lower():
        if i in "aeiouáéíóú":
            vocal += i

    return vocal
