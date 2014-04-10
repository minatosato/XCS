#!/usr/local/bin python
# -*- coding:utf-8 -*-

import os
import sys
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

performance = []
"""操作するファイルはperformance0.csvスタート"""
i = 0
file_path = "performance" + str(i) + ".csv"
while os.path.exists(file_path):
    pf = np.loadtxt(file_path,delimiter=",")
    performance.append(pf)
    i += 1
    file_path = "performance" + str(i) + ".csv"
"""データの数 = whileでインクリメントした分"""
data_num = i
"""データの中身の長さ = np.loadtxtしたデータのlen"""
data_length = len(np.loadtxt("performance0.csv",delimiter=","))
pf = []
"""0, 100, 200, 300, ..., data_length*100"""
x = np.arange(0,data_length*100,100)
for i in range(data_length):
    sum = 0.0
    for j in range(data_num):
    	sum += performance[j][i]
    pf.append(sum/float(data_num))
pf = np.array(pf)
np.savetxt("ave_performance.csv",pf,delimiter=",")
fig = plt.figure(figsize=(16, 10))
ax = fig.add_subplot(1,1,1)
ax.plot(x, pf, linewidth=2, label='performance')
ax.set_ylim(40, 110)
ax.set_xlim(0, data_length*100)
ax.set_title('Performance')
ax.set_yticklabels(['40%','50%','60%','70%','80%','90%','100%',''])
ax.grid()
filenamepng = "performance.png"
plt.savefig(filenamepng, dpi=150)
filenameeps = "performance.eps"
plt.savefig(filenameeps)
plt.show()

