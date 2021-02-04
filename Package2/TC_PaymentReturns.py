
import unittest


class PaymentReturnTest(unittest.TestCase):
    def test_taxreturn(self):
        print("Tax return by Card")
        self.assertTrue(True)
    def test_paycash(self):
        print("Tax return by Cash")
        self.assertTrue(True)
if __name__=="__main__":
    unittest.main()
