import unittest

class SignupTest(unittest.TestCase):
    def test_signbyemail(self):
        print("SignUp by email")
        self.assertTrue(True)
    def test_signbyfb(self):
        print("Sign UP by FB")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()
