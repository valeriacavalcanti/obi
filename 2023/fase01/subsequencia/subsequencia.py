# OBI 2023 - Fase 01
# Níveis: 1 e Sênior

ta, tb = [int(x) for x in input().split()]
sa = [int(x) for x in input().split()]
sb = [int(x) for x in input().split()]

a, b = 0, 0

while (True):
    if (a < ta) and (b < tb):
        if (sa[a] == sb[b]):
            b += 1
        a += 1
    else:
        break

if (b == tb):
    print("S")
else:
    print("N")
