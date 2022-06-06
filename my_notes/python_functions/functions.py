'''             FUNCTIONS
    DRY
Don't repeat yourself!!!!
Functions are pieces(blocks) of code that does something.
They are reusable.
They execute or run when called by thier name.
They can have parameters(variables) and arguments(values).
Parameters are basically variables that I define inside the function parentheses.
They can have arguments. (Arguments are the actual value that you give to the function.)
They can return data as a result. 
There are built-in functions. Example print()
I can create my custom functions, which are called user defined functions.



                CREATING A FUNCTION
                
Before I create a function, it is good to think of a discriptive name that I want for my function.
Discriptive names.
Same naming rules as variables.

def function_name(parameters):  # parameters are basically variables that I define inside the function.
    print("Hello World!")

The function does nothing untill it is activated.
The process of activating the function is called calling the function.
Also known as: running, execution, involking.
I can call a function by it's name and add parenthesis.
Any parameters or arguments are placed inside the parenthesis.




                PARAMETER VS ARGUMENT

A parameter is a variable defined inside a function's parenthesis.

An argument is the actual value you pass(give) the function when it is called.

def sum(x,y):  # x and y are the parameters
    print(x + y)
    
sum(4,5)   # 9  ## 4 and 5 are the actual arguments.

'''