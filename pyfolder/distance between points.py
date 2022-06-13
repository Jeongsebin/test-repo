import numpy as np
from scipy.spatial.distance import pdist, squareform

x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

d = squareform(pdist(x, 'euclidean'))
print(d)

#점들 사이의 거리 계산 A(0, 1) B(1, 0) C(2, 0) 3개중 2개뽑 = 3(순서상관 X)
# [[ 0            1.41421356   2.23606798 ]
#  [ 1.41421356   0            1          ]
#  [ 2.23606798   1            0          ]]
