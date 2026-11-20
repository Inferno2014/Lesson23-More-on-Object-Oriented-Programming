class Daily_message():
    def __init__(self):
        self.message = ""
    def get_message(self):
        self.message = input("Enter today's message: ")
    def print_message(self):
        print("Message in uppercase:", self.message.upper())
daily_text = Daily_message()
daily_text.get_message()
daily_text.print_message()
class Helper_session():
    def __init__(self):
        print("Daily Data Helper session created")
    def __del__(self):
        print("Daily Data Helper session ended")
def create_session():
    print("Making helper session...")
    session = Helper_session()
    print("Session is ready...")
    return session
print("")
print("Calling create_session() function...")
session_obj = create_session()
print("Program is still running...")
del session_obj
print("Program End")