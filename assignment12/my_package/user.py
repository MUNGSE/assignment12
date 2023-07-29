class User:
    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"Username: {self.username}, Email: {self.email}"
