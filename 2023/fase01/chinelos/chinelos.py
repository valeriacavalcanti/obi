# OBI 2023 - Fase 01
# Nível: Júnior

n = int(input())
estoque = [0]

for i in range(n):
    estoque.append(int(input()))

total = 0
pedidos = int(input())
for i in range(pedidos):
    tam = int(input())
    if (estoque[tam] > 0):
        estoque[tam] -=1
        total += 1

print(total)
