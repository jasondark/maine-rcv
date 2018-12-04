#!/usr/bin/env python3

from collections import defaultdict

with open('data/04-reduced/tabulate.txt') as f:
    votes = [(t[1], int(t[0])) for vote in f.readlines() for t in [vote.split()]]


eliminated = set()

rcv_round = 0
while True:
    rcv_round += 1
    print("computing round {}".format(rcv_round))
    candidates = defaultdict(int)
    for j, (vote, i) in enumerate(votes):
        # skip over uninformative votes
        while len(vote) > 0 and vote[0] in eliminated:
            vote = vote[1:]

        # update the vote
        votes[j] = (vote, i)

        # if vote is not exhausted, count it
        if len(vote) > 0:
            candidates[vote[0]] += i

    print({c: v for c, v in candidates.items()})

    total = sum(candidates.values())
    strongest = max(candidates.items(), key=lambda pair: pair[1])
    weakest = min(candidates.items(), key=lambda pair: pair[1])

    if 2 * strongest[1] > total:
        print("majority threshold met, winner is {}".format(strongest[0]))
        break
    else:
        print("eliminating {}".format(weakest[0]))
        eliminated.add(weakest[0])

