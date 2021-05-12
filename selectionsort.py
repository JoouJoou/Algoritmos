# -*- coding: UTF-8 -*-
def selectionsort(lista):
    for num in range(0, len(lista)-1):
        posicaodomin = num
        for elemento in range(num+1, len(lista)):
            if lista[elemento] < lista[posicaodomin]:
                temp = lista[elemento]
                lista[elemento] = lista[posicaodomin]
                lista[posicaodomin] = temp
    return lista

lista = [10, 12, 1, 4, 3, 2]
print(selectionsort(lista))