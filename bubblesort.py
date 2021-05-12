# -*- coding: UTF-8 -*-
def bubblesort(lista):
    for num in range(len(lista)-1, 0, -1):
        for elemento in range(num):
            if lista[elemento] > lista[elemento+1]:
                temp = lista[elemento]
                lista[elemento] = lista[elemento+1]
                lista[elemento+1] = temp
    return lista

lista = [50, 3, 10, 22, 31, 12, 54, 48, 1, 21, 2]
print(bubblesort(lista))