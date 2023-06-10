# OBI 2023 - Fase 01
# Nível: Júnior

pao = int(input())
doce = int(input())
bolo = int(input())

pontos = pao + doce * 2 + bolo * 3

if (pontos >= 150):
    print("B")
elif (pontos >= 120):
    print("D")
elif (pontos >= 100):
    print("P")
else:
    print("N")
