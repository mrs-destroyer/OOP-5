# Calendar Module
import calendar
print(calendar.calendar(2024))


# OS module
import os
print(os)


# Python Urllib Module
import webbrowser
url = input("Enter your URL here : ")
print("wait..") 
webbrowser.open(url)


# pprint
import pprint
date = {
    "Name" : "Asad" ,
    "Age" : "25" ,
    "Address" : "Lahore"
}
p = pprint.PrettyPrinter(width = 1) # if we can't it put here 
p.pprint(date) # and here put pprint.pprint(date) its prints on one line.


# Timit function
import timeit
print(timeit.timeit(stmt = "x = 0" , setup = " " , number = 10))
print(timeit.timeit(stmt = "while x < 10 : x += 1" , setup = "x = 0" , number = 1))
print(timeit.timeit(stmt = "for x in range(10): pass" , setup = " " , number = 1))


# Import module
def add(num1 , num2):
    print(num1+num2)

import add
