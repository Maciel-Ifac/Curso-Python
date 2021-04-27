print("Determina o mdc de dois números n > 0 e m > 0\n")

# leia o valor de n
n = int(input("Digite o valor de n (n > 0): "))

# leia o valor de m
m = int(input("Digite o valor de m (m > 0): "))

# aqui começa o algoritmo de Euclides
anterior = n
atual    = m
resto    = anterior % atual

while resto != 0:
    anterior = atual
    atual    = resto
    resto    = anterior % atual

print("MDC(%d,%d)=%d" %(n,m,atual))