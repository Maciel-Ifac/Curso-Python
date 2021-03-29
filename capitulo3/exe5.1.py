import matplotlib.pyplot as plt 
import numpy as np 

u = []
tb = []
a = -0.5
h = 1/1000
z = [] # lista e**(a*tb)
x = [] # lista contendo n valores inteiros (0,...,1003)

u.insert(0,1.0)
u.insert(1,10**(h*a))
u.insert(1,10**(2*h*a))

for n in range(0,1000):
    u.append(u[n+2] + h*a*((23/12)*u[n+2]-(4/3)*u[n+1]*(5/12)*u[n]))
    
for n in range(0,1003):
    tb.append(10**(n*h))
    z.append(10**(10**(n*h)))
    x.append(n)

dif = np.absolute(np.array(z) - np.array(u)) # dif = |e**(a*tb) – u |

# Primeiro Gráfico tb x u
#plt.plot(tb,u) 

# Segundo Gráfico |e**(a*tb) – u |
'''
plt.subplot(1,2,1)
plt.plot(tb,u)
plt.subplot(1,2,2)
plt.plot(x,dif)
'''
fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.plot(tb, u,color ='blue',linewidth = 1.5)
ax2.plot(x, dif,color ='blue',linewidth = 1.5)
ax1.set(ylabel='Probabilidade', xlabel='Posição(j)')
ax2.set(ylabel='Probabilidade', xlabel='Posição(j)')
fig.set_size_inches(7, 2) # dimensão da figura(altura-largura)
plt.tight_layout()#regulariza a distância entre os gráficos