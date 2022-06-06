'''             VARARGS PARAMETERS
Let me define variable number of arguments for a function.
They are identified by using the * symbol.

All positional arguments are going to be a tuple when an argument




'''
def total_numbers(a=7, *numbers,**phonebook):  # All the keyword argument after the (**) To the end are allocated to a dictionary.
    print("My fav number is ", a)  # My fav number is  7

    for num in numbers:
        print("num", num)   # num 1
                            # num 2
                            # num 3

    for name,phone_number in phonebook.items():  # phone_number is no longer used!
        print(name,phone_number)
    
total_numbers(7,1,2,3,Jane=2222,John=4444,Angela=5555)  # Jane 2222
                                                        # John 4444
                                                        # Angela 5555

# When a function is called the names supplied will be assigned a phone number.
