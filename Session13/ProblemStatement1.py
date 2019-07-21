#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
You survey households in your area to find the average rent they are paying. Find the standard deviation from the following data:

$1550, $1700, $900, $850, $1000, $950.
"""
import statistics as st

data = [1550,1700,900,850,1000,950]
print("Standard Deviation =", st.stdev(data))