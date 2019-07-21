#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculate F Test for given 10, 20, 30, 40, 50 and 5, 10, 15, 20, 25.

For 10, 20, 30, 40, 50:
"""
import statistics as st

group1 = [10, 20, 30, 40, 50]
group1_total_inputs = len(group1)
group1_mean = st.mean(group1)
group1_sd = st.stdev(group1)
group1_varience = st.variance(group1)

group2 = [5, 10, 15, 20, 25]
group2_total_inputs = len(group2)
group2_mean = st.mean(group2)
group2_sd = st.stdev(group2)
group2_varience = st.variance(group2)

print("F Test value for", group1, "and", group2, "is", group1_varience / group2_varience)