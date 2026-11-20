class Student():
    def __init__(self,name):
        self.name = name
    def display(self):
        print(self.name)
    def __del__(self):
        print("Destructor called Here!......")
s1 = Student('Amit')
s1.display()
s2 = Student('ABC')
del s2
s3 = Student('John')
s3.display()
