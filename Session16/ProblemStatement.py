#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Blood glucose levels for obese patients have a mean of 100 with a standard deviation of 15. 
A researcher thinks that a diet high in raw cornstarch will have a positive effect on blood glucose levels. 
A sample of 36 patients who have tried the raw cornstarch diet have a mean glucose level of 108. 
Test the hypothesis that the raw cornstarch had an effect or not.

1. In one state, 52% of the voters are Republicans, and 48% are Democrats. 
In a second state, 47% of the voters are Republicans, and 53% are Democrats.
Suppose a simple random sample of 100 voters are surveyed from each state.
What is the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state?

2. You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard deviation is 209. 
How well did you score on the test compared to the average test taker?
"""
import scipy.stats as st

print("Let H0: μ= 100,  Stating the hypothesis. Given, The population mean is 100.")
print("Let H1: μ > 100 ")

significance_level = 0.05 # It is not given in the problem so let’s assume it as 5% (0.05).
m = 100 # Blood glucose levels for obese patients have a mean of 100. 
s = 15 # Standard deviation of 15
p = 36 # A sample of 36 patients
x = 108 # Patients who have tried the raw cornstarch diet have a mean glucose level of 108.
Z = (x-m) / (s/(p**0.5)) # Z-Score for this set of data
p_value = st.norm.cdf(Z) # By looking at z- table, Probability of having value less than 108.
p_value_comp = 1-p_value # Probability of having value more than or equals to 108.

print("Probability of having value less than 108 is : ",p_value)
print("Probability of having value more than or equals to 108 is: ",p_value_comp)
print()

if(p_value_comp < significance_level ):
    print("Probability of having value more than or equals to 108 is less than " + str(significance_level) + " so we will reject the Null hypothesis. There is raw cornstarch effect.")
else:
    print("Probability of having value less than 108 is not less than " + str(significance_level) + " so we will not reject the Null hypothesis. There is no raw cornstarch effect.")
print("\n", "="*50, "\n", sep="")

'''
1. In one state, 52% of the voters are Republicans, and 48% are Democrats. 
In a second state, 47% of the voters are Republicans, and 53% are Democrats.
Suppose a simple random sample of 100 voters are surveyed from each state.
What is the probability that the survey will show a greater percentage of Republican voters in the second state than in the first state?
'''

P1 = 0.52
P2 = 0.47
print("The proportion of Republican voters in the first state ( 52% ): P1  =", P1)
print("The proportion of Republican voters in the second state ( 47% ): P2 =", P2) 
print()

n1 = 100
n2 = 100
print("The number of voters sampled from the first state: n1 =", n1)
print("The number of voters sampled from the second state: n2 =", n2)
print()

md = P1-P2
print("The mean of the difference in sample proportions: E(p1-p2) = P1-P2 =", round(md,2))
print()

sd = ((P1*(1-P1)/n1) + (P2*(1-P2)/n2))**0.5
print("The standard deviation of the difference, σd = sqrt{[P1(1-P1)/n1] + [P2(1-P2)/n2]}, σd =", sd)
print()

print("We need to find if the probability p1 - p2 is less than zero. To find this probability, we need to transform the random variable (p1 - p2) into a z-score.")
print()

Z =  (0-md)/sd #Finding Z-Score, z(p1-p2) using mean difference and calculated standard deviation
print("Z-Score using mean difference and calculated standard deviation:", Z)
print()

p_value = st.norm.cdf(Z)
print("The probability that the survey will show a greater percentage of Republican voters in the second state than in the first state is:", round(p_value, 2))
print("\n", "="*50, "\n", sep="")

'''
2. You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard deviation is 209. 
How well did you score on the test compared to the average test taker?
'''
m = 1026 # The mean score for the SAT is 1026.
s = 209 # The standard deviation is 209.
x = 1100 # You take the SAT and score 1100.
Z = (x-m)/s # Calculating Z - Score

p_value = st.norm.cdf(Z) #The probability of given z-score
print("I have scored higher than", str(p_value*100), "% of test takers.")
print("\n", "="*50, "\n", sep="")