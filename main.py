from TestHUDL import TestHUDL

if __name__ == '__main__':
    # Test Case 1: Login with correct credentials
    print("Test Case 1")
    tc1 = TestHUDL()
    TestHUDL.callTest(tc1, 'Config/configSettings.ini')

    # Test Case 2: Login with correct email, but incorrect password
    print("Test Case 2")
    tc2 = TestHUDL()
    TestHUDL.callTest(tc2, 'Config/configSettings-IncorrectPassword.ini')

    # Test Case 3: Login with incorrect email, but correct password
    print("Test Case 3")
    tc3 = TestHUDL()
    TestHUDL.callTest(tc3, 'Config/configSettings-IncorrectEmail.ini')

    # Test Case 4: Login with incorrect credentials
    print("Test Case 4")
    tc4 = TestHUDL()
    TestHUDL.callTest(tc4, 'Config/configSettings-IncorrectCredentials.ini')

    # Test Case 5: Improper Email with no .COM
    print("Test Case 5")
    tc5 = TestHUDL()
    TestHUDL.callTest(tc5, 'Config/configSettings-WrongEmailFormat1.ini')

    # Test Case 6: Improper Email with no @
    print("Test Case 6")
    tc6 = TestHUDL()
    TestHUDL.callTest(tc6, 'Config/configSettings-WrongEmailFormat2.ini')

    # Test Case 7: Improper Email with special characters
    print("Test Case 7")
    tc7 = TestHUDL()
    TestHUDL.callTest(tc7, 'Config/configSettings-WrongEmailFormat3.ini')

    # Test Case 8: No Email Provided
    print("Test Case 8")
    tc8 = TestHUDL()
    TestHUDL.callTest(tc8, 'Config/configSettings-NoEmail.ini')

    # Test Case 9: No Password Provided
    print("Test Case 9")
    tc9 = TestHUDL()
    TestHUDL.callTest(tc9, 'Config/configSettings-NoPassword.ini')
