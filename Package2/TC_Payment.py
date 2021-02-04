
import unittest

class PaymentTest(unittest.TestCase):
    def test_paybycard(self):
        print("Payment by Card")
        self.assertTrue(True)
    def test_paybycash(self):
        print("Payment by Cash")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()