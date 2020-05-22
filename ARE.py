import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

def calc(T):
    for i in range(0, len(T) - 1):
        S.append(S[i] - r * b * S[i] * I[i] / N - r2 * b2 * S[i] * E[i] / N)
        E.append(E[i] + r * b * S[i] * I[i] / N - a * E[i] + r2 * b2 * S[i] * E[i] / N)
        I.append(I[i] + a * E[i] - y * I[i])
        R.append(R[i] + y * I[i])

def plot(T,S,E,I,R):
    plt.figure()
    plt.title("SEIR-le courbe de la transmission du virus par le temps")
    plt.plot(T,S,color='r',label='sensible')
    plt.plot(T, E, color='k', label='non infectieux')
    plt.plot(T, I, color='b', label='Infectées')
    plt.plot(T, R, color='g', label='retirées')
    plt.grid(False)
    plt.legend()
    plt.xlabel("temps(jours)")
    plt.ylabel("personne")
    plt.show()

if __name__ == '__main__':
    
    N = 10000  # population
    E = []  # non infectieux
    E.append(0)

    I = []  # Infectées
    I.append(1)

    S = []  # sensible
    S.append(N - I[0])

    R = []  # retirées
    R.append(0)

    r = 3  # le nombre de perconne contactent avec un infectieux
    b = 0.03  # Probabilité d'infection par infectée
    a = 0.1  # Probabilité de morbidité non infectieux
    r2 = 3  # le nombre de perconne contactent avec un non infectieux
    b2 = 0.03  # Probabilité d'infection par non infectious
    y = 0.1  # Probabilité de récupération

    T = [i for i in range(0, 160)]  # temps(
    calc(T)
    plot(T,S,E,I,R)

