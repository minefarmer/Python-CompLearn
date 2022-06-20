'''             BASIC EXCEPYION HANDLING   part 3








'''
# c = 12 / 0  # Traceback (most recent call last):
            # File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\errors_exceptions_handling\basic_exception_handling3.py", line 11, in <module>
            #     c = 12 / 0
            # ZeroDivisionError: division by zero


# print(x)  # Traceback (most recent call last):
            # File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\errors_exceptions_handling\basic_exception_handling3.py", line 17, in <module>
            #     print(x)
            # NameError: name 'x' is not define



# print(int("HI"))  # Traceback (most recent call last):
                # File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\errors_exceptions_handling\basic_exception_handling3.py", line 24, in <module>
                #     print(int("HI"))
                # ValueError: invalid literal for int() with base 10: 'HI'



# try:
#     n = 12/ int(input("Enter a whole number: "))  # 5.5
#     print("The value of your number is ", n)
# except ZeroDivisionError as e:  # e stands for error
#     print(e)
# except ValueError as e:
#     print(e)  #   # invalid literal for int() with base 10: '5.5'

# finally:
#     print("Hope you entered a valid number.")  # Hope you entered a valid number.
    


# try:
#     n = 12/ int(input("Enter a whole number: "))  # a
#     print("The value of your number is ", n)
# except ZeroDivisionError as e:  # e stands for error
#     print(e)
# except ValueError as e:
#     print(e)  #   # invalid literal for int() with base 10: 'a'

# finally:
#     print("Hope you entered a valid number.")  # Hope you entered a valid number.



try:
    n = 12/ int(input("Enter a whole number: "))  # 8
    print("The value of your number is ", n)  # 1.5
except ZeroDivisionError as e:  # e stands for error
    print(e)
except ValueError as e:
    print(e)

finally:
    print("Hope you entered a valid number.")  # Hope you entered a valid number.

