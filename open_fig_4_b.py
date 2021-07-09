import matplotlib.pyplot as plt
import numpy as np
import os

SMALL_SIZE = 8
MEDIUM_SIZE = 18
BIGGER_SIZE = 22

plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

blue = np.array([67 / 255, 114 / 255, 189 / 255])
red = np.array([159 / 255, 58 / 255, 65 / 255])
purple = np.array([0.32, 0.106, 0.575])
yellow = np.array([0.948, 0.83, 0.148])

res = 250
L_tm = np.load('results/fig_4_b/L_tm.npy')
L_tf = np.load('results/fig_4_b/L_tf.npy')
L_pf = np.load('results/fig_4_b/L_pf.npy')

# thisdir = 'results/fig_6'
# for r, d, f in os.walk(thisdir):  # r=root, d=directories, f = files
#     for file in f:
#         if file != '.DS_Store':
#             f = file.split("_")
#             if int(f[0]) == 249:
#                 X = np.load(thisdir + '/' + f[0] + '_' + f[1][:-4] + '.npy')
#                 L_tm[int(f[1][:-4])] = X[0]
#                 L_tf[int(f[1][:-4])] = X[1]
#                 L_pf[int(f[1][:-4])] = X[2]

eps = 0.01
res = 250
L_a = np.linspace(0, 20, res)
L_a = L_a[:len(L_tm)]
# ymin = -0.3589701495096897
# ymax = 1.0647128642623662

fig, ax = plt.subplots()
plt.plot(L_a, L_tm, label=r'$\overline{t}_m^*$', color=yellow, alpha=1)
plt.plot(L_a, L_tf, label=r'$\overline{t}_f^*$', color=purple)
plt.plot(L_a[1:], L_pf[1:], label=r'$\overline{p}_f^*$', color=purple, linestyle=(0, (3, 4)), alpha=1)
# plt.legend()
# plt.xlabel(r'$a$')
xmin, xmax = plt.xlim()
plt.xlim(xmin, xmax)
ax.hlines(0, xmin, xmax, color=blue, linestyles='dashed')
ax.hlines(1, xmin, xmax, color=red, linestyles='dashed')
ymin, ymax = plt.ylim()
plt.ylim(ymin, ymax)
plt.tight_layout()
