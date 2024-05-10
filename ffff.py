import unittest
def add_two_numbers(x,y):
    return x+y

class TestAddTwoNumbers(unittest.TestCase):
    def test_add_two_numbers(self):
        self.assertEqual(add_two_numbers(4,6), 10)

if __name__=="__main__":
    unittest.main()



    