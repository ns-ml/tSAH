import os
import re
import pandas as pd

def split_files(data):

    with open("data/" + data, mode='r') as bigfile:
        reader = bigfile.read()
        for i, part in enumerate(reader.split('[report_end]')):
            with open("data/split/file_" + str(i + 1) + ".txt", mode='w') as newfile:
                newfile.write(part)

def countFiles(directory):
    _,_,files = os.walk(directory).next()
    return len(files)


def removeNonCT(directory):

    badFiles = []
    for file in os.listdir(directory):
        with open(os.path.join(directory, file), 'r') as f:
            reader = f.read().lower()
            mo = re.search('''type:\s*ct\s*scan\s*head''', reader)
            if not mo:
                badFiles.append(f.name)

    for name in badFiles:
        os.remove(name)

def removeNoSAH(directory):

    noSAHFiles = []

    for file in os.listdir(directory):
        with open(os.path.join(directory, file), 'r') as f:
            report = f.read().lower()
            mo = re.search('''(subarachnoid\s*(hemorrhage|bleed|blood))|(sah)''', report)
            if not mo:
                noSAHFiles.append(f.name)


    for name in noSAHFiles:
        os.remove(name)

def toDataFrame(directory):

    masterList = []
    for file in os.listdir(directory):
        with open(os.path.join(directory, file), 'r') as f:
            report = f.read().lower()
            reportTrimmed = re.sub('\n|\r', ' ', report)
            reportTrimmed = re.sub(' +', ' ', reportTrimmed).strip()

            #MRN
            mo = re.search(r'(\d+)\|', report)
            mrn = mo.group(0).rstrip('|')

            #Report Body
            body = re.search('report:(.*)radiologist', reportTrimmed).group(1).strip()

            masterList.append([mrn, body])

    df = pd.DataFrame(masterList, columns=['MRN', 'Report'])
    pd.to_numeric(df['MRN'])
    return df
