class Employee():
    def __init__(self,login_status):
        self.login_status = login_status
    def display(self):
        print(self.login_status)
    def __del__(self):
        print('Logged Off!')
login = Employee('Logged In!')
login.display()