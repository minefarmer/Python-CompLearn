'''             NESTED FUNCTION ACCESSING VARIABLE SCOPE

Python allows a nested function to access the outer scope of the enclosing function.
And this concept or pattern is referred to as closure.





'''
def display_message(message):
    "hello"
    def message_sender():
        "nested function"
        print(message)
    message_sender()

display_message("Show my the money!")  # Show my the money!

