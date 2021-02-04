import unittest

class LoginTest(unittest.TestCase):
    def test_loginbyemail(self):
        print("Login by email")
        self.assertTrue(True)
    def test_loginbyfb(self):
        print("Login by FB")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()
