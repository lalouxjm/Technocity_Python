##MY_FUNC
import re
import math
import datetime


#Turn the string red
def red(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;31m{value}{value2}{value3}{value4}{value5}\033[0m"
#Turn the string green
def green(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;32m{value}{value2}{value3}{value4}{value5}\033[0m"
#Turn the string blue
def blue(value: str, value2="", value3="", value4="", value5="") -> str:
    return f"\033[1;34m{value}{value2}{value3}{value4}{value5}\033[0m"
# x*2
def double(value: int) -> int:
    return value * 2
# x/2
def half(value: float) -> float:
    return value / 2
# x²
def expose(value: int) -> int:
    return pow(value,2)

#Factorial
#Multiply 1*2*3*4*5
def factorial(num: int) -> int:
    result = 1
    for i in range(1,num+1):
        result *= i
    return result

#Reverse a string hello -> olleh
def reverse(value: str) -> str:
    return value[::-1]

#Snake_Case
def snake_case(value: str) -> str:
    n = value.lower()
    words = n.split(" ")
    return "_".join(words)

#Find the longest word in a sentence
def longest_word(sentence: str) -> str:
    """words = re.findall(r"[a-zA-Z]+", sentence)"""
    words = sentence.split()
    longest = ""

    for word in words:
        clean = ''.join(c for c in word if c.isalpha())
        if len(clean) > len(longest):
            longest = clean
    return longest