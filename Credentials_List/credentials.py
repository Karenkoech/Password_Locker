class Credentials():
    """
    Class that generates new instances of credentials
    """
    Credentials_list = [] # Empty credentials list
def __init__(self,account_name,account_password,account_email,):
    """
    __init__ method that helps us define properties for our objects.
    """
    self.account_name = account_name
    self.account_password = account_password
    self.account_email = account_email

    def save_credentials():
        """
        save_credentials method saves credentials objects into credentials_list
        """
        Credentials.credentials_list.append(self)

    def delete_credentials():
        """
        delete_credentials method deletes a saved credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)

new_credentials = Credentials("karen","karen123","karen@gmail.com")
new_credentials.save_credentials()
print(Credentials.credentials_list)


