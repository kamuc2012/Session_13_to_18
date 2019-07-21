#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A die marked A to E is rolled 50 times. Find the probability of getting a “D” exactly 5 times.
"""
from scipy import stats

n = 50
p = 0.2
probability = stats.binom.pmf(5, n, p)

print("The probability of getting a “D” exactly 5 times is", probability)