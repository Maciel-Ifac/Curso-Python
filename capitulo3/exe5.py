import matplotlib.pyplot as plt 


# Exercício 5
u = {}
td = {}
u1 = {}
a = -0.5
h = 1/1000
u[0]= 1.0
u[1]= 10**(h*a)
u[2]=10**(2*h*a)



for n in range(0,1000):
    u[n+3]= u[n+2] + h*a*((23/12)*u[n+2]-(4/3)*u[n+1]*(5/12)*u[n])
    
    td[n]= n*h
    
    u1[n] = 10**(a*n*h)

    #print(u[n],td[n],u1[n])

plt.plot(u.values(),label='MUV')
plt.plot(u1.values())
plt.legend(loc='lower right', shadow=True)
plt.show()