import pytest
from homework import (task1, task2, task3, task4, task5, task6, task17, task18, task19, task20)

def test_task1():
    data1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    data2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    rez = [1, 2, 3, 5, 8, 13]
    assert task1(data1, data2) == rez

def test_task2():
    data = 'I am a good developer. I am also a writer'
    assert task2(data) == 5

def test_task3():
    assert task3(27) == True

def test_task4():
    assert task4(48) == 3


def test_task5():
    data = [0, 2, 3, 4, 6, 7, 10]
    rez = [2, 3, 4, 6, 7, 10, 0]
    assert task5(data) == rez

def test_task6():
    data = [5, 7, 9, 11]
    assert task6(data) == True

def test_task17():
    num_factorial = 5
    rez = 120
    assert task17(num_factorial) == rez

def test_task18():
    data = 'modify it using the following algorithm zz'
    rez = 'npEjgz jU vtjOh UIf gpmmpxjOh bmhpsjUIn AA'
    assert task18(data) == rez

def test_task19():
    data = 'hello world'
    rez = 'ehllo dlorw'
    assert task19(data) == rez

def test_task20():
    num1 = 20
    num2 = [19, 20, 21]
    assert task20(num1, num2[0]) == False
    assert task20(num1, num2[1]) == '-1'
    assert task20(num1, num2[2]) == True

