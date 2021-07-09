import os

from functions import *

eps = 0.01

res = 25
pas = 10 * eps / res
L_cri = np.linspace(0 + pas, 10 * eps - pas, res)
pas = 1 / res
L_c = np.linspace(0 + pas, 1 - pas, res)

for i, cri in enumerate(L_cri):
    for j, c in enumerate(L_c):
        if os.path.isfile('results/fig_A1/' + str(i) + '_' + str(j) + '.npy') == False:
            print('cri', cri, 'c', c, flush=True)
            X = tm_tf_pf(c, a, b, l, lp, N, Np, d, d, cri, s, ta, tp, cor)
            np.save('results/fig_A1/' + str(i) + '_' + str(j), X)
