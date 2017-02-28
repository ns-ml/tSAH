import func
import pandas as pd
import os

dataFile = 'original.txt'
directory = 'data/split'

# TODO: Seperate into individual reports
func.split_files(dataFile)

# How many reports are there?


# TODO: Remove non head CT reports (consider adding MRI?)
func.removeNonCT(directory)

# TODO: Remove no mention of SAH
func.removeNoSAH(directory)

# TODO: Pick earliest study, remove duplicates
# Start by creating a pandas dataframe
df = func.toDataFrame(directory) 
# TODO: Provide result file
df.to_csv('results.csv')
# Assumptions:
# - Each report has a type: CT SCAN HEAD (case-insensitive)
# - Does not take into account negation