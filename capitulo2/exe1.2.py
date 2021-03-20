# Calcula as raizes de uma equação do segundo grau.
# f(x) = ax**2 + b*x + c

def f(a, b, c):
    x1 = (-b + (b**2 - 4*a*c)**(1/2)) / (2*a)
    x2 = (-b - (b**2 - 4*a*c)**(1/2)) / (2*a)
    return x1, x2


x1, x2 = f(1, 0.25, -5)

print("\nValor de x1 é: {0:.2f}".format(x1))
print("Valor de x2 é: {0:.2f}".format(x2))