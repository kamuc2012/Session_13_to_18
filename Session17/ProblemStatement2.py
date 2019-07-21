#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Using the following data, perform a one-way analysis of variance using α=.05.

Write up the results in APA format.

[Group1: 51, 45, 33, 45, 67]
[Group2: 23, 43, 23, 43, 45]
[Group3: 56, 76, 74, 87, 56]
"""
import pandas as pd
import scipy.stats as stats

df = pd.DataFrame({"Group1": [51, 45, 33, 45, 67], "Group2": [23, 43, 23, 43, 45], "Group3": [56, 76, 74, 87, 56]})
print(df)
print("\n", "="*50, "\n", sep="")

'''
Answer:
H0:mean_G1 = mean_G2 = mean_G3
H1:mean_G1 != mean_G2 != mean_G3

mean1=(51+ 45+ 33+ 45+ 67)/5
mean1
mean2=(23+ 43+ 23+ 43+ 45)/5
mean2
mean3=(56+ 76+ 74+ 87+ 56)/5
mean3

var=(((51-mean1)**2)+((45-mean1)**2)+((33-mean1)**2)+((45-mean1)**2)+((67-mean1)**2))/4
var2=(((23-mean2)**2)+((43-mean2)**2)+((23-mean2)**2)+((43-mean2)**2)+((45-mean2)**2))/4
var3=(((56-mean3)**2)+((76-mean3)**2)+((74-mean3)**2)+((87-mean3)**2)+((56-mean3)**2))/4

print(var,var2,var3)

MS_error=(153.2+128.8+183.2)/3=155.07
df_error=15−3=12
SS_error=(155.07)(15−3)=1860.8

Grand mean,  x_bar_grand=(48.2+35.4+69.8)/3=51.13

 group mean grand mean deviations sq deviations
       48.2      51.13      -2.93          8.58
       35.4      51.13     -15.73        247.43
       69.8      51.13      18.67        348.57
       
Var_means=(604.58)/3−1=302.29

MS_between=(302.29)*(5)=1511.45

Test statistic and critical value

    F=1511.45/155.07=9.75
    Fcritical(2,12)=3.89 (using F table)

since 9.75>3.89, Hence we reject H0

ANOVA table
source  SS      df      MS     F
group   1057.5   2    528.75 3.93
error  11703.82 87    134.53
total  12761.32

Effect size
    nita_2=1057.5/12761.32=0.08
APA write up 
    F(2, 12)=9.75, p <0.05, nita_2=0.62.
'''