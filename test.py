import unittest

from venmo import get_number_of_transactions


class TestStringMethods(unittest.TestCase):

    def test_get_number_of_transactions(self):
        test_data = {'data': [{'Foo': 'Bar'}, {'Foo2': 'Bar2'}, {'Foo3': 'Bar3'}]}
        self.assertEqual(get_number_of_transactions(test_data), 3)


if __name__ == '__main__':
    unittest.main()