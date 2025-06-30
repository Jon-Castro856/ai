import unittest
from functions.get_file_content import get_file_content

class Test(unittest.TestCase):
    def test_gfo(self):
        print("Testing with main.py")
        files = get_file_content("calculator", "main.py")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")
        

        print("Testing with calculator.py")
        files = get_file_content("calculator", "pkg/calculator.py")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

        print("Testing with non-existing directory")
        files = get_file_content("calculator", "/bin/cat")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

        print("Testing with lorem for truncation")
        files = get_file_content("calculator", "lorem.txt")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")


if __name__ == "__main__":
    unittest.main()