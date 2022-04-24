import unittest # Importing the unittest module
from credentials import Credentials #Importing the credentials class
import pyperclip

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

def tearDown(self):
    """
    tearDown method that does clean up after each test case has run.
    """
    Credentials.credentials_list = []

def test_save_multiple_credentials(self):
    """
    test_save_multiple_credentials to check if we can save multiple credentials
    objects to our credentials_list
    """
    self.new_credentials.save_credentials()
    test_credentials = Credentials("karen","karen123","karen@gmail") # new credentials
    test_credentials.save_credentials()
    self.assertEqual(len(Credentials.credentials_list),2)

def test_delete_credentials(self):
    """ 
    test_delete_credentials to test if we can remove a credentials from our credentials list"""  
    self.new_credentials.save_credentials()
    test_credentials = Credentials("karen","karen123","karen@gmail") # new credentials
    test_credentials.save_credentials()

    self.new_credentials.delete_credentials() # Deleting a credentials object
    self.assertEqual(len(Credentials.credentials_list),1)

def  test_find_credentials_by_name(self):
    """
    test to check if we can find a credentials by account name and display information """
    
    self.new_credentials.save_credentials()
    test_credentials = Credentials("karen","karen123","karen@gmail") # new credentials
    test_credentials.save_credentials()

    found_credentials = Credentials.find_by_name("karen")

    self.assertEqual(found_credentials.account_name,test_credentials.account_name)

def test_copy_email_(self):
    """
    Test to confirm that we are copying the email address from a found credentials.
    """
    self.new_credentials.save_credentials()
    Credentials.copy_email("karen")

    self.assertEqual(self.new_credentials.account_email,pyperclip.paste())







    if __name__ == "__main__":
        unittest.main()


    