from my_package.menu import Menu
from my_package.authentication import Authentication
from my_package.user import User
from my_package.database import users

def main():
    while True:
        Menu.display()
        choice = Menu.get_choice()

        if choice == 1:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if Authentication.login(username, password):
                print("Login successful!")
            else:
                print("Invalid credentials!")

        elif choice == 2:
            username = input("Enter a username: ")
            password = input("Enter a password: ")
            email = input("Enter an email: ")
            user = User(username, password, email)
            users.append(user)
            print("Registration successful!")

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again!")

if __name__ == "__main__":
    main()
