import unittest
from os_rename import replacing

class MyTestCase(unittest.TestCase):
    def test_rename(self):
        self.assertEqual(replacing("2465873457",["2","1"]),"1465873457")
        self.assertEqual(replacing("2222_1111465873457",["2","1"]),"1111_1111465873457")
        self.assertEqual(replacing("1. Выписка ЕГРН характеристики 78_06_0002205_13 от 19.12.19",["_","-"]),
                         "1. Выписка ЕГРН характеристики 78-06-0002205-13 от 19.12.19")
        self.assertEqual(replacing("1. 78_06_0002205_13 от 19.12.19",[" 7"," (7"]),
                         "1. (78_06_0002205_13 от 19.12.19")
        self.assertEqual(replacing("1- & Contract %% 78_06_0002205_13 от 19.12.19", [" от", ") от"]),
                         "1- & Contract %% 78_06_0002205_13) от 19.12.19")

if __name__ == '__main__':
    unittest.main()
