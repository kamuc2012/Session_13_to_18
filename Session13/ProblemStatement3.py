#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In a class on 100 students, 80 students passed in all subjects, 10 failed in one subject, 7 failed in two subjects and 3 failed in three subjects. 

Find the probability distribution of the variable for number of subjects a student from the given class has failed in.
"""
import pandas as pd

class_strength = 100
passed_all_subjects = 80
failed_one_subject = 10
failed_two_subjects = 7
failed_three_subjects = 3

prob_failing_zero_subject = float(passed_all_subjects) / class_strength
prob_failing_one_subject = float(failed_one_subject) / class_strength
prob_failing_two_subjects = float(failed_two_subjects) / class_strength
prob_failing_three_subjects = float(failed_three_subjects) / class_strength

print("The probability distribution of the variable for number of subjects a student from the given class has failed in: \n")

prob_distribution_data = {"X": ["P(X)"], "0": [prob_failing_zero_subject], "1": [prob_failing_one_subject], "2": [prob_failing_two_subjects], "3": [prob_failing_three_subjects]}
df = pd.DataFrame(data=prob_distribution_data)

print(df.to_string(index=False))