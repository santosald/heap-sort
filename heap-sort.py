import math

# filho da esq;
def left(i):
    return (2*i)

# filho da dir;
def right(i):
    return (2*i) + 1

# comparar o pai com os filhos e troca com o maior (se houver);
def max_heapify(A, i, tam):

    maior = i
    l = left(i)
    r = right(i)

    if (l <= tam-1):
        if (A[l] > A[i]):
            maior = l

    if (r <= tam-1):
        if (A[r] > A[maior]):
            maior = r

    if maior != i:
        A[i], A[maior] = A[maior], A[i]
        max_heapify(A, maior, tam)

    else:
        pass


# constrói o heap garantindo a carac. de máx;
def build_max_heap(A):

    tam = len(A)

    # começando do piso da metade do tamanho do vetor, indo até a raiz;
    for i in range(math.floor(tam/2), 0, -1):
        max_heapify(A, i, tam)    

# ordena o array extraíndo a raíz e decrementando o tam a cada iteração;
def heap_sort(A):

    build_max_heap(A)
    tam = len(A)

    for i in range(tam-1, 1, -1):
        A[1], A[i] = A[i], A[1]
        tam = tam - 1
        max_heapify(A,1,tam)
        

# drive do programa
if __name__ == '__main__':

    B = []

    f = open('num.1000.txt', 'r')   # endereço do arquivo de texto.
    for line in f:
        B.append(int(line))
    
    f.close()

    A = [len(B)] + B

    heap_sort(A)
    print(A)
