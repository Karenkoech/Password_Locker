
class Credentials():
    """
    Class that generates new instances of credentials
    """
    credentials_list = [] # Empty credentials list

    def __init__(self,account_name,account_password,account_email,):
        """
        __init__ method that helps us define properties for our objects.
        """
        self.account_name = account_name
        self.account_password = account_password
        self.account_email = account_email

    def save_credentials(self):
        """
        save_credentials method saves credentials objects into credentials_list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        delete_credentials method deletes a saved credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls,account_name):
        """
        Method that takes in a name and returns a credentials that matches that name.
        """
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials

    @classmethod
    def credentials_exist(cls,account_name):
        """
        Method that checks if a credentials exists from the credentials list.
        """
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True

        return False

    @classmethod
    def display_credentials(cls):
        """
        method that returns the credentials list
        """
        return cls.credentials_list
        
    



    