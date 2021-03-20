import matplotlib.pyplot as plt
import numpy as np

# Exercício1: Verificar se x = 2.3 é raiz da f(x)

# Definindo a função


def f(x):
    return x**2 + 0.25*x - 5


# Plotando a função
x = np.linspace(-10, 10)

plt.grid()
plt.plot(x, f(x))
plt.xlim(-10, 10)
plt.ylim(-5, 93)
plt.show()

# Imprimindo resultado
print(f(2.3))print("O valor de x é: {0:.5f}".format(f(2.11456)))