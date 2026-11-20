class Upper():
    def __init__(self,string):
        self.string = string
    def display(self):
        print(self.string.upper())
    def __del__(self):
        print('Destructor called!')
s1 = Upper('party')
s1.display()
s2 = Upper('balloon')
del s2
s3 = Upper('clown')
s3.display()