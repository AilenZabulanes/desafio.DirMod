diccionario = {
    "a": "2",
    "b": "22",
    "c": "222",
    "d": "3",
    "e": "33",
    "f": "333",
    "g": "4",
    "h": "44",
    "i": "444",
    "j": "5",
    "k": "55",
    "l": "555",
    "m": "6",
    "n": "66",
    "o": "666",
    "p": "7",
    "q": "77",
    "r": "777",
    "s": "7777",
    "t": "8",
    "u": "88",
    "v": "888",
    "w": "9",
    "x": "99",
    "y": "999",
    "z": "9999",
    " ": "0"
}


def sec(texto, diccionario):
    devuelve = ""
    frase = texto.lower()
    for i in range(len(frase)):
        letra = frase[i]
        letra_anterior = frase[i-1]
        dicc = diccionario[letra][0]
        dicc_anterior = diccionario[letra_anterior][0]
        if(dicc == dicc_anterior):
            devuelve += " " + diccionario[letra]
        else:
            devuelve += diccionario[letra]

    return devuelve

texto = input("Ingrese el texto que quiera convertir: ")
print(sec(texto, diccionario))