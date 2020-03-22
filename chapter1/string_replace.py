import unittest

def can_replace(str1: str, str2: str) -> bool:
    if str1 == str2:
        return True

    if len(str1) == len(str2):
        dif_count = 0
        # 置換
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                dif_count += 1
            if dif_count > 1:
                return False
        return True
    elif len(str1) > len(str2):
        if len(str1)-len(str2)>1:
            return False
        
        i = 0
        j = 0
        dif_count = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                i += 1
                dif_count += 1
                if dif_count > 1:
                    return False
        return True
    else:
        if len(str2)-len(str1)>1:
            return False
        
        i = 0
        j = 0
        dif_count = 0
        while i < len(str1) and j < len(str2):
            if str1[i] == str2[j]:
                i += 1
                j += 1
            else:
                j += 1
                dif_count += 1
                if dif_count > 1:
                    return False
        return True

class Test(unittest.TestCase):

    def test_can_replace(self):
        ok = [
            ("pale","ple"),
            ("ppppppppppppa","pppppppppppp"),
            ("pale","bale"),
            ("abcde","abcdef"),
            ("ale","pale"),
            ("pale","ale"),
            ("ale","all"),
            ]
        ng = [
            ("pale","bake"),
            ("atyhe","fsefg"),
            ("aaa","aaabb"),
            ('pkle', 'pable'),
            ('pal', 'palks'),
            ('palks', 'pal')
            ]

        for str1,str2 in ok:
            actual = can_replace(str1,str2)
            self.assertTrue(actual)
        
        for str1,str2 in ng:
            actual = can_replace(str1,str2)
            self.assertFalse(actual)   


if __name__ == "__main__":
    unittest.main()
