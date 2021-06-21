# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 18:13:17 2021

@author: vavilse1
"""

from bots import *
from itertools import combinations
from random import randint

payout = {("C", "C"): (2, 2), ("C", "N"): (-1, 3), ("N", "C"): (3, -1), ("N", "N"): (0, 0)}

def match(bot1, bot2):
    bot1.__init__()
    bot2.__init__()
    score1 = 0
    score2 = 0
    for _ in range(randint(5,10)):
        resp1 = bot1.move()
        resp2 = bot2.move()
        bot1.append_history(resp2)
        bot2.append_history(resp1)
        dscores = payout[(resp1, resp2)]
        score1 += dscores[0]
        score2 += dscores[1]
    return (score1, score2)

def statistics(bots_list):
    scores = {bot: 0 for bot in bots_list}
    for _ in range(10):
        for pair in combinations(bots_list, 2):
            dscores = match(pair[0], pair[1])
            scores[pair[0]] += dscores[0]
            scores[pair[1]] += dscores[1]
    return scores

def print_statistics(bots_list):
    scores = statistics(bots_list)
    for k, v in sorted(scores.items(), key = lambda item: item[1], reverse = True):
        print(v, k.__class__.__name__, sep = "\t")