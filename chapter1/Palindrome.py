import unittest
from collections import defaultdict

# O(N)
def is_palidrome(s: str) -> bool:
    s = s.lower()
    d = defaultdict(int)

    for char in s:
        if char == " ":
            continue
        d[char] += 1
    
    odd_count = 0
    # 奇数個のものが二こ以上あったらダメ
    for key, value in d.items():
        if value%2:
            if odd_count == 0:
                odd_count += 1
            else:
                return False
    return True

class Test(unittest.TestCase):

    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for test_string, expected in self.data:
            actual = is_palidrome(test_string)
            self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()