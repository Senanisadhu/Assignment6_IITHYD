import numpy as np
import matplotlib.pyplot as plt
import math


def dir_vec(B,E):
  return E-B



#Area using Hero's formula
def tri_hero(b,e,n):
  s = (b+e+n)/2
  area = np.sqrt(s*(s-b)*(s-e)*(s-n))
  return area
def tri_section(B,E,k):
  V = (k*B+E)/(k+1)
  return V

#Generate line points
def line_gen(B,E):
  len =10
  dim = B.shape[0]
  x_BE = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = B + lam_1[i]*(E-B)
    x_BE[:,i]= temp1.T
  return x_BE

#Triangle vertices
def tri_vert(b,e,n):
  w = (b**2 + n**2-e**2 )/(2*b)
  z = np.sqrt(n**2-w**2)
  B = np.array([w,z])
  E = np.array([0,0])
  N = np.array([b,0])
  return  B,E,N
def line_dir_pt(m,B, dim):
  len = 10
  dim = B.shape[0]
  x_BE = np.zeros((dim,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = B + lam_1[i]*m
    x_BE[:,i]= temp1.T
  return x_BE

len = 100
degrad = 180/np.pi

#Quadrilateral sides
i=5.6 #diagonal BN
j=6.5 #diagonal DE
b=e=n=d=math.sqrt((i/2)**2+(j/2)**2)
print(b)
#theta1 = P
t1 = np.arccos((b**2+j**2-e**2)/(2*b*j))



#Rotation matrix for t1
X = np.array(([np.cos(t1),-np.sin(t1)],[np.sin(t1),np.cos(t1)]) )



#Quadrilateral vertices
D,E,N =  tri_vert(b,e,j)
B1,E1,D1 =  tri_vert(j,n,d)
B = X@B1

#Printing coordinates
print(B1,B,E,N,D)

#Generating all lines
x_BE = line_gen(B,E)
x_EN = line_gen(E,N)
x_NB = line_gen(B,N)
x_ED = line_gen(E,D)
x_DB = line_gen(D,B)
x_ND = line_gen(N,D)



#Plotting all lines
plt.plot(x_BE[0,:],x_BE[1,:],label='$BE$')
plt.plot(x_EN[0,:],x_EN[1,:],label='$EN$')
plt.plot(x_NB[0,:],x_NB[1,:],label='$NB$')
plt.plot(x_ED[0,:],x_ED[1,:],label='$ED$')
plt.plot(x_DB[0,:],x_DB[1,:],label='$DB$')
plt.plot(x_ND[0,:],x_ND[1,:],label='$ND$')


plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 + 0.1), B[1] * (1 - 0.1) , 'B')

plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 - 0.2), E[1] * (1) , 'E')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1 + 0.03), N[1] * (1 - 0.1) , 'N')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')