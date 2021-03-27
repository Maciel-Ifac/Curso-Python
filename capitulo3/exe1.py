# Exercício 1

# 1.1
L = [1, 2]
L3 = 3*L
print(L3)

# 1.2
print(L3[0],L3[-1]) # L3[10] gera um erro, pois não existe nesta lista!

# 1.3
L4 = [k**2 for k in L3] # Eleva cada elemento da lista ao quadrado.
print(L4)

# 1.4. Podemos concatenar L3 e L4 de várias formas. Segue dois exemplos:

L5 = L3 + L4 # Soma
L5 = [*L3,*L4] # Desempacotamento
print(L5)
'''
Ver link, pois é bem interessante:
https://www.delftstack.com/pt/howto/python/how-to-concatenate-two-or-multiple-lists-in-python/
'''
