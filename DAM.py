lista = list(range(6))

cadena = "esto es una cadena"


print(lista[1:-1])
print(lista[0:-2])

print(cadena[4:-5])
print(cadena[5:len(cadena)])



def conjuga(verbo):
    sol = []
    raiz = verbo[0:-2]
    termi= verbo[-2:len(verbo)]
    listar = ['o', 'as', 'a', 'amos', 'áis', 'an']
    lister = ['o', 'es', 'e', 'emos', 'eis', 'en']
    listir= ['o','es','e','imos','is', 'en']
    if termi == "ar":
        for i in listar:
            sol.append(raiz+i)
        return sol
    elif termi == "er":
        for i in lister:
            sol.append(raiz+i)
        return sol
    elif termi=="ir":
        for i in listir:
            sol.append(raiz+i)
        return sol
print(conjuga("cambiar"))
