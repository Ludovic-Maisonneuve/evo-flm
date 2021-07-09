import os

from functions import *

eps = 0.01

a = 0
cri = 0
s = 1 * eps
dm = d / 5

res = 250
pas = 20 / res
L_N = np.linspace(0 + pas, 20 - pas, res)
pas = 0.1 / res
L_l = np.linspace(0 + pas, 0.1 - pas, res)

for i, N in enumerate(L_N):
    for j, l in enumerate(L_l):
        if i > 200 and os.path.isfile('results/fig_7/' + str(i) + '_' + str(j) + '.npy') == False:
            print('N', N, 'l', l, flush=True)
            X = tm_tf_pf(c, a, b, l, lp, N, Np, dm, d, cri, s, ta, tp, cor)
            np.save('results/fig_7/' + str(i) + '_' + str(j), X)
