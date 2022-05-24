# 几何布朗运动的随机过程下的蒙特卡洛模拟
import numpy as np

S0 = 50  ##标的股票价格
sigma = 0.3  ##年化波动率
K = 50  ##行权价
T = 1.0  ##到期时间
r = 0.05  ##无风险利率
I = 100000  ##模拟次数
M = 365  #拟合天数
z = np.random.standard_normal((M + 1, I))  # 正态分布随机项，维持变量统一
dt = T / M  #时间微分变量

####(a)
S0_a = np.zeros((M + 1, I))#初始化参数
S0_a[0] = S0
for t in range(1, M + 1):
    S0_a[t] = S0_a[t - 1] * np.exp(
        (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z[t])  #进行资产价格模拟
S0_a = S0_a[-1] #得出规定时间的资产价格
C0_a = np.exp(-r * T) * np.mean(np.maximum(S0_a - K, 0))  #计算期权估计价格

####(b)
min_val = 15  #设置敲入阈值
max_val = 90  #设置敲出阈值
S0_b = np.zeros((M + 1, I))#初始化参数
S0_b[0] = S0
for t in range(1, M + 1):
    S_sub = S0_b[t - 1] * np.exp(
        (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z[t])  #进行资产价格模拟
    S_pick_1 = (S_sub <= min_val)#添加(2)题的约束条件
    S_pick_2 = (S_sub >= max_val)
    S_sub[S_pick_1 + S_pick_2] = 0
    S0_b[t] = S_sub
S0_b = S0_b[-1] #得出规定时间的资产价格
C0_b = np.exp(-r * T) * np.mean(np.maximum(S0_b - K, 0))  #计算期权估计价格

####(c)
ds = 0.0001 #设置扰动项
##重复(a)(b)操作获取新的结果
S0_a_delta = np.zeros((M + 1, I))#初始化参数
S0_a_delta[0] = S0 + ds
for t in range(1, M + 1):
    S0_a_delta[t] = S0_a_delta[t - 1] * np.exp(
        (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z[t])  #进行资产价格模拟
S0_a_delta = S0_a_delta[-1] #得出规定时间的资产价格
C0_a_delta = np.exp(-r * T) * np.mean(np.maximum(S0_a_delta - K, 0))  #计算期权估计价格
S0_b_delta = np.zeros((M + 1, I))#初始化参数
S0_b_delta[0] = S0 + ds
for t in range(1, M + 1):
    S_sub = S0_b_delta[t - 1] * np.exp(
        (r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z[t])  #进行资产价格模拟
    S_pick_1 = (S_sub <= min_val)#添加(2)题的约束条件
    S_pick_2 = (S_sub >= max_val)
    S_sub[S_pick_1 + S_pick_2] = 0
    S0_b_delta[t] = S_sub
S0_b_delta = S0_b_delta[-1] #得出规定时间的资产价格
C0_b_delta = np.exp(-r * T) * np.mean(np.maximum(S0_b_delta - K, 0))  #计算期权估计价格
delta_a = (C0_a_delta - C0_a) / np.mean(S0_a_delta - S0_a) #计算Delta
delta_b = (C0_b_delta - C0_b) / np.mean(S0_b_delta - S0_b)

print('(a)题中期权估计价值为：{}， Delta为{}'.format(C0_a, delta_a))
print('(b)题中期权估计价值为：{}， Delta为{}'.format(C0_b, delta_b))

