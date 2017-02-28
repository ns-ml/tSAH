import func

dataFile = 'original.txt'
splitDir = 'data/split'

# TODO: Seperate into individual reports
func.split_files(dataFile)

# TODO: Remove non head CT reports (consider adding MRI?)
func.removeNonCT(splitDir)

# TODO: Remove no mention of SAH
func.removeNoSAH(splitDir)

# TODO: Pick earliest study, remove duplicates

# TODO: Provide result file

# Assumptions:
# - Each report has a type: CT SCAN HEAD (case-insensitive)
# - Does not take into account negation