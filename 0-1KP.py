import numpy as np
import sys
import os
import math
import random
import time
import matplotlib.pyplot as plt

#提取数据

file = open("idkp1-10.txt", 'r+')
num = 0    #记录行号
print('请输入要提取的数据组数（0-10）：')
user = int(input())
for line in file:
    num = num + 1
    if user == 0:
        cubage = 10149
        diemnsion = 3 * 10
    if user == 1:
        cubage = 61500
        diemnsion = 3 * 100
    if user == 2:
        cubage = 103936
        diemnsion = 3 * 200
    if user == 3:
        cubage = 214453
        diemnsion = 3 * 300
    if user == 4:
        cubage = 251980
        diemnsion = 3 * 400
    if user == 5:
        cubage = 297482
        diemnsion = 3 * 500
    if user == 6:
        cubage = 415217
        diemnsion = 3 * 600
    if user == 7:
        cubage = 434677
        diemnsion = 3 * 700
    if user == 8:
        cubage = 464860
        diemnsion = 3 * 800
    if user == 9:
        cubage = 454989
        diemnsion = 3 * 900
    if user == 10:
        cubage = 496541
        diemnsion = 3 * 1000
    if (num == user * 8 + 6) :
        V = line.strip().split(',')
    if (num == user * 8 + 8):
        W = line.strip().split(',')
print('价值：', V)
print('重量：', W)


#画散点图


del W[-1]
del V[-1]
x = list(map(int, W))
y = list(map(int, V))
plt.scatter(x, y)
plt.show()
#print(x)


#项集第三项的价值:重量比的非递增排序

Ratio = []     #项集所有项比值
Ratio_1 = []    #第三项比值排序
n = len(x)
for i in range(n):
    ratio = y[i]/x[i]
    Ratio.append(ratio)
for i in range(2, len(Ratio), 3):
    ratio_1 = Ratio[i]
    Ratio_1.append(ratio_1)
Ratio_1.sort(reverse=True)
print('排序结果为：', Ratio_1)



#用户能够自主选择动态规划算法、回溯算法求解指定D{0-1} KP数据的最优解和求解时间（以秒为单位）


best = []
m = cubage    #m为背包最大容量
bag = []

start =time.time()
for i in range(len(x)):    # bag表示物品的重量与其所对应的质量
    bag.append([])
    for j in range(2):
        weight = x[i]
        value = y[i]
        if j == 0:
            bag[i].append(weight)
        if j == 1:
            bag[i].append(value)
#print(bag)
for i in range(len(bag)):
    best.append([0]*(m+1))
for i in range(m+1):
    if i >= bag[0][1]:
        best[0][i] = bag[0][0]    #第一次遍历数组将得到第一个物品所对应的最大质量得出

for i in range(1, len(bag)):
    for j in range(m+1):
        if bag[i][1] <= j:
            best[i][j] = max(best[i-1][j], best[i-1][j-bag[i][1]]+bag[i][0])    # 取best[i][j]当前的最大质量
end = time.time()

print('最优解为：', best[-1][-1])  # 打印best最终j=m(背包最大容量)的最大质量
print('运行时间为: %s 秒'%(end-start))    #其中end-start就是程序运行的时间，单位是秒。


#结果保存为txt文件

Best = best[-1][-1]
f = open("best_result.txt", 'w')
f.write('最优解为：')
f.write(str(Best))
f.write('\n')
f.write('运行时间为：')
f.write(str(end-start))
f.close()
