l=[3, 15, 8, 9, 1]

def nome(c):

    while True:
        for j in range(len(l)):
            if c == l[j]:
                index = j
                return index

print(l)
f = int(input('Digite um número da lista:'))
print('O index do número é:', nome(f))
