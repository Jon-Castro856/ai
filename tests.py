import unittest
from functions.write_file import write_file

class Test(unittest.TestCase):
    def test_gfo(self):
        print("Testing with lorem")
        files = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")
    
        print("Testing with new file")
        files = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")

        print("Testing with non-existing directory")
        files = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(files)
        self.assertTrue(files)
        print("------------------------------------")



if __name__ == "__main__":
    unittest.main()