#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two balls are drawn at random in succession without replacement from an urn containing 4 red balls and 6 black balls.

Find the probabilities of all the possible outcomes.
"""
from scipy import stats

total_num_of_balls = 10
total_red_balls = 4
total_black_balls = 6

# Possible outcomes could be (R,R), (R,B), (B,R), (B,B)
R_R = (total_red_balls/total_num_of_balls) * (total_red_balls-1)/(total_num_of_balls-1)
R_B = (total_red_balls/total_num_of_balls) * (total_black_balls)/(total_num_of_balls-1)
B_R = (total_black_balls/total_num_of_balls) * (total_red_balls)/(total_num_of_balls-1)
B_B = (total_black_balls/total_num_of_balls) * (total_black_balls-1)/(total_num_of_balls-1)

print("The probability of (R,R) is", round(R_R, 2))
print("The probability of (R,B) is", round(R_B, 2))
print("The probability of (B,R) is", round(B_R, 2))
print("The probability of (B,B) is", round(B_B, 2))