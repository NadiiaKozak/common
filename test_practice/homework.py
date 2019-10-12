import datetime
import re
import math


def task1(data1, data2):
    """
    Return a list that contains only the elements that are common between the lists (without duplicates).
    :param data1: list
    :param data2: list
    :return: list
    """
    return list(set(data1).intersection(data2))


def task2(data):
    """
    Return the number of times that the letter “a” appears anywhere in the given string.
    :param data: str
    :return: int
    """
    return data.count('a')


def task3(num):
    """
    Check if a given positive integer is a power of three.
    :param num: int
    :return: bool
    """
    return math.log(num, 3).is_integer()


def task4(num):
    """
    Added the digits of a positive integer repeatedly until the result has a single digit.
    :param num: int
    :return: int
    """
    while num >= 10:
        num = sum([int(i) for i in str(num)])
    return num


def task5(data):
    """
    Push all zeros to the end of a list.
    :param data: list
    :return: list
    """
    return [i for i in data if i != 0] + [i for i in data if i == 0]


def task6(data):
    """
    Check a sequence of numbers is an arithmetic progression or not.
    :param data: list
    :return: bool
    """
    return 1 == len(set(data[i + 1] - data[i] for i in range(len(data) - 1)))


def task7(data):
     """
     Write a Python program to find the number in a list that doesn't occur twice.
     :param data: list
     :return: list
     """
     return [i for i in data if data.count(i) == 1]

def task8(data):
    """
    Write a Python program to find a missing number from a list.
    :param data: list
    :return: int
    """
    z = data.pop()
    l = [j+1 for j in range(z)]
    data.append(z)
    l1 = [i for i in l if i not in data]
    return l1



def task9(data):
    """
    Write a Python program to count the elements in a list until an element is a tuple
    :param data: list
    :return: int
    """
    j = 0
    for i in data:
          if not isinstance(i, tuple):
               j +=1
          else:
               break
    return j

def task10(data):
    """
    Write a program that will take the str parameter being passed and return the string
    in reversed order. For example: if the input string is "Hello World and Coders" then
    your program should return the string sredoC dna dlroW olleH.
    :param data: str
    :return: str
    """
    return data[::-1]

def task11(num):
    """
    Write a program that will take the num parameter being passed and return the number of hours
    and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3).
    Separate the number of hours and minutes with a colon.
    :param num: int
    :return: str
    """
    td = str(datetime.timedelta(minutes=num)) [:-3]
    return td

def task12(data):
    """
    Write a program that will take the parameter being passed and
    return the largest word in the string. If there are two
    or more words that are the same length, return the first word f
    rom the string with that length. Ignore punctuation.
    :param data: str
    :return: str
    """
    data = re.sub("[^\w]", " ",  data).split()
    data = sorted(data, key=lambda a: len(a), reverse=True)
    return data[0]

def task13():
    """
    Write a program (using functions!) that asks the user for a long string
    containing multiple words. Print back to the user the same string, except
    with the words in backwards order.
    :param data: str
    :return: str
    """
    data = input('input a long string containing multiple words: ', )
    return (' '.join(reversed(data.split())))

def task14():
    """
    Write a program that asks the user how many Fibonnaci numbers to generate
    and then generates them. Take this opportunity to think about how you can
    use functions. Make sure to ask the user to enter the number of numbers
    in the sequence to generate.
    (Hint: The Fibonnaci seqence is a sequence of
    numbers where the next number in the sequence is the sum of the previous
    two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
    """
    try:
        num = int(input('how many Fibonnaci numbers to generate?: ', ))
        if num == 0:
            return 0
        elif num == 1 or num == 2:
            return 1
        elif num > 2:
            f = [1, 1]
            for i in range(2, num):
                f.append(f[i-2] + f[i-1])
            return f
    except ValueError:
        print('entered incorrect number ')




def task15(data):
    """
    Let’s say I give you a list saved in a variable:
     data = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
     Write one line of Python that takes this list a and makes a new list
     that has only the even elements of this list in it.
    :return: list
    """
    return [i for i in data if i%2 == 0]

def task16():
    """
    Write a program that will add up all the numbers from 1 to input number.
    For example: if the input is 4 then your program should return 10 because
    1 + 2 + 3 + 4 = 10.
    :return: int
    """
    try:
        num = int(input('input number: ', ))
        if num == 0:
            return 0
        elif num >= 1:
            return sum([i for i in range(1, num+1)])
    except ValueError:
        print('entered incorrect number ')

def task17(num):
    """
    Write a program that will take the parameter being passed and
    return the factorial of it. For example: if num = 4,
    then your program should return (4 * 3 * 2 * 1) = 24
    :return:  int
    """
    return math.factorial(num)

def task18(data):
    """
    Write a program that will take the str parameter being passed and modify
    it using the following algorithm. Replace every letter in the string with
    the letter following it in the alphabet (ie. cbecomes d, zbecomes a).
    Then capitalize every vowel in this new string (a, e, i, o, u) and finally
    return this modified string.
    data :str
    :return: str
    """
    a = 'aeiou'
    l =[]
    for i in data:
        for j in i:
            if j != ' ':
                j = 'a' if j == 'z' else chr(ord(j) + 1)
                j = j.upper() if j in a else j
            else:
                j = ' '
            l.append(j)
    return ''.join(l)

def task19(data):
    """
    Write a program that will take the str string parameter being passed
    and return the string with the letters in alphabetical order (ie. hello
     becomes ehllo). Assume numbers and punctuation symbols will not be included
     in the string.
    :param data: str
    :return: str
    """
    data = data.split()
    data = [''.join(sorted(i)) for i in data]
    return ' '.join(data)

def task20(num1, num2):
    """
    Write a program that will take both parameters being passed and return the true
    if num2 is greater than num1, otherwise return the false. If the parameter value
    s are equal to each other then return the string -1
    :param num1: int
    :param num2: int
    :return: bool
    """
    return '-1' if num2 == num1 else num2 > num1
