import torch
import torch.nn as nn

# 定义输入张量
L, S, N, E = 10, 20, 32, 1024
Q = torch.randn(L, 1, E)
K = torch.randn(S, N, E)
V = torch.randn(S, N, E)

# 实例化MultiheadAttention模块
attention = nn.MultiheadAttention(embed_dim=E, num_heads=8)

# 进行张量计算
output, _ = attention(Q, Q, Q)
output1, _ = attention(Q, Q, Q)
print(output.shape)
