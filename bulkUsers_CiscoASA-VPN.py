"""
This script lets you create Anyconnect VPN users in bulk mode
"""
import sys
import pyfiglet



def main():
    """
    Main function that executes the script
    """

    banner = pyfiglet.figlet_format('CISCO ASA - Remote Access VPN users')
    print(banner)

    print("Please, choose group-policy to associate with the users: ")
    groupPolicy = input()


    with open("C:\\Users\\[your name]\\your-file.txt") as f:
        usersList = f.read()

    usersList = usersList.split("\n")

    with open("C:\\Users\\[your name]\\your-file.txt") as f:
        passwordsList = f.read()

    passwordsList = passwordsList.split("\n")

    for i in range(0, 51):
        print(f"username {usersList[i]} password {passwordsList[i]} privilege 0")
        print(f"username {usersList[i]} attributes")
        print(f" vpn-group-policy {groupPolicy}\n service-type remote-access")


if __name__ == "__main__":
    main()