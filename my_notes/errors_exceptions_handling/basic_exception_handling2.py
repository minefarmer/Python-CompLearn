'''             BASIC EXCEPYION HANDLING   part 2








'''
# b = "Hello"

# print(int(b))  # Traceback (most recent call last):
                # File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\errors_exceptions_handling\basic_exception_handling2.py", line 13, in <module>
                #     print(int(b))
                # ValueError: invalid literal for int() with base 10: 'Hello'




# while True:
#     try:
#         n = int(input("Enter a whole number: "))
#         break
#     except ValueError:
#         print("No valid integer entered")  # 8.5
#                                         # No valid integer entered

# print("Great you have entered an interger")


# while True:
#     try:
#         n = int(input("Enter a whole number: "))
#         break
#     except ValueError:
#         print("No valid integer entered")  # abc
#                                         # No valid integer entered

# print("Great you have entered an interger")


while True:
    try:
        n = int(input("Enter a whole number: "))
        break
    except ValueError:
        print("No valid integer entered")  # abc
                                        # No valid integer entered

print("Great you have entered an interger")  #  8
                                            # Great you have entered an interger
        