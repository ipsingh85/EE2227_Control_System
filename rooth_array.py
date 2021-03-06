
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cmath
from matplotlib import cm

# Coefficients of Given Polynomial
Coeff = np.array([1,3,3,9])
# Roots of given Polynomial
Roots = np.roots(Coeff)
	
def Creating_RH_Matrix(Coeff,epsilon=1e-5):
	
	l = Coeff.shape[0]
	
	# Creating a Routh-Hurwtiz Matrix with all elements as zeros
	RH = np.zeros((l,int(np.ceil(l/2))))

	# Assigning Elements to First Row of Matrix
	RH[0] = Coeff[0::2]

	# Assigning Elements to Second Row of Matrix
	if RH.shape[1] >= Coeff[1::2].shape[0]:
		x = Coeff[1::2].shape[0]
		RH[1,:x] = Coeff[1::2]

	# As First Elements of Row cannot be zeros replacing them by a small value
	if (RH[0][0] == 0):
		RH[0][0] = epsilon
	if (RH[1][0] == 0):
		RH[1][0] = epsilon
	
	return RH


def RH_Matrix(Coeff,epsilon=1e-5):
	
	
	RH = Creating_RH_Matrix(Coeff,epsilon)
	l = Coeff.shape[0]
			
	for i in range(2,l):
		a = RH[i-2]
		b = RH[i-1]
		a1,a2 = a[0],b[0]
		for j in range(1,a.shape[0]):
			b1,b2 = a[j],b[j]
			Det = (a2*b1 - a1*b2)/a2
			RH[i][j-1] = Det
			
			# Checking Ratio of above 2 Rows.
			# The following for loop classifies whether it is Case (b) or Case(c)
			t = []
			it=0
			for m in range(a.shape[0]):
				if (a[m] != 0 and b[m] != 0):
					it = it+1
					if (m==0):
						d = a[m]/b[m]
						t.append(1)
					else:
						c = a[m]/b[m]
						if (c==d):
							t.append(1)
						else:
							t.append(0)
		
		# Case (b)
		if (np.sum(t) == it and RH[i][0] == 0):
			for k in range(b.shape[0]):
				RH[i][k] = (l-i- 2*k) * b[k]
		
		# Case (c)	
		elif (RH[i][0] == 0 and np.sum(t) != it):
			RH[i][0] = epsilon
		
	return RH

def Sign_Changes(RH):
	"""
	The function calculates no.of sign changes in RH Matrix
	"""
	output = 0
	l = RH.shape[0]
	for i in range(l-1):
		a = RH[i][0]
		b = RH[i+1][0]
		
		if a*b < 0:
			output += 1
			
	print ("No.of Roots on Right of Y-axis are",output)

# Printing Routh Hurwitz Matrix
RH = RH_Matrix(Coeff)
print ("Routh Hurwitz Matrix:")
print (RH)

# Sign Changes in Routh Hurwitz Matrix
Sign_Changes(RH)

# Plotting the Roots of Given Polynomial
plt.axhline(y=0, color='black',linewidth=0.5)
plt.axvline(x=0, color='black',linewidth=0.5)
plt.scatter(Roots.real,Roots.imag,color='red')
plt.show()
