# -*- coding: utf-8 -*-
"""Untitled9.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1EMjlsCjfwa13VcHPwbo53oRZyG-p6_fW
"""

# Program to check if a character is a vowel or consonant

# Take input from the user
char = input("Enter a single character: ").lower()

# Check if the input is a letter
if char.isalpha() and len(char) == 1:
    if char in 'aeiou':
        print(f"{char} is a vowel.")
    else:
        print(f"{char} is a consonant.")
else:
    print("Invalid input! Please enter a single alphabetic character.")