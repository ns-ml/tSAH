import os
import re

def split_files(data):

    with open("data/" + data, mode='r') as bigfile:
        reader = bigfile.read()
        for i, part in enumerate(reader.split('[report_end]')):
            with open("data/split/file_" + str(i + 1) + ".txt", mode='w') as newfile:
                newfile.write(part)

def removeNonCT(dir):

    badFiles = []
    for file in os.listdir(dir):
        with open(os.path.join(dir, file), 'r') as f:
            reader = f.read().lower()
            mo = re.search('''type:\s*ct\s*scan\s*head''', reader)
            if not mo:
                badFiles.append(f.name)

    for name in badFiles:
        os.remove(name)

def removeNoSAH(dir):

    noSAHFiles = []

    for file in os.listdir(dir):
        with open(os.path.join(dir, file), 'r') as f:
            report = f.read().lower()
            mo = re.search('''(subarachnoid\s*(hemorrhage|bleed|blood))|(sah)''', report)
            if not mo:
                noSAHFiles.append(f.name)


    for name in noSAHFiles:
        os.remove(name)
