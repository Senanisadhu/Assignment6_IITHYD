import numpy as np
import matplotlib.pyplot as plt



def dir_vec(J,U):
  return U-J



#Area using Hero's formula
def tri_hero(j,u,m):
  s = (j+u+m)/2
  area = np.sqrt(s*(s-j)*(s-u)*(s-m))
  return area
def tri_section(J,U,k):
  V = (k*J+U)/(k+1)
  return V

#Generate line points
def line_gen(J,U):
  len =10
  dim = J.shape[0]
  x_JU = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = J + lam_1[i]*(U-J)
    x_JU[:,i]= temp1.T
  return x_JU

#Triangle vertices
def tri_vert(j,u,m):
  w = (j**2 + m**2-u**2 )/(2*j)
  z = np.sqrt(m**2-w**2)
  J = np.array([w,z])
  U = np.array([0,0])
  M = np.array([j,0])
  return  J,U,M
def line_dir_pt(m,J, dim):
  len = 10
  dim = J.shape[0]
  x_JU = np.zeros((dim,len))
  lam_1 = np.linspace(0,10,len)
  for i in range(len):
    temp1 = J + lam_1[i]*m
    x_JU[:,i]= temp1.T
  return x_JU

len = 100
degrad = 180/np.pi

#Quadrilateral sides
j = 4 #UM
u = 5 #PM
m=4.5 #JP
p = 3.5 #JU
d = 6.5 #UP

#theta1 = PUM
t1 = np.arccos((j**2+d**2-u**2)/(2*j*d))
#theta2 = JUP
t2 = np.arccos((p**2+d**2-m**2)/(2*p*d))

print(t1*degrad,t2*degrad)

#Rotation matrix for t1
X = np.array(([np.cos(t1),-np.sin(t1)],[np.sin(t1),np.cos(t1)]) )



#Quadrilateral vertices
P,U,M =  tri_vert(j,u,d)
J1,U1,P1 =  tri_vert(d,m,p)
J = X@J1

#Printing coordinates
print(J1,J,U,M,P)

#Generating all lines
x_JU = line_gen(J,U)
x_UM = line_gen(U,M)
#x_MJ = line_gen(J,M)
x_UP = line_gen(U,P)
x_PJ = line_gen(P,J)
x_MP = line_gen(M,P)



#Plotting all lines
plt.plot(x_JU[0,:],x_JU[1,:],label='$JU$')
plt.plot(x_UM[0,:],x_UM[1,:],label='$UM$')
#plt.plot(x_MJ[0,:],x_MJ[1,:],label='$MJ$')
plt.plot(x_UP[0,:],x_UP[1,:],label='$UP$')
plt.plot(x_MP[0,:],x_MP[1,:],label='$MP$')
plt.plot(x_PJ[0,:],x_PJ[1,:],label='$PJ$')


plt.plot(J[0], J[1], 'o')
plt.text(J[0] * (1 + 0.1), J[1] * (1 - 0.1) , 'J')

plt.plot(U[0], U[1], 'o')
plt.text(U[0] * (1 - 0.2), U[1] * (1) , 'U')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.03), M[1] * (1 - 0.1) , 'M')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.03), P[1] * (1 - 0.1) , 'P')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')