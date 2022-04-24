#!/usr/bin/env python3.8
from credentials import Credentials

def create_Credentials(account_name,account_password,account_email):
    """
    Function to create a new credentials
    """
    new_credentials = Credentials(account_name,account_password,account_email)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save credentials
    """
    credentials.save_credentials()

def delete_credentials(credentials):
    """
    Function to delete credentials
    """
    credentials.delete_credentials()

def find_credentials(account_name):
    """
    Function that finds a credentials by account name
    """
    return Credentials.find_by_name(account_name)

def credentials_exist(account_name):
    """
    Function that checks if a credentials exists
    """
    return Credentials.credentials_exist(account_name)

def display_credentials():
    """
    Function that returns the credentials list
    """
    return Credentials.display_credentials()

def main():
    print("Hello! Welcome to your password locker. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. What would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a credentials, ex -exit the credentials list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Credentials")
            print("-"*10)

            print("Account name: ")
            account_name = input()

            print("Account password: ")
            account_password = input()

            print("Account email: ")
            account_email = input()

            save_credentials(create_Credentials(account_name,account_password,account_email)) # create and save new credentials.
            print('\n')
            print(f"New Credentials {account_name} {account_password} {account_email} created")
            print('\n')

        elif short_code == 'dc':

            if display_credentials():
                print("Here is a list of all your credentials")
                print('\n')

                for credentials in display_credentials():
                    print(f"{credentials.account_name} {credentials.account_password} {credentials.account_email}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any credentials saved yet")
                print('\n')

        elif short_code == 'fc':

            print("Enter the account name you want to search for")

            search_name = input()
            if credentials_exist(search_name):
                search_credentials = find_credentials(search_name)
                print(f"{search_credentials.account_name} {search_credentials.account_password} {search_credentials.account_email}")
                print('-' * 20)

            else:
                print("That credentials does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else: print("I really didn't get that. Please use the short codes")

if __name__ == '__main__':

    main()

