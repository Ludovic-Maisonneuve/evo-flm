from functions import *

res = 250
L_cri = np.linspace(0, 10 * eps, res)

a = 10

L_tm = []
L_tf = []
L_pf = []

for cri in L_cri:
    print(cri, flush=True)
    tm, tf, pf = tm_tf_pf(c, a, b, l, lp, N, Np, d, d, cri, s, ta, tp, cor)
    print(tm, tf, flush=True)
    L_tm.append(tm)
    L_tf.append(tf)
    L_pf.append(pf)
    np.save('results/fig_4_a/L_tm', L_tm)
    np.save('results/fig_4_a/L_tf', L_tf)
    np.save('results/fig_4_a/L_pf', L_pf)
