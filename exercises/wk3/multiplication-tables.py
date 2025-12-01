#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Filename: multiplication-tables.py
Author: Joe
Date: 2025-11-30
Version: 0.1.0
Description: This script generates multiplication tables for integers from (0, 12), inclusive.
"""

# List comprehension initialization
rows, cols = 13, 13
matrix = [[0 for _ in range(cols)] for _ in range(rows)]
# matrix = [[0] * cols for _ in range(rows)]

# Populate matrix
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = i * j

# # Or populate matrix With enumerate
# for i, row in enumerate(matrix):
#     for j in range(cols):
#         row[j] = i * j
#
# # Or populate matrix with double enumerate
# for i, row in enumerate(matrix):
#     for j, _ in enumerate(row):
#         row[j] = i * j

# Print matrix
print(matrix)

# Spot Test
assert matrix[0][0] == 0
assert matrix[12][12] == 144
assert matrix[7][7] == 49
