#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A test is conducted which is consisting of 20 MCQs (multiple choices questions) with every MCQ having its four options out of which only one is correct.

Determine the probability that a person undertaking that test has answered exactly 5 questions wrong.
"""
from scipy import stats

total_num_of_question = 20
p_wrong_answer = 3/4
probability = stats.binom.pmf(5, total_num_of_question, p_wrong_answer)

print("The probability that a person undertaking that test has answered exactly 5 questions wrong is", probability)