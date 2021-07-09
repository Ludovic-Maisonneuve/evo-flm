from functions import *

cri = 0 * eps
a = 0
s = 1 * eps
res = 250
L_r = np.linspace(0, 1, res)

L_tm = []
L_tf = []
L_pf = []

for r in L_r:
    print(r, flush=True)
    tm, tf, pf = tm_tf_pf(c, a, b, l, lp, N, Np, r * d, d, cri, s, ta, tp, cor)
    print(tm, tf, flush=True)
    L_tm.append(tm)
    L_tf.append(tf)
    L_pf.append(pf)
    np.save('results/fig_5_a/L_tm', L_tm)
    np.save('results/fig_5_a/L_tf', L_tf)
    np.save('results/fig_5_a/L_pf', L_pf)

# a = 10
#
# L_tm = []
# L_tf = []
# L_pf = []
#
# for cri in L_cri:
#     print(cri, flush=True)
#     tm, tf, pf = tm_tf_pf(c, a, b, l, lp, N, Np, d, d, cri, s, to, tp, cor)
#     print(tm, tf, flush=True)
#     L_tm.append(tm)
#     L_tf.append(tf)
#     L_pf.append(pf)
#     np.save('results/fig_4_a/bis/L_tm', L_tm)
#     np.save('results/fig_4_a/bis/L_tf', L_tf)
#     np.save('results/fig_4_a/bis/L_pf', L_pf)
