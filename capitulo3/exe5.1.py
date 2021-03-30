import matplotlib.pyplot as plt 
import numpy as np 

u = []
tb = []
a = -0.5
h = 1/1000
z = [] # lista e**(a*tb)
x = [] # lista contendo n valores inteiros (0,...,1003)


u.insert(0,1.0)
u.insert(1,np.exp(h*a))
u.insert(1,np.exp(2*h*a))

for n in range(0,1000):
    u.append(u[n+2] + h*a*((23/12)*u[n+2]-(4/3)*u[n+1]*(5/12)*u[n]))
    
for n in range(0,1003):
    tb.append(np.exp(n*h)) 
    z.append(np.exp(a*n*h))
    x.append(n)

dif = np.absolute(np.array(z) - np.array(u)) # dif = |e**(a*tb) – u |

# Plotando resultados !!!

fig, (ax1, ax2) = plt.subplots(1, 2)

ax1.plot(tb, u,color ='blue',linewidth = 2.0)
ax1.set_ylabel('tb', fontsize=20) # eixo y
ax1.set_xlabel('u', fontsize=20)  # eixo x
ax1.set_title('')

ax2.plot(x, dif,color ='blue',linewidth = 2.0)
ax2.set_ylabel('dif', fontsize=20) # eixo y
ax2.set_xlabel('x', fontsize=20)  # eixo x


fig.set_size_inches(7, 2) # dimensão da figura(altura-largura)
plt.tight_layout()#regulariza a distância entre os gráficos
plt.show()