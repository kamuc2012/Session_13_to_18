#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Find the variance for the following set of data representing trees in California (heights in feet):

3, 21, 98, 203, 17, 9
"""
import statistics as st

data = [3, 21, 98, 203, 17, 9]
print("Variance =", st.variance(data))