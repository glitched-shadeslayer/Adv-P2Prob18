import numpy as np
from numpy import linalg as LA


def dir_vec(A,B):
  return B-A

def norm_vec(A,B):
  return omat@dir_vec(A,B)

#Generate line points
def line_gen(A,B):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def circ(O,r):
  len =100
  theta = np.linspace(0,2*np.pi,len)
  x_circ = np.zeros((2,len))
  x_circ[0,:] = r*np.cos(theta)
  x_circ[1,:] = r*np.sin(theta)
  x_circ = (x_circ.T + O).T
  return x_circ

 
#Intersection points
def intersec_pts(n_1,n_2,c,O,r):
	V = np.vstack((n_1,n_2))
	P = np.linalg.inv(V)@c
	m_2 = omat@n_2
	d = np.linalg.norm(P-O)
	l = np.sqrt(r*r - d*d)
	X = P + l*m_2/(np.linalg.norm(m_2))
	Y = P - l*m_2/(np.linalg.norm(m_2))
	return X,Y	

#Area of a triangle
def area(A,B,C):
	prod = np.cross((B-A),(C-A))
	area = np.linalg.norm(prod)/2
	return area	

#creating parabola
def parab(V,u,g,F,k):
    len = 100
    x1 = np.linspace(-0.75,0.75,len)
    x2 = np.power(x1,2)
    x = np.vstack((x1,x2))
    vcm = g-u
    vcp = g+u
    A = np.vstack((V,vcp.T))
    b = np.append(vcm,-F)
    d = LA.lstsq(A,b)[0]
    d = d.reshape(2,1)
    par = k*x + d
    return par

#If-else
def ifelse(A,B):
	if A == B:
		stat = True
	else:
		stat = False
	return stat
    
#Generate line points
def line_dir_pt(m,A,k1,k2):
  len =10
  x_AB = np.zeros((2,len))
  lam_1 = np.linspace(k1,k2,len)
  for i in range(len):
    temp1 = A + lam_1[i]*m
    x_AB[:,i]= temp1.T
  return x_AB

dvec = np.array([-1,1]) 
omat = np.array([[0,1],[-1,0]])
