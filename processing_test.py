import func
import os.path


def test_split():
    func.split_files('test.txt')
    assert os.path.isfile('data/split/file_1.txt')


def testRemoveNonCT():
    dir = 'data/split'
    func.removeNonCT(dir)
    assert os.path.isfile('data/split/file_1.txt') == False
    assert os.path.isfile('data/split/file_2.txt')
