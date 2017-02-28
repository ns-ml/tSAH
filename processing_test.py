import func
import os.path

dir = 'data/split'
testFile = 'test.txt'

def test_split():
    func.split_files(testFile)
    assert os.path.isfile('data/split/file_1.txt')


def testRemoveNonCT():
    func.removeNonCT(dir)
    assert os.path.isfile('data/split/file_1.txt') == False
    assert os.path.isfile('data/split/file_2.txt')

def testRemoveNoSAH():
    func.removeNoSAH(dir)
    assert os.path.isfile('data/split/file_2.txt')
    assert os.path.isfile('data/split/file_5.txt') == False