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
import pandas as pd
import scipy.stats as stats

# Creating data frame with provided dataset
education = ["High School", "Bachelor", "Masters", "PHD"]
female = [60, 54, 46, 41]
male = [40, 44, 53, 57]
df = pd.DataFrame({"Education": education, "Female": female, "Male": male})
print(df)
print("\n", "="*50, "\n", sep="")

# Calculate Mean, Standard Deviation, ZScore and P values
df["Mean_Female"] = df["Female"].mean()
df["Mean_Male"] = df["Male"].mean()

df["StdDev_Female"] = df["Female"].std()
df["StdDev_Male"] = df["Male"].std()

df["Z_Female"] = stats.zscore(df["Female"])
df["Z_Male"] = stats.zscore(df["Male"])

df["P_Female"] = [stats.norm.cdf(pval) for pval in stats.zscore(df["Female"])]
df["P_Male"] = [stats.norm.cdf(pval) for pval in stats.zscore(df["Male"])]

print(df)
print("\n", "="*50, "\n", sep="")

print("From the above data analysis - we can conclude that education level depends on the gender.\n\n")

print("Male population is higher than Femal population for education level at Masters AND Ph.D.")
print("Femal population is higher than Male population for education level High-School AND Bachelor")