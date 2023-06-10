# OBI 2023 - Fase 01
# Níveis: 1 e Sênior

# ATENÇÃO! ESSA SOLUÇÃO DÁ TLE !!

nseq, nsub = [int(n) for n in input().split()]
seq = [int(n) for n in input().split()]
sub = [int(n) for n in input().split()]

pos = 0
ok = True

for s in sub:
    # print("procurando ", s, "em", seq[pos:])
    if (s in seq[pos:]):
        pos = seq.index(s, pos)
        pos += 1
    else:
        ok = False
        break

if (ok):
    print("S")
else:
    print("N")
