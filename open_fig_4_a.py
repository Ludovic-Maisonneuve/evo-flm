import matplotlib.pyplot as plt
import numpy as np

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

L_tm = np.load('results/fig_4_a/L_tm.npy')
L_tf = np.load('results/fig_4_a/L_tf.npy')
L_pf = np.load('results/fig_4_a/L_pf.npy')
eps = 0.01
res = 250
L_cri = np.linspace(0, 10 * eps, res)

# ymin = -0.3589701495096897
# ymax = 1.0647128642623662

fig, ax = plt.subplots()
plt.plot(L_cri[:len(L_tm)], L_tm, label=r'$\overline{t}_m^*$', color=yellow, alpha=1)
plt.plot(L_cri[:len(L_tm)], L_tf, label=r'$\overline{t}_f^*$', color=purple)
plt.plot(L_cri[:len(L_tm)], L_pf, label=r'$\overline{p}_f^*$', color=purple, linestyle=(0, (3, 4)), alpha=1)
# plt.legend()
# plt.xlabel(r'strength of RI ($c_{RI}$)')
# plt.ylabel('equilibrium trait value')
xmin, xmax = plt.xlim()
plt.xlim(xmin, xmax)
ax.hlines(0, xmin, xmax, color=blue, linestyles='dashed')
ax.hlines(1, xmin, xmax, color=red, linestyles='dashed')
# ymin, ymax = plt.ylim()
# plt.ylim(ymin, ymax)
plt.tight_layout()
