# OBI 2023 - Fase 01
# Níveis: 2 e Sênior

saldo = int(input())
contas = []

for _ in range(3):
    contas.append(int(input()))

contas.sort()
qt = 0
soma = 0
for i in range(3):
    if (contas[i] + soma <= saldo):
        qt += 1
        soma += contas[i]
    else:
        break

print(qt)
