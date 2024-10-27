import numpy as np

np1=np.array([1,2,3,4])
np2=np.array([5,6,7,8])

print(np.vstack((np1,np2)))

print(np.hstack((np1,np2)))

print(np.column_stack((np1,np2)))