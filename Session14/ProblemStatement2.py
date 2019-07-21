#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A die marked A to E is rolled 50 times. Find the probability of getting a “D” exactly 5 times.
"""
from scipy import stats

total_num_of_rolls = 50
p_D = 1/5
probability = stats.binom.pmf(5, total_num_of_rolls, p_D)

print("The probability of getting a “D” exactly 5 times is", probability)