import yaml
import pytest
from main import tribonacci


def getTestData():
    with open(r'testDataTribonacci.yaml') as file:
        testData = yaml.load(file, Loader=yaml.FullLoader)
        return testData


def test_tribonacci(testData):
    for key in testData:
        if testData[key]['type'] == 'valid':
            assert tribonacci(testData[key]['input']) == testData[key]['expected'], "test failed because the result is not equal to " + str(
                testData[key]['expected']) + " with the following input: " + str(testData[key]['input'])
        if testData[key]['type'] == 'exception':
            with pytest.raises(Exception, match=r".* Exception: .*"):
                tribonacci(testData[key]['input'])


testData = getTestData()
test_tribonacci(testData)
