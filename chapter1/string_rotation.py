import unittest# O(N)

# 第一引数に指定した文字列が呼び出し元の文字列に含まれている場合はそのスタートの位置（最初の文字の位置）、含まれていない場合は-1が返される。
def is_substring(string, sub):
    return string.find(sub) != -1


def string_rotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2)
    return False


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('waterbottle', 'erbottlewat', True),
        ('foo', 'bar', False),
        ('foo', 'foofoo', False),
        ('foo','ofo',True),
        ('fffffff','fffffff',True)
    ]

    def test_string_rotation(self):
        for [s1, s2, expected] in self.data:
            actual = string_rotation(s1, s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()