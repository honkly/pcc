class User():
    """docstring for User"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print("Hello! " + self.first_name.title() + ' ' + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print("Login attempts are " + str(self.login_attempts))

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)

class Admin(User):
    """9-8权限"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()