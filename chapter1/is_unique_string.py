import unittest

def is_unique(string: str)-> bool:
    # ASCIIだと仮定して(128)それ以上なら必ず重複
    if len(string) > 128:
        return False

    char_set = [False]*128

    for char in string:
        ord_char = ord(char)
        if char_set[ord_char]:
            return False
        else:
            char_set[ord_char] = True
    
    return True


class Test(unittest.TestCase):
    data_true = ["", "abcdefghijk","4p[()-#$%^&*"]
    data_false = ["aaerg", "bbbbbb", "hb juf=j()","  "]

    def test_unique(self):
        for string in self.data_true:
            actual = is_unique(string)
            self.assertTrue(actual)
        
        for string in self.data_false:
            actual = is_unique(string)
            self.assertFalse(actual)

if __name__ == "__main__":
    unittest.main()




