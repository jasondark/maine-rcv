#!/usr/bin/env python3

from collections import defaultdict
import numpy as np
import numpy.linalg as linalg

candidates = set('BGHP')
pairs = defaultdict(int)

with open('data/04-reduced/tabulate.txt') as f:
    for line in f.readlines():
        nstr, ranking = line.split()
        n = int(nstr)
        unranked = candidates - set(ranking)

        for i in range(0, len(ranking)):

            # ranking[i] > ranking[j]
            for j in range(i+1, len(ranking)):
                pairs[(ranking[i], ranking[j])] += n

            # any specified candidate > any unspecified candidate
            for c in unranked:
                pairs[(ranking[i], c)] += n

tally = []
for a in 'BGHP':
    for b in 'BGHP':
        if b <= a:
            continue

        m, n = pairs[(a, b)], pairs[(b, a)]

        if m > n:
            tally.append((a, b, m-n))
        else:
            tally.append((b, a, n-m))

tally.sort(key=lambda x: -x[2])
print('Ranked Pairs:')
print('\n'.join('{}\t{}\t{}'.format(a, b, i) for a, b, i in tally))



A = np.zeros((4, 4))
for i, a in enumerate('BGHP'):
    for j, b in enumerate('BGHP'):
        if i == j:
            continue
        # A[i,j] = rate at which j->i = number of i>j
        A[i, j] = pairs[(a, b)]
A -= np.diag(A.sum(axis=0))


print('\nContinuous Time Markov Chain')
w, v = linalg.eig(A)
r = v[:,0] / v[:,0].sum()
ranking = []
for a, b in zip('BGHP', r):
    ranking.append((a, b))
ranking.sort(key=lambda x: -x[1])
print('\n'.join('{}\t{}'.format(a, b) for a, b in ranking))

print('\nDiscrete Time Markov Chain')
q = -A.diagonal(0) * r
q /= q.sum()
ranking = []
for a, b in zip('BGHP', q):
    ranking.append((a, b))
ranking.sort(key=lambda x: -x[1])
print('\n'.join('{}\t{}'.format(a, b) for a, b in ranking))

B = np.eye(4)
for i, a in enumerate('BGHP'):
    for j, b in enumerate('BGHP'):
        if i == j:
            continue
        B[i, j] = pairs[(a, b)] / pairs[(b, a)]

print('\nAnalytic Hierarchy Process')
w, v = linalg.eig(B)
s = np.real(v[:,0] / v[:,0].sum())
ranking = []
for a, b in zip('BGHP', s):
    ranking.append((a, b))
ranking.sort(key=lambda x: -x[1])
print('\n'.join('{}\t{}'.format(a, b) for a, b in ranking))



