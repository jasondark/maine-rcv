#!/usr/bin/env python3

from collections import defaultdict
import re

print("parsing votes")
# two or more consecutive undervotes (blanks), or any overvote, immediately exhausts ballot
with open('data/03-coded/votes.dat') as f:
    votes = [re.sub(r"(UU|O).*", "", vote.strip()) for vote in f.readlines()]

# undervotes immediately "forward" to next selection
eliminated = {'U'}

rcv_round = 0
while True:
    rcv_round += 1
    print("computing round {}".format(rcv_round))
    candidates = defaultdict(int)
    for i, vote in enumerate(votes):
        # skip over uninformative votes
        while len(vote) > 0 and vote[0] in eliminated:
            vote = vote[1:]

        # update the vote
        votes[i] = vote

        # if vote is not exhausted, count it
        if len(vote) > 0:
            candidates[vote[0]] += 1

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

