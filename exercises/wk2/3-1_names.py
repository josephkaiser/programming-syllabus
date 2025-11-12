'''
3-1. Names

This is the accompanying code for PythonCrashCourse chapter 3 exercise 3-1.

Original Author: Joseph Kaiser
Creation Date: 11/2/2025
'''

names = ["jon", "john", "johnny", "jim", "jimbo", "jimmy", "jimothy"]

for i in range(len(names)):
    print(f"{names[i].strip().title()}")
    
