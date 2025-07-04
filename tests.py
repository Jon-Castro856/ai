import unittest
from functions.run_python import run_python_file

class Test(unittest.TestCase):
    def test_gfo(self):
        print("Testing")
        files = run_python_file("calculator", 'main.py')
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

        print("Testing 2")
        files = run_python_file("calculator", 'tests.py')
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

        print("Testing external directories")
        files = run_python_file("calculator", '../main.py')
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

        print("Testing nonexisting file")
        files = run_python_file("calculator", 'nonexistent.py')
        print(files)
        self.assertTrue(files)
        print("------------------------------------")
    
if __name__ == "__main__":
    unittest.main()