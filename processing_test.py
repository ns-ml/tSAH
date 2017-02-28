import func
import os.path
import pandas as pd

directory = 'data/split'
testFile = 'test.txt'
numberOfTestFiles = 6

def test_split():
    func.split_files(testFile)
    assert os.path.isfile('data/split/file_1.txt')

def testCount():
    file_count = func.countFiles(directory)
    assert file_count == numberOfTestFiles


def testRemoveNonCT():
    func.removeNonCT(directory)
    assert os.path.isfile('data/split/file_1.txt') == False
    assert os.path.isfile('data/split/file_2.txt')

def testRemoveNoSAH():
    func.removeNoSAH(directory)
    assert os.path.isfile('data/split/file_2.txt')
    assert os.path.isfile('data/split/file_5.txt') == False

def testDataFrame():
    df = func.toDataFrame(directory)
    assert df.ix[0, 0] == '100074204'