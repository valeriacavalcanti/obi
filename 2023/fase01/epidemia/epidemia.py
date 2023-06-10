# OBI 2023 - Fase 01
# Nível: Júnior

d0 = int(input())
r = int(input())
acc = int(input())

soma = d0
dias = 0

while (soma < acc):
    dias += 1
    d0 *= r
    soma += d0

print(dias)
