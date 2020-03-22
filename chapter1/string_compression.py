import unittest

def compress(string: str) -> str:
    if len(string) < 2:
        return string

    prev_char = string[0]
    cur_count = 1

    res = ""

    for i in range(1,len(string)):
        if prev_char == string[i]:
            cur_count += 1
        else:
            res += prev_char+str(cur_count)
            prev_char = string[i]
            cur_count = 1
    else:
        res += prev_char+str(cur_count)

    if len(string) <= len(res):
        return string
    else:
        return res

    ## list.join()の方がいい

class Test(unittest.TestCase):

    def test_can_replace(self):
        ok = [
            ("aaaaaaaaaaa","a11"),
            ("aa","aa"),
            ("a","a"),
            ("abcde","abcde"),
            ("aaaabbccddfftttttt","a4b2c2d2f2t6"),
            ("aaaab","a4b1"),
            ]

        for original,answer in ok:
            actual = compress(original)
            self.assertEqual(actual,answer)


if __name__ == "__main__":
    unittest.main()