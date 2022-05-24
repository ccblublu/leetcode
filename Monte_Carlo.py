from ast import Num
import numpy as np
import matplotlib.pyplot as plt
from numpy import random as npr
from tqdm import tqdm

class MonteCarlo:

    def __init__(self):
        self.sigma = 0.3  # 波动率
        self.r = 0.05  #贴现的无风险利率
        self.min_val = 15  #敲入
        self.max_val = 90  #敲出
        self.I = 100000  #拟合次数
        self.M = 365  #拟合天数
        self.S0 = 50  #股票价格
        self.K = 50  #行权价格
        self.T = 1.0  #到期年化时间

    def gbm_mcs(self, z, ds=0.):
        '''
        基于几何布朗运动生成资产价格
        '''
        S = np.zeros((self.M + 1, self.I))
        S[0] = self.S0 + ds
        S_2 = S.copy()
        dt = self.T / self.M  #时间微分变量
        for t in range(1, self.M + 1):
            S[t] = S[t - 1] * np.exp(
                (self.r - 0.5 * self.sigma**2) * dt +
                self.sigma * np.sqrt(dt) * z[t])  #进行资产价格模拟

            S_sub = S_2[t - 1] * np.exp(
                (self.r - 0.5 * self.sigma**2) * dt +
                self.sigma * np.sqrt(dt) * z[t])  #(2)题的约束条件
            S_pick_1 = (S_sub <= self.min_val)
            S_pick_2 = (S_sub >= self.max_val)
            S_sub[S_pick_1 + S_pick_2] = 0
            S_2[t] = S_sub

        # S = S[-1] #得出规定时间的资产价格
        min_y = np.array([self.min_val]*(self.M+1))
        max_y = np.array([self.max_val]*(self.M+1))
        # plt.figure(figsize=(10,8))
        # plt.hist(S[-1], bins=50)
        # plt.savefig('./hist.png')
        # plt.close()

        plt.figure(figsize=(10,8))
        plt.plot(S[:,0:100], lw=1.5)
        # plt.plot(min_y, lw=2, color= 'black', label='敲入')
        # plt.plot(max_y, lw=2, color= 'black', label='敲出')
        plt.ylim(0,110)
        plt.savefig('./Q1.png')
        # plt.show()
        plt.close()

        plt.figure(figsize=(10,8))
        plt.plot(S_2[:,0:100], lw=1.5)
        plt.plot(min_y, lw=2, color= 'black', label='敲入')
        plt.plot(max_y, lw=2, color= 'black', label='敲出')
        plt.ylim(0,110)
        plt.savefig('./Q2.png')
        # plt.show()
        plt.close()
        '''
        基于蒙特卡洛模拟法计算期权估计价值
        '''
        C0_a = np.exp(-self.r * self.T) * np.mean(np.maximum(
            S[-1] - self.K, 0))  #(1)题
        C0_b = np.exp(-self.r * self.T) * np.mean(
            np.maximum(S_2[-1] - self.K, 0))  #(2)题
        return C0_a, C0_b, S[-1], S_2[-1]

    def cal_delta(self,ds):
        z = npr.standard_normal((self.M + 1, self.I))  # 正态分布随机项，维持变量统一
        C0_a, C0_b, S0, S0_2 = self.gbm_mcs(z)
        C1_a, C1_b, S1, S1_2 = self.gbm_mcs(z, ds)
        delta_a = (C1_a - C0_a) / np.mean(S1 - S0)
        # delta_b = (C1_b - C0_b) / np.mean(S1_2 - S0_2)
        print('(1)题中期权估计价值为：{}， Delta为{}'.format(C0_a, delta_a))
        print('(2)题中期权估计价值为：{}， Delta为{}'.format(C0_b, delta_b))
        return C0_a, delta_a,C0_b, delta_b

if __name__ == "__main__":
    s = MonteCarlo()
    c0_1 = []
    c0_2 = []
    delta_1 = []
    delta_2 = []
    for i in tqdm(range(1)):
        C0_a, delta_a,C0_b, delta_b = s.cal_delta(0.0001)
        c0_1.append(C0_a)
        c0_2.append(C0_b)
        delta_1.append(delta_a)
        delta_2.append(delta_b)
    # plt.figure(figsize=(10,8))
    # plt.plot(c0_1, lw=2, label='(1)')
    # plt.ylim(6.5,7.5)
    # plt.savefig('./C0_a.png')
    # plt.show()
    # plt.close()

    # plt.figure(figsize=(10,8))
    # plt.plot(c0_2, lw=2, label='(2)')
    # plt.ylim(4.5,5.5)
    # plt.savefig('./C0_b.png')
    # plt.show()
    # plt.close()

    # plt.figure(figsize=(10,8))
    # plt.plot(delta_1, lw=2, label='(1)')
    # plt.ylim(-1,1)
    # plt.savefig('./Delta_a.png')
    # plt.show()
    # plt.close()
    
    # plt.figure(figsize=(10,8))
    # plt.plot(delta_2, lw=2, label='(2)')
    # plt.ylim(-1,1)
    # plt.savefig('./Delta_b.png')
    # plt.show()
    # plt.close()
