import unittest

from Package1.TC_login import LoginTest
from Package1.Tc_signup import SignupTest
from Package2.TC_Payment import PaymentTest
from Package2.TC_PaymentReturns import PaymentReturnTest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentReturnTest)

#Creating test suite
Sanity_test=unittest.TestSuite([tc1,tc2])
Function_test=unittest.TestSuite([tc3,tc4])
Master_test=unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner(verbosity=2).run(Master_test)
