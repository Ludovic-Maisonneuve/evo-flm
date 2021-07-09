import os

from functions import *

eps = 0.01
cri = 5 * eps
res = 5
L_cor = np.linspace(0, 1, res)
dm = d
df = d

for j, cor in enumerate(L_cor):
    print('cor', cor, flush=True)


    def b_pred(t, tm, tf, pf):
        D = 1 + l * N / 2 * (np.exp(-b * (t - tf) ** 2) + np.exp(-b * (t - tm) ** 2)) + lp * Np * np.exp(
            -b * (t - tp) ** 2)

        Num = (l * N / 2 * (-2 * b * (t - tf) * np.exp(-b * (t - tf) ** 2) - 2 * b * (t - tm) * np.exp(
            -b * (t - tm) ** 2)) - 2 * b * (t - tp) * lp * Np * np.exp(-b * (t - tp) ** 2))
        return Num / D ** 2


    def beta_pred(tm, tf, pf):
        return np.array([dm * b_pred(tm, tm, tf, pf), df * b_pred(tf, tm, tf, pf), 0])


    def beta_repro(tm, tf, pf):
        D = (1 - c) * (2 * a * (pf - tm) * N * np.exp(-a * (pf - tm) ** 2) + 2 * a * (pf - tp) * Np * cri * np.exp(
            -a * (pf - tp) ** 2))
        Num = c * (N + Np) + (1 - c) * (N * np.exp(-a * (pf - tm) ** 2) + Np * cri * np.exp(-a * (pf - tp) ** 2))
        return np.array([-2 * a * (tm - pf), 0, -2 * a * (pf - tm) + D / Num])


    def beta_dev(tm, tf, pf):
        return np.array([-2 * s * (tm - ta), -2 * s * (tf - ta), 0])


    def beta_ns(tm, tf, pf):
        return beta_pred(tm, tf, pf) + beta_dev(tm, tf, pf)


    X0 = np.array([ta, ta, ta])
    X = X0
    C = 0.01
    Gtmtf = cor * np.sqrt(C * C)
    Gtmpf = a * C * C
    Gtfpf = Gtmtf * Gtmpf / C
    G = np.array([[C, Gtmtf, Gtmpf], [Gtmtf, C, Gtfpf], [Gtmpf, Gtfpf, C]])
    dX = np.array([1, 1, 1])
    i = 0

    L_tm = [ta]
    L_tf = [ta]
    L_pf = [ta]

    while np.sqrt(dX[0] ** 2 + dX[1] ** 2 + dX[2] ** 2) / 3 > 0.01 ** 2 * 0.0001 and (
            X[0] ** 2 + X[1] ** 2 + X[2] ** 2) / 3 < 1000 and i < 1000000:
        i += 1
        dd = np.array([0, 0, 0])
        dX = 1 / 2 * np.dot(G, beta_ns(X[0], X[1], X[2]) + beta_repro(X[0], X[1], X[2]))
        X = X + dX
        L_tm.append(X[0])
        L_tf.append(X[1])
        L_pf.append(X[2])

    np.save('results/fig_A4/L_tm_' + str(cor), L_tm)
    np.save('results/fig_A4/L_tf_' + str(cor), L_tf)
    np.save('results/fig_A4/L_pf_' + str(cor), L_pf)
