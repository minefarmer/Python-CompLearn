'''             PYTHON EXCEPTIONS(errors)
Exceptions are errors that occur during the execution of a program.
They can break my code and force my programs to stop working.

>>> 7/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> Print("HI
  File "<stdin>", line 1
    Print("HI
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> Print("HI")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>>




#               HANDLING EXCEPTIONS ***********************************************************
It's a good practice to specify how your program handles exceptions when they occur.
However Python has its own built-in methods.

Errors can be handled or caught by embedding my own code in try and except statement blocks.
    What that means is that when I write my code, the code, the part, the block of code that I'm trying to check for errors, I can wrap it in a try block.
And for every try block, there will be at least one except block in the code I want to check for errors.
The code inside the except block will contain the handler of how to handle that error.
When it is caught,there must be at least one accept block or clause for every try block
I can add as many try and except block as I need.
The handlers for the specific errors are placed inside the except block.
The default Python handler is called if no handler is specified.



#               KEYWORDS USED IN HANDLING EXCEPTIONS  ************************************
The first is called a try block.    Lets me test a block of code for errors.
except block: Lets me specify how to handle errors.
finally block: lets me specify what code to excute regardless of what happens in a try and except block.

else block: Lets me specify what code to execute if there's no error. This is optionally used.



#               SYNTAX FOR HANDLING EXCEPTIONS
try:
    code to test for errors

except:
    code to execute to handle errors

finally:
    code to execute regardless of errors.

else:
    code to execute if there are no errors



'''

