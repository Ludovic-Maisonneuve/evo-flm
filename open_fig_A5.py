import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

SMALL_SIZE = 16
MEDIUM_SIZE = 20
BIGGER_SIZE = 25

plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

blue_div = np.array([61 / 255, 139 / 255, 240 / 255])
blue = np.array([67 / 255, 114 / 255, 189 / 255])
red = np.array([159 / 255, 58 / 255, 65 / 255])
red_div = np.array([240 / 255, 58 / 255, 65 / 255])
gmin = -1
gmax = 2
n = 50


def color(t):
    i = int(n * (t + 1) / 3)
    if t == float('inf'):
        c = np.array([0 / 255, 0 / 255, 0 / 255])
    elif i < n * (-gmin) / (gmax - gmin):
        a = n * (-gmin) / (gmax - gmin)
        c = (a - i) / a * blue_div + i / a * blue
    elif i < n * (1 - gmin) / (gmax - gmin):
        a = n * (1 - gmin) / (gmax - gmin)
        b = n * (-gmin) / (gmax - gmin)
        c = (a - i) / (a - b) * blue + (i - b) / (a - b) * red
    else:
        a = n
        b = n * (1 - gmin) / (gmax - gmin)
        c = (a - i) / (a - b) * red + (i - b) / (a - b) * red_div
    return c[0], c[1], c[2]


L = []
for t in np.linspace(-1, 2, n):
    L.append(color(t))

cm = LinearSegmentedColormap.from_list(
    'cmap', L, N=n)

res = 15
R_tm = np.zeros((res, res))
R_tf = np.zeros((res, res))
R_sd = np.zeros((res, res))

thisdir = 'results/fig_A5'

for r, d, f in os.walk(thisdir):  # r=root, d=directories, f = files
    for file in f:
        if file != '.DS_Store':
            f = file.split("_")
            X = np.load(thisdir + '/' + f[0] + '_' + f[1][:-4] + '.npy')
            R_tm[int(f[0]), int(f[1][:-4])] = X[0]
            R_tf[int(f[0]), int(f[1][:-4])] = X[1]
            R_sd[int(f[0]), int(f[1][:-4])] = np.abs(X[0] - X[1])

eps = 0.01
fig, ax = plt.subplots(1)
plt.imshow(R_tm.T, extent=[0, 20, 0, 0.1], aspect=20 / 0.1, origin='lower', cmap=cm, vmin=-1,
           vmax=2)  # , interpolation='bicubic')
plt.colorbar()
# plt.title(r'$\overline{t}_m$')
plt.xlabel(r'$N$')
plt.ylabel(r'$\lambda$')
plt.xticks([0, 10, 20])
plt.yticks([0, 0.05, 0.1])
# ax.axhline(0.1, 0, 1, color='yellow', linestyle='--')
plt.tight_layout()

fig, ax = plt.subplots(1)
plt.imshow(R_tf.T, extent=[0, 20, 0, 0.1], aspect=20 / 0.1, origin='lower', cmap=cm, vmin=-1,
           vmax=2)  # , interpolation='bicubic')
plt.colorbar()
# plt.title(r'$\overline{t}_f$')
plt.xlabel(r'$N$')
plt.ylabel(r'$\lambda$')
plt.xticks([0, 10, 20])
plt.yticks([0, 0.05, 0.1])
# ax.axhline(0.1, 0, 1, color='yellow', linestyle='--')
plt.tight_layout()

SMALL_SIZE = 8
MEDIUM_SIZE = 12
BIGGER_SIZE = 17

plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

# cmap = plt.get_cmap()
# bounds=np.linspace(np.min(R_sd), np.max(R_sd), 25)
# norm = colors.BoundaryNorm(bounds, cmap.N)

fig, ax = plt.subplots(1)
plt.imshow(R_sd.T, extent=[0, 20, 0, 0.1], aspect=20 / 0.1, origin='lower')  # , interpolation='bicubic')
plt.colorbar()
pas = 20 / res
x = np.linspace(0 + pas, 20 - pas, res)
pas = 0.1 / res
y = np.linspace(0 + pas, 0.1 - pas, res)
X, Y = np.meshgrid(x, y)
Z = R_sd.T
CS = ax.contour(x, y, Z, levels=[1.025, 1.05, 1.06, 1.07, 1.08], colors='tab:red')
ax.clabel(CS, inline=True, fontsize=10)
# plt.title('female-limited mimicry caused by RI')
plt.xlabel(r'$N$')
plt.ylabel(r'$\lambda$')
# ax.axhline(0.1, 0, 1, color='yellow', linestyle='--')
plt.tight_layout()
