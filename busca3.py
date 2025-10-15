def busca_binaria(l, c):
    ini = 0
    fin = len(l) -1

    while ini <= fin:
        mei = ini + fin // 2
        if c == l[mei]:
            return mei
        if c > l[mei]:
            ini = mei + 1
        else:
            fin = mei -1
    return -1

f = [12, 25, 37, 41, 53, 59, 68, 71, 95]
f2 = int(input('Digite um número da lista:'))
print(busca_binaria(f, f2))