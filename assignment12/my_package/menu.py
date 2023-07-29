class Menu:
    @staticmethod
    def display():
        print("1. Login")
        print("2. Register")
        print("3. Exit")

    @staticmethod
    def get_choice():
        return int(input("Enter your choice: "))
