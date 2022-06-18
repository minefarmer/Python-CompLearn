'''                             FORMATTING DATE AND TIME  part 1
The datetime object has a method for formating date objects into readable strings. It is called strftime()
The method takes one parameter, which is the format, and that is used to specify the type of formating that I want the returning string to have.

        FORMATING DATE
Directive   Discription                 Example
%a          Weekday short version       Mon
%A          Weekday full version        Monday
%w    Weekday index numbers 0-6: Mon is index 0   0
%d          Day of the month:01 - 31    17  
%b          Month name short version    Dec  
%B          Month name full version     April  
%m          Month as a number: 1 - 12   12
%y          Year short version, without century 22
%Y          Year full version, with century  2022



        FORMATING TIME
Directive   Discription                                         Example
%H          Hour:00-23                                          18 
%I          Hour:00-12                                          07 
%p          AM | PM                                             AM   
%M          Minute : 00 - 59                                    47    
%S          Seconds: 00 - 59                                    07  
%f          Microsecond: 000000 - 999999                        656789  
%z          UTC offset                                          + 0100  
%Z          Timezone                                            CST
%J          Day number of year : 001 -36                        365 
%U          Week number of year. Sunday as first day of week. 00-53     52
%W          Week number of year. Monday as first day of week. 00-53     52   
%c          Local version of date and time                      Mon Apr 8 13:05:00 2022 
%x          Local version of date                               04|8|22
%X          Local version of time                               14:20:00  
%%          A % character                                       %


                        FORMATTING DATE AND TIME  part 2  **********************************************

'''
from datetime import date
from datetime import time
from datetime import datetime

today = datetime.now()

print(today)  # 2022-06-12 17:44:21.448505

print(today.strftime("the current year is: %Y"))  # the current year is: 2022

print(today.strftime("%a, %d, %B, %y"))  # Sun, 12, June, 22








'''             FORMATTING DATE AND TIME  part 3  **********************************************'''
today = datetime.now()

print(today.strftime("%c"))  # Sun Jun 12 18:04:45 2022
print(today.strftime("%x"))  # 06/12/22
print(today.strftime("%X"))  # 18:07:43
print(today.strftime("%I:%M:%S %p"))  # 06:12:20 PM
print(today.strftime("%I:%M"))  # 06:16


