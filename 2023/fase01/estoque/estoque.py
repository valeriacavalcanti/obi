# OBI 2023 - Fase 01
# Níveis: 1 - 2 - Sênior

l, c = [int(n) for n in input().split()]
estoque = [[0] * c]

for _ in range(l):
    estoque.append([0] + [int(n) for n in input().split()])

vendas = int(input())
qt = 0
for _ in range(vendas):
    l, c = [int(n) for n in input().split()]
    if (estoque[l][c] > 0):
        estoque[l][c] -= 1
        qt += 1

print(qt)
