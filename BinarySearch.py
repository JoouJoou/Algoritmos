# -*- coding: UTF-8 -*-
def buscabinaria(valor, lista):
    menor = 0
    count = 0
    maior = len(lista)-1
    while menor <= maior:
        meio = (maior+menor)//2
        if valor == lista[meio]:
            count+= 1
            return count
        elif valor < lista[meio]:
            count+= 1
            maior = meio - 1
        else:
            count+= 1
            menor = meio + 1
    return count