import numpy as np
import torch
# A = np.array([[[1, 2, 3],
#                [4, 5, 6],
#                [7, 8, 9]],
#               [[11, 12, 13],
#                [14, 15, 16],
#                [17, 18, 9]]]
#          )
# B = np.array([
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ])
# print(A.shape)
# print(A[:, 0, 0:2])
# print(np.sum(A, axis=0))
# print(np.sum(A, axis=(0, 1)))
# print(np.sum(B, axis=0))
# 生成64x16的floatTensor
C = torch.FloatTensor(64, 16)
print(C)
print(C.shape)