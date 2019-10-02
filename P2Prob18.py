import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
from numpy import linalg as LA

len = 100

#Given points
O1 = np.array([0,0]) 
O2 = np.array([3,4]) 

#Reqired parameters
d = np.linalg.norm(O1-O2)
m_1 = dir_vec(O1,O2)
n_1 = norm_vec(O1,O2)

#Radii of the circles
r1 = 3
r2 = 4
r3 = (r1 + r2 + d)/2

#Points M and N
M = O1 - r1*m_1/d
N = O2 + r2*m_1/d

#Center of circle C3
O3 = (M+N)/2
#print(O3)

#Generating Circles
C_1 = circ(O1,r1)
C_2 = circ(O2,r2) 
C_3 = circ(O3,r3)

#Finding points W, X, Y, Z
n_2 = np.array([3,4])
m_2 = omat@n_2
c = np.zeros(2)
c[0] = n_1@O3
c[1] = 9
X, Y = intersec_pts(n_1,n_2,c,O1,r1)
W, Z = intersec_pts(n_1,n_2,c,O3,r3)

#parabola
V = np.array([(1,0),(0,0)])
k = np.zeros(2)
k[0] = -3
k[1] = ((k[0])*(k[0]))/8
a = -15/(n_2@k)
#print(a)

#Given parabola parameters
u = -0.5*np.array([0,3])
F = 0
g = u 

par = parab(V,u,g,F,8*a)
plt.plot(par[0,:],par[1,:],label='Parabola')
 
#Areas
MZN = area(M,Z,N)
ZMW = area(Z,M,W)
res = round(MZN/ZMW,2)

print("(i) is",ifelse(round(np.array([2,1])@O3),6))
print("(ii) is",ifelse(a,10/3))
print("(iii) is",ifelse(res,1.25))
print("(iv) is",ifelse(a,21/5))
 
#Generating line points
l1 = line_dir_pt(m_1,O3,-2,2)
tan = line_dir_pt(n_1,M,-3,1)
ZW = line_gen(Z,W)

#Plotting circles
plt.plot(C_1[0,:],C_1[1,:],label='$C_1$')
plt.plot(C_2[0,:],C_2[1,:],label='$C_2$')
plt.plot(C_3[0,:],C_3[1,:],label='$C_3$')

#Plotting all the lines
plt.plot(l1[0,:],l1[1,:])
plt.plot(ZW[0,:],ZW[1,:])
plt.plot(tan[0,:],tan[1,:],label='$Tangent$')

#Plotting all the points
plt.plot(O1[0], O1[1], 'o')
plt.text(O1[0] * (1 - 0.5), O1[1] * (1 + 0.25) , '$O_1$')
plt.plot(O2[0], O2[1], 'o')
plt.text(O2[0] * (1 + 0.1), O2[1] * (1 - 0.2) , '$O_2$')
plt.plot(O3[0], O3[1], 'o')
plt.text(O3[0] * (1 + 0.1), O3[1] * (1 - 0.1) , '$O_3$')
plt.plot(M[0], M[1], 'o')
plt.text(M[0] * (1 + 0.1), M[1] * (1 - 0.1) , 'M')
plt.plot(N[0], N[1], 'o')
plt.text(N[0] * (1 + 0.1), N[1] * (1 - 0.1) , 'N')
plt.plot(X[0], X[1], 'o')
plt.text(X[0] * (1 + 0.1), X[1] * (1 - 0.1) , 'X')
plt.plot(Y[0], Y[1], 'o')
plt.text(Y[0] * (1 + 0.1), Y[1] * (1 - 0.1) , 'Y')
plt.plot(Z[0], Z[1], 'o')
plt.text(Z[0] * (1 + 0.2), Z[1] * (1 + 0.2) , 'Z')
plt.plot(W[0], W[1], 'o')
plt.text(W[0] * (1 + 0.1), W[1] * (1 - 0.1) , 'W')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.show()

