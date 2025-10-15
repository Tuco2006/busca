def nome(l, c):
    for i in range(len(l)):
        if l[i] == c:
            return i
    return -1


l = []
usu = int(input('Digite o primeiro número da lista:'))
l.append(usu)
usu2 = int(input('Digite o segundo número da lista:'))
l.append(usu2)
usu3 = int(input('Digite o terceiro número da lista:'))
l.append(usu3)

print(l)
f = int(input('Digite um número da lista:'))
print('O index do número é:', nome(l, f))