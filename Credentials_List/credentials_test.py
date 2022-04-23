import unittest # Importing the unittest module
from credentials import Credentials #Importing the credentials class

class TestCredentials(unittest.TestCase):
    """
    Test class that defines test cases for the credentials class behaviours.
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """
    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credentials = Credentials("karen" "karen123","karen@gmail") # create credentials object

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_credentials.account_name,"karen")
        self.assertEqual(self.new_credentials.account_password,"karen123")
        self.assertEqual(self.new_credentials.account_email,"karen@gmail")

def test_save_credentials(self):
    """
    test_save_credentials test case to test if the credentials object is saved into
     the credentials list
    """
    self.new_credentials.save_credentials() # saving the new credentials
    self.assertEqual(len(Credentials.credentials_list),1)





    if __name__ == "__main__":
        unittest.main()


    