# OBI 2023 - Fase 01
# Níveis: 2 e Sênior

# ATENÇÃO! ESSA SOLUÇÃO DÁ TLE !!

l, c = [int(n) for n in input().split()]
lista = []

for _ in range(c):
    i, j = [int(n) for n in input().split()]
    lista.append((i, j))

caminhos = int(input())
qt = 0
for _ in range(caminhos):
    percurso = [int(n) for n in input().split()]
    ok = True
    for i in range(1, percurso[0]):
        if ((percurso[i], percurso[i+1]) not in lista) and ((percurso[i+1], percurso[i]) not in lista):
            ok = False
            break
    if (ok):
        qt += 1

print(qt)
