__author__ = 'Albert-Jan'

import unittest

class InputFunTests(unittest.TestCase):

    def test_input_fun_should_return_prompt_asynchronously(self):
        res = input(">>> ")
        self.assertEqual(res, ">>> testing")


    def test_error_on_input(self):
        threw = False
        try: 
            res = input("error")
        except ValueError as e:
            self.assertIsInstance(e, ValueError)
            threw = True

        self.assertTrue(threw)

if __name__ == '__main__':
    unittest.main()
