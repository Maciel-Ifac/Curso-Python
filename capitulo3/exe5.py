import matplotlib.pyplot as plt 

# Exercício 5

# Primeira conta h = 1/1000
u1h = {}
u2h = {}
a = -0.5
h = 1/1000
u1h[0]= 1.0
u1h[1]= 10**(h*a)
u1h[2]=10**(2*h*a)

# Segunda conta h = 1/10
u1h1 = {}
u2h1 = {}
h1 = 1/10
u1h1[0]= 1.0
u1h1[1]= 10**(h1*a)
u1h1[2]=10**(2*h1*a)

for n in range(0,1000):
    u1h[n+3]= u1h[n+2] + h*a*((23/12)*u1h[n+2]-(4/3)*u1h[n+1]*(5/12)*u1h[n])
    u2h[n] = 10**(a*n*h)

    u1h1[n+3]= u1h1[n+2] + h1*a*((23/12)*u1h1[n+2]-(4/3)*u1h1[n+1]*(5/12)*u1h1[n])
    u2h1[n] = 10**(a*n*h1)
    #print(u[n],td[n],u1[n]) 

fig, ax1 = plt.subplots()

# These are in unitless percentages of the figure size. (0,0 is bottom left)
left, bottom, width, height = [0.52, 0.5, 0.35, 0.35]
ax2 = fig.add_axes([left, bottom, width, height])

ax1.plot(u1h1.values(), color='red',label='u1h1')
ax1.plot(u2h1.values(), color='blue', label='u2h1')
ax1.legend(loc='lower right', shadow=True)
ax1.set(xlabel='(n)', ylabel='(u1h1),(u2h1)')
ax1.set_xlim(0, 1000)
ax1.set_ylim(0, 1)

ax2.set_xlim(0, 1000)
ax2.set_ylim(0, 1)

ax2.plot(u1h.values(), color='red',label='u1h')
ax2.plot(u2h.values(), color='blue',label='u2h')
ax2.legend(loc='lower right', shadow=True)
plt.xlabel("(n)")
plt.ylabel('(u1h,u2h)')
#plt.legend()
plt.show()

'''
plt.plot(u.values(),label='u')
plt.plot(u1.values(),label='u1')
plt.xlabel("(n)")
plt.ylabel('u(n),u1(n)')
plt.xlim(0, 1000)
plt.ylim(0.3, 1)
plt.legend()
plt.show()
'''