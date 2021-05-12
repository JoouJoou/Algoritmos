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

search_input = [int(i) for i in input("").split()]
range_list = search_input.pop(0)
main_list = [search_input.pop(0) for e in range(range_list)]
for test in search_input:
    print(buscabinaria(test, main_list), end=' ')