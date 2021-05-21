# -*- coding: UTF-8 -*-
def bubblesort(lista):
    for num in range(len(lista)-1, 0, -1):
        for elemento in range(num):
            if lista[elemento] > lista[elemento+1]:
                temp = lista[elemento]
                lista[elemento] = lista[elemento+1]
                lista[elemento+1] = temp
    return lista