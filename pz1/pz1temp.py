import numpy as np
from scipy.special import spherical_jn, spherical_yn

def hankel_three_kind(n, k, r):
    return spherical_jn(n, k * r) + 1j * spherical_yn(n, k * r)

def an(n, k, r):
    return spherical_jn(n, k * r) / hankel_three_kind(n, k, r)

def bn(n, k, r):
    return ((k * r * spherical_jn(n - 1, k * r) - n * spherical_jn(n, k * r)) /
            (k * r * hankel_three_kind(n - 1, k, r) - n * hankel_three_kind(n, k, r)))


def sigma(lamb, k, r):
    s = 0
    for n in range(1, 200 + 1):
        s += (-1)**n * (n + 0.5) * (bn(n, k, r) - an(n, k, r))
    return (lamb**2 / np.pi) * abs(s)**2



lamb = 'c/hz'
k = 2 * np.pi / lamb
fmin = 0.01e9
fmax = 40000000000
D = 0.01

sigma = ''
an = '' 
bn = ''
hn = ''

if __name__ == '__main__':
    with open('task_rcs_01.csv', encoding='utf-8') as file:
        file.readline()
        variant, fmin, fmax, D = map(float, file.readline().split(','))
