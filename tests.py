import unittest
from functions.get_files_info import get_files_info

class Test(unittest.TestCase):
    def test_gfo(self):
        print("Testing with current directory")
        files = get_files_info("calculator", ".")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")
        

        print("Testing with subdirectory")
        files = get_files_info("calculator", "pkg")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

        print("Testing with non-existing directory")
        files = get_files_info("calculator", "/bin")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

        print("Testing with higher level directory")
        files = get_files_info("calculator", "../")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

if __name__ == "__main__":
    unittest.main()