# OBI 2023 - Fase 01
# Níveis: 2 e Sênior

s, t = [int(x) for x in input().split()]
s += 1
m = [[0] * s for (x) in range(s)]

for _ in range(t):
    i, j = [int(x) for x in input().split()]
    m[i][j] = 1
    m[j][i] = 1

qt = int(input())
validos = 0
for _ in range(qt):
    caminho = [int(x) for x in input()[1:].split()]
    valido = True
    for i in range(0, len(caminho) - 1):
        vez = caminho[i]
        proximo = caminho[i + 1]
        if (m[vez][proximo] == 0):
            valido = False
            break
    if (valido == True):
        validos += 1

print(validos)
