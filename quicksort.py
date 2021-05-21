def quicksort(lista, primeiro, ultimo):
    if primeiro < ultimo:
        pivo = lista[primeiro]
        leftmark = primeiro+1
        rightmark = ultimo
        while True:
            while leftmark <= rightmark and lista[leftmark] <= pivo:
                leftmark+= 1
            while rightmark >= leftmark and lista[rightmark] >= pivo:
                rightmark-= 1
            if rightmark < leftmark:
                break
            else:
                temp = lista[rightmark]
                lista[rightmark] = lista[leftmark]
                lista[leftmark] = temp
        temp = lista[rightmark]
        lista[rightmark] = pivo
        lista[primeiro] = temp
        quicksort(lista, primeiro, rightmark-1)
        quicksort(lista, rightmark+1, ultimo)
def quicksorthelper(lista):
    quicksort(lista, 0, len(lista)-1)