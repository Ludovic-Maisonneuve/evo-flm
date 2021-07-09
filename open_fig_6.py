import os

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

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

res = 250
R_tm = np.zeros((res, res))
R_tf = np.zeros((res, res))
R_pf = np.zeros((res, res))
R_sd = np.zeros((res, res))

pas = 1 / res
L_tp = np.linspace(0 + pas, 1 - pas, res)

thisdir = 'results/fig_6'
for r, d, f in os.walk(thisdir):  # r=root, d=directories, f = files
    for file in f:
        if file != '.DS_Store':
            f = file.split("_")
            X = np.load(thisdir + '/' + f[0] + '_' + f[1][:-4] + '.npy')
            R_tm[int(f[0]), int(f[1][:-4])] = X[0] + (1 - L_tp[int(f[0])])
            R_tf[int(f[0]), int(f[1][:-4])] = X[1] + (1 - L_tp[int(f[0])])
            R_pf[int(f[0]), int(f[1][:-4])] = X[2] + (1 - L_tp[int(f[0])])
            R_sd[int(f[0]), int(f[1][:-4])] = np.abs(X[0]) - np.abs(X[1])

eps = 0.01

max = np.max(R_sd)
min = np.min(R_sd)
vmax = np.abs(np.max([max, min]))

purple = np.array([0.32, 0.106, 0.575])
black = np.array([0.05, 0.05, 0.05])
yellow = np.array([0.948, 0.83, 0.148])
gmin = -1
gmax = 2
n = 100

k = 0.3


def color(t):
    if t < 0:
        c = ((vmax + t) / vmax) ** k * black + (-t / vmax) ** k * purple
    else:
        c = ((vmax - t) / vmax) ** k * black + (t / vmax) ** k * yellow
    return c[0], c[1], c[2]


L = []
for t in np.linspace(-vmax, vmax, n):
    L.append(color(t))

cm = LinearSegmentedColormap.from_list(
    'cmap', L, N=n)

fig, ax = plt.subplots(1)
plt.imshow(R_sd.T, extent=[0, 1, 0, 10], aspect=1 / 10, origin='lower', cmap=cm, vmax=vmax,
           vmin=-vmax)  # , interpolation='bicubic')
plt.colorbar()
plt.xlabel(r"$|t'-t_a|$")
plt.ylabel(r'$a$')
plt.tight_layout()

blue_div = np.array([61 / 255, 139 / 255, 240 / 255])
blue = np.array([67 / 255, 114 / 255, 189 / 255])
red = np.array([159 / 255, 58 / 255, 65 / 255])
red_div = np.array([240 / 255, 58 / 255, 65 / 255])
gmin = -1
gmax = 2
n = 50

k = 1


def color(t):
    i = int(n * (t + 1) / 3)
    if t == float('inf'):
        c = np.array([0 / 255, 0 / 255, 0 / 255])
    elif i < n * (-gmin) / (gmax - gmin):
        a = n * (-gmin) / (gmax - gmin)
        c = ((a - i) / a) ** k * blue_div + (i / a) ** k * blue
    elif i < n * (1 - gmin) / (gmax - gmin):
        a = n * (1 - gmin) / (gmax - gmin)
        b = n * (-gmin) / (gmax - gmin)
        c = ((a - i) / (a - b)) ** k * blue + ((i - b) / (a - b)) ** k * red
    else:
        a = n
        b = n * (1 - gmin) / (gmax - gmin)
        c = ((a - i) / (a - b)) ** k * red + ((i - b) / (a - b)) ** k * red_div
    return c[0], c[1], c[2]


L = []
for t in np.linspace(-1, 2, n):
    L.append(color(t))

cm = LinearSegmentedColormap.from_list(
    'cmap', L, N=n)

SMALL_SIZE = 16
MEDIUM_SIZE = 22
BIGGER_SIZE = 27

plt.rc('font', size=SMALL_SIZE)  # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)  # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)  # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)  # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)  # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

eps = 0.01
fig, ax = plt.subplots(1)
plt.imshow(R_tm.T, extent=[0, 1, 0, 10], aspect=1 / 10, origin='lower', cmap=cm, vmin=-1,
           vmax=2)  # , interpolation='bicubic')
cbar = plt.colorbar()
plt.xlabel(r"$|t'-t_a|$")
plt.ylabel(r'$a$')
plt.xticks([0, 0.5, 1])
plt.yticks([0, 5, 10])
pas = 1 / res
x = np.linspace(0 + pas, 1 - pas, res)
pas = 10 / res
y = np.linspace(0 + pas, 10 - pas, res)
# X, Y = np.meshgrid(x, y)
Z = R_tm.T
CS = ax.contour(x, y, Z, levels=[0, 0.4, 0.45, 0.5], colors='yellow')
ax.clabel(CS, inline=True, fontsize=15)
plt.tight_layout()

fig, ax = plt.subplots(1)
plt.imshow(R_tf.T, extent=[0, 1, 0, 10], aspect=1 / 10, origin='lower', cmap=cm, vmin=-1,
           vmax=2)  # , interpolation='bicubic')
cbar = plt.colorbar()
plt.xlabel(r"$|t'-t_a|$")
plt.ylabel(r'$a$')
plt.xticks([0, 0.5, 1])
plt.yticks([0, 5, 10])
pas = 1 / res
x = np.linspace(0 + pas, 1 - pas, res)
pas = 10 / res
y = np.linspace(0 + pas, 10 - pas, res)
# X, Y = np.meshgrid(x, y)
Z = R_tf.T
CS = ax.contour(x, y, Z, levels=[0, 0.95, 0.96, 0.97, 0.98, 0.99, 1], colors='yellow')
ax.clabel(CS, inline=True, fontsize=15)
plt.tight_layout()

fig, ax = plt.subplots(1)
plt.imshow(R_pf.T, extent=[0, 1, 0, 10], aspect=1 / 10, origin='lower', cmap=cm, vmin=-1,
           vmax=2)  # , interpolation='bicubic')
cbar = plt.colorbar()
cbar.ax.set_ylabel(r'$\overline{p}_f^*$')
plt.xlabel(r"$|t'-t_a|$")
plt.ylabel(r'$a$')
plt.tight_layout()
