import os

from functions import *

res = 25
pas = 5 * eps / res
L_cri = np.linspace(0 + pas, 2 * eps - pas, res)
pas = 0.1 / res
L_l = np.linspace(0 + pas, 0.1 - pas, res)

for i, cri in enumerate(L_cri):
    for j, l in enumerate(L_l):
        if os.path.isfile('results/fig_3_50/' + str(i) + '_' + str(j) + '.npy') == False:
            print('cri', cri, 'l', l, flush=True)
            X = tm_tf_pf(c, a, b, l, lp, N, Np, d, d, cri, s, ta, tp, cor)
            np.save('results/fig_3_50/' + str(i) + '_' + str(j), X)
