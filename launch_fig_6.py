import os

from functions import *

eps = 0.01

res = 250
pas = 1 / res
L_ta = np.linspace(1 - pas, 0 + pas, res)
pas = 1 / res
L_a = np.linspace(0 + pas, 10 - pas, res)

for i, ta in enumerate(L_ta):
    for j, a in enumerate(L_a):
        if i > 75 and os.path.isfile('results/fig_6/' + str(i) + '_' + str(j) + '.npy') == False:
            print('ta', ta, 'a', a, flush=True)
            X = tm_tf_pf(c, a, b, l, lp, N, Np, d, d, cri, s, ta, tp, cor)
            np.save('results/fig_6/' + str(i) + '_' + str(j), X)
