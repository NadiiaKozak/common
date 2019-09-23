"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    if first == second :
        return True
    else :
        return False
    


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if type(first)==type(second):
        return True
    else :
        return False


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if id(first)==id(second):
        return True
    else:
        return False
    


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    #try:
        #raise ValueError
    if type(first_value)is not int:
        raise ValueError('no int')
    elif type(second_value)is not int:
        raise ValueError('no int')
    else: 
        mult=first_value*second_value
        return mult                 
    #except ValueError:
    #    print('no int')
    
    
      
        


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise ValueError

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        ValueError

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    try:
        first_value1=int(first_value)
        second_value1=int(second_value)
        mult=first_value1*second_value1
        return mult
        
    except TypeError :
        print(" is not possible to convert arguments to int value")
        

def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    if word in text:
        return True
    else:
        return False
        


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    L=[i for i in range (13)]
    del L[6:8]
    return L


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    L=data
    V=list(filter(lambda x: x>=0,L))
    return V    


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """
    number=[i for i in range(1,27)]
    alphabetic=list(str('qwertyuiopasdfghjklzxcvbnm'))
    alphabetic.sort()
    vvv1=dict(zip(number,alphabetic,))
    return vvv1
    


def simple_sort(data: List[int]) -> list:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """
    L=data
    i=0
    j=0
    z=len(L)

    while i<z-1:
        while j<z-1:
            jjj=L[j]
            kkk=L[j+1]
            if jjj>kkk:
               k=L[j]
               L[j]=L[j+1]
               L[j+1]=k
            j+=1    
        i+=1
        j=0
    return L
              
              
