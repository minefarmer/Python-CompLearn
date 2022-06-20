'''             IMPLEMENTING BASIC EXCEPTION HANDLING  part: 1








'''
# print(x)  # Traceback (most recent call last):
        # File "c:\Users\pgold\MatHub\Python-CompLearn\my_notes\errors_exceptions_handling\basic_exception_handling1.py", line 11, in <module>
        #     print(x)
        # NameError: name 'x' is not defined



# try:
#     print(x)
# except:
#     print('Variable is not defined')  # Variable is not defined



# try:
#     print(x)
# except:
#     print('Variable is not defined')  # Variable is not defined
# else:
#     print("Hello")
    


# x = 20
# try:
#     print(x)  # 20
# except:
#     print('Variable is not defined')
# else:
#     print("Hello")  # Hello



x = 20
try:
    print(x)  # 20
except:
    print('Variable is not defined')
else:
    print("Hello")  # Hello

finally:
    print("I may get an error if no variabl is specified.")  # I may get an error if no variabl is specified.
