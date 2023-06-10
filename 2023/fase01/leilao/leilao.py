# OBI 2023 - Fase 01
# Nível: 2

lances = int(input())

maior = -1
dono = ''

for i in range(lances):
    nome = input()
    valor = int(input())
    if (valor > maior):
        maior = valor
        dono = nome

print(dono)
print(maior)
