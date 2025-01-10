import random
import time


def gerar_array(tamanho_array):
    array = [random.randint(0, 5 * tamanho_array) for _ in range(tamanho_array)]
    return array


#Bubble Sort
def bubble_sort(ar):
    n_elementos = len(ar)
    trocou = True

    while(trocou):
        trocou = False
        for i in range(n_elementos - 1):
            if ar[i] > ar[i+1]:
                ar[i], ar[i+1] = ar[i+1], ar[i]
                trocou = True
        n_elementos -= 1

    return ar[:10]        


#Selection Sort
def selection_sort(ar):
    n_elementos = len(ar)
    for i in range(n_elementos - 1):
        iMenor = i
        for j in range(i+1, n_elementos):
            if ar[j] < ar[iMenor]:
                iMenor = j
        ar[i], ar[iMenor] = ar[iMenor], ar[i]

    return ar[:10]    


#Insertion Sort
def insertion_sort(ar):
    n_elementos = len(ar)
    for i in range(1, n_elementos):
        aux = ar[i]
        j = i - 1
        while j >= 0 and aux < ar[j]:
            ar[j + 1] = ar[j]
            j -= 1
        ar[j + 1] = aux

    return ar[:10]



def contador_sort(metodosort):
    inicio = time.time()
    ar = gerar_array(15000)

    print(metodosort(ar))

    fim = time.time()
    tempo_de_execucao = fim - inicio
    print("Tempo de execução: {:.2f} segundos".format(tempo_de_execucao))


contador_sort(bubble_sort)
contador_sort(selection_sort)
contador_sort(insertion_sort)
