import sys, pathlib
sys.path.append(pathlib.Path(__file__).parent.parent / 'src')
from {{filename}} import {{filename}}
import unittest

class {{filename}}Test(unittest.TestCase):
    def test_init(self):
        ins = {{filename}}()
        self.assertEqual({{filename}}, type(ins))
    def test_raise(self):
        with self.assertRaises(Exception) as e:
            raise Exception('A')
        self.assertEqual('A', e.exception.args[0])


if __name__ == '__main__':
    unittest.main()
