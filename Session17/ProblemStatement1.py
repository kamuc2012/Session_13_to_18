#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Is gender independent of education level? A random sample of 395 people were surveyed and each person was asked to report the highest education level they obtained.

The data that resulted from the survey is summarized in the following table:

        High-School     Bachelor    Masters     Ph.D.   Total
Female  60              54          46          41      201
Male    40              44          53          57      194
Total   100             98          99          98      395

Question: Are gender and education level dependent at 5% level of significance? In other words, given the data collected above, is there a relationship between the gender of an individual and the level of education that they have obtained?
"""
import scipy.stats as st

female = [60, 54, 46, 41] #From given table
male = [40, 44, 53, 57] #From given table

female_total = 201 #From given table
male_total = 194 #From given trom
people_total = 395 #From given total
edu_level_total = [100, 98, 99, 98] #From given table

significance_level = 0.05 #Given, 5% level of significance

sample_size = 4 #Given, Education levels: High School, Bachelors, Masters & Ph.d

def calc_expected_values(comm_total_lst, seq_total, sample_len): #Calculates expected values 
    lst = []
    for val in comm_total_lst:
        lst.append(val*seq_total/sample_len)
    return lst

expected_female = calc_expected_values(edu_level_total,female_total,people_total) #Calculates expected values for female

expected_male = calc_expected_values(edu_level_total,male_total,people_total) #Calculates expected values for male

f_obs = female + male 
print("\nF-Observed (From given table):",f_obs)

f_exp = expected_female + expected_male
print("\nF-Expected (Calculated from given table):",f_exp)

dof = sample_size - 1 #Degree of freedom of given data set

chi_sq_calc = st.chisquare(f_obs,f_exp) #Calculated Chi-Square for given observed and expected values 
print("\nChi-Square (Calculated using F-Observed and F-Expected):",chi_sq_calc.statistic)

chi_sq_critical = st.chi2.isf(q=significance_level, df=dof) #Calculates Chi-Square critical values 
print("\nChi-Square Critical (Calculated using given significance level and degree of freedom):",chi_sq_critical)

#The critical value of Chi-Square with calculated degree of freedom is lesser than the calculated.Therefore we reject the null hypothesis and conclude that the education level depends on gender at a 5% level of significance.
print("\nIf the critical value of Chi-Square with calculated degree of freedom is lesser than the calculated. Therefore we reject the null hypothesis and conclude that the education level depends on gender at a 5% level of significance.")

if chi_sq_critical < chi_sq_calc.statistic:
    print("\nReject the null hypothesis and this concludes that the education level depends on gender at a 5% level of significance.")
else:
    print("\nNull hypothesis can not be rejected and this concludes that the education level does not depends on gender at a 5% level of significance.")