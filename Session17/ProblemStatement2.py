#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the following data, perform a one-way analysis of variance using α=.05.

Write up the results in APA format.

[Group1: 51, 45, 33, 45, 67]
[Group2: 23, 43, 23, 43, 45]
[Group3: 56, 76, 74, 87, 56]
"""
import scipy.stats as st
import statistics as sts

print("\nLet, Null Hypothesis H0: μ1 = μ2 = μ3 ")
print("\nLet, Alternate Hypothesis Ha: μ1 ≠ μ2 ≠ μ3 ") 

print("\nGiven, \n[Group1: 51, 45, 33, 45, 67]")
print("\n[Group2: 23, 43, 23, 43, 45]")
print("\n[Group3: 56, 76, 74, 87, 56]")
    
group_1 = [51, 45, 33, 45, 67] #Given, [Group1: 51, 45, 33, 45, 67]
group_2 = [23, 43, 23, 43, 45] #Given, [Group2: 23, 43, 23, 43, 45]
group_3 = [56, 76, 74, 87, 56] #Given, [Group3: 56, 76, 74, 87, 56]

n = len(group_1) + len(group_2) + len(group_3) #Count of all the availabale data 
k = 3 #Given three group of samples
significance_level = 0.05 #Given, using α=.05

group_1_mean = sts.mean(group_1) #Mean value of Group1
group_2_mean = sts.mean(group_2) #Mean value of Group2
group_3_mean = sts.mean(group_3) #Mean value of Group3
total_mean = sts.mean(group_1 + group_2 + group_3) ##Mean value of all the given groups

dof_between = k-1 #Degree of freedom between
print("\nDegree of freedom between (dof_between):",dof_between)

dof_within= n-k #Degree of freedom within
print("\nDegree of freedom within (dof_within):",dof_within)

group_size = len(group_1) #From given group

#Sum of Squares Between
ss_between = (((group_1_mean-total_mean)**2) + ((group_2_mean-total_mean)**2) + ((group_3_mean-total_mean)**2)) * group_size
print("\nSum of Squares Between (ss_between):",ss_between)

ms_between = ss_between/dof_between #Mean Square Between
print("\nMean Square Between (ms_between = ss_between/dof_between):",ms_between)

def calc_sum_of_square(sequence, mean): #Calculates sum of squares for given sequence and mean.
    sum_val = 0
    for val in sequence:
        sum_val += ((val-mean)**2)
    return sum_val

#Sum of Squares Within
ss_within = calc_sum_of_square(group_1, group_1_mean) + calc_sum_of_square(group_2, group_2_mean) + calc_sum_of_square(group_3, group_3_mean)
print("\nSum of Squares Within (ss_within):",ss_within)

ms_within = ss_within/dof_within #Mean Square Within
print("\nMean Square Within (ms_within = ss_within/dof_within):",ms_within)

F_Calc = ms_between/ms_within #F-Satistic
print("\nF-Calculated (ms_between/ms_within):",F_Calc)

#Calculating F-Critical using given significance level and degree of freedom
F_Critical = st.f.ppf(q=1-significance_level, dfn=dof_between, dfd=dof_within) 
print("\nF-Critical:",F_Critical)

print("\nIf the critical value of F from tables is less than the calculated value of F, reject the null hypothesis")
if F_Critical < F_Calc:
    print("\nReject Null Hypothesis H0 and conclude that at least two of the means are significantly different from each other.")
else:
    print("\nNull Hypothesis H0 can not be rejected and conclude that all the means are equal.")