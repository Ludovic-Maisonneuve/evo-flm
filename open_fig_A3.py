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

res = 5
L_cor = np.linspace(0, 1, res)

for j, cor in enumerate(L_cor):

    C = 0.01
    Gtmtf = cor * np.sqrt(C * C)

    L_tm = np.load('results/fig_A3/L_tm_' + str(cor) + '.npy')
    L_tf = np.load('results/fig_A3/L_tf_' + str(cor) + '.npy')
    L_pf = np.load('results/fig_A3/L_pf_' + str(cor) + '.npy')

    fig, ax = plt.subplots()
    plt.plot(L_tm, label=r'$\overline{t}_m^*$', color=yellow, alpha=1)
    plt.plot(L_tf, label=r'$\overline{t}_f^*$', color=purple, alpha=1)
    plt.plot(L_pf, label=r'$\overline{p}_f^*$', color=purple, linestyle=(0, (3, 4)), alpha=1)
    if j == 0:
        xmin, xmax = plt.xlim()
    plt.xticks([0, 50000, 100000])
    plt.legend()
    plt.xlabel('generation')
    plt.xlim(xmin, xmax)
    ax.hlines(0, xmin, xmax, color=blue, linestyles='dashed')
    ax.hlines(1, xmin, xmax, color=red, linestyles='dashed')
    ymin, ymax = plt.ylim()
    plt.ylim(ymin, ymax)
    plt.title(r'$G_{t_mt_f}=$' + str(Gtmtf / 0.01) + r'$\sqrt{G_{t_mt_m}G_{t_ft_f}}$')
    if j == 4:
        plt.title(r'$G_{t_mt_f}=\sqrt{G_{t_mt_m}G_{t_ft_f}}$')
    if j == 0:
        plt.title(r'$G_{t_mt_f}=0$')
    plt.tight_layout()
