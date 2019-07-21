#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate F Test for given 10, 20, 30, 40, 50 and 5, 10, 15, 20, 25.

For 10, 20, 30, 40, 50:
"""
import scipy.stats as st
import statistics as sts

print("Let, Null Hypothesis H0: No difference in variances.") #Null Hypothesis, Ho: No difference in variances.
print("Let, Alternate Hypothesis Ha: Difference in variances.\n") #Alternate Hypothesis, Ha: Difference in variances.

lst_1 = [ 10, 20, 30, 40, 50] #Given data
print("Given first data set:",lst_1)

lst_2 = [ 5, 10, 15, 20, 25] #Given data
print("Given second data set:",lst_2)

var_1 = sts.variance(lst_1) #Variance of 10, 20, 30, 40, 50
print("\nVariance of 10, 20, 30, 40, 50 is (var_1):",var_1)

var_2 = sts.variance(lst_2) #Variance of 5, 10, 15, 20, 25
print("Variance of 5, 10, 15, 20, 25 is (var_2):", var_2)

F_Test = var_1/var_2 #F Test = (variance of 10, 20, 30, 40, 50) / (variance of 5, 10, 15, 20, 25) 
print("\nF-Test value of the given data sets (var_1/var_2):",F_Test)

dof_lst_1 = len(lst_1)-1 #Degrees of freedom 10, 20, 30, 40, 50
print("\nDegree of freedom of 10, 20, 30, 40, 50 is:",dof_lst_1)

dof_lst_2 = len(lst_2)-1 #Degrees of freedom 5, 10, 15, 20, 25
print("\nDegree of freedom of 5, 10, 15, 20, 25 is:",dof_lst_2)

significance_level = 0.05 #If not given, default alpha value = 0.05

F_Critical = st.f.ppf(q=1-significance_level, dfn=dof_lst_1, dfd=dof_lst_2) # F-Table value using default alpha value = 0.05 and calculated degree of freedom
print("\nF-Critical value using default alpha (value = 0.05) is: "+str(F_Critical))

#If the F-Table value is smaller than the calculated value, you can reject the null hypothesis.
print("\nIf the F-Crtitical value is smaller than the calculated value, we can reject the null hypothesis.")

if F_Critical < F_Test:
    print("\nNull hypothesis can be rejected.")
else:
    print("\nNull hypothesis can not be rejected.")