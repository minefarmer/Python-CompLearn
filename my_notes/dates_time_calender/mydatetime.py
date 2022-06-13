'''                     Working with Date and Time  part 1
Python has a module called (date time)

!!!!! I need to make sure that my file names are different from the names of modules





'''
from datetime import date
from datetime import time
from datetime import datetime

today = date.today()

# print("Today is ", today)  # Today is  2022-06-12

# print("The date components are ", today)  # The date components are  2022-06-12

# print("The date components are ", today.day,today.month,today.year)  # The date components are  12 6 2022







                    #  Working with Date and Time  part 2  ******************************************************

# print("The weekday number is", today.weekday())  # The weekday number is 6

# days = ["mon","tues","wed","thu","fri","sat","sun"]
# print("the weekday is", days[today.weekday()])  # the weekday is sun






                    #  Working with Date and Time  part 3  ******************************************************



today = datetime.now()

print("The current time is ", today)  # The current time is  2022-06-12 16:33:14.638037

t = datetime.time(datetime.now())
print("The time now is ", t)  # The time now is  16:36:48.320314

