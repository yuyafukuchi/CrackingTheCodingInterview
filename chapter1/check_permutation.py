import unittest
from collections import Counter


def check(str1: str, str2: str) -> bool:
    counter1 = Counter(str1)
    counter2 = Counter(str2)

    if counter1 == counter2:
        return True
    else:
        return False

class Test(unittest.TestCase):

    def test_check_permutation(self):
        data_true = [('abc','bac'),('aaaa','aaaa'),('abcdefghijk','kjihgfedabc')]
        data_false = [('aaa','aaaa'),('abcd','abce')]

        for str1,str2 in data_true:
            actual = check(str1,str2)
            self.assertTrue(actual)
        
        for str1,str2 in data_false:
            actual = check(str1,str2)
            self.assertFalse(actual)   
        

if __name__ == "__main__":
    unittest.main()
