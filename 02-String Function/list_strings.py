#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Strings and list

# PART 1 STRINGS

# Strings can we written(declared)
# in 3 different ways
sqoute = 'hello'
dquote = "hello"
multi_line = """hello guys"""

print(sqoute, dquote, multi_line)

# Cast to string
number = 10
str_num = str(number)
print(type(str_num))
print(number)

# escape character
# \b backspace
# \n newline
# \r ASCII carriage return
# \t tab

print('hello there\nhow\tare you?')

# \' single qoute
# \" double quote
print('\'hello\'')
print("\"hello\"")

name = 'mike'

# strings methods
print(name.capitalize())
print(name.upper())
print(name.lower())

# Splitting strings

data = 'Hello world from python'

print(data.split())
print(data.split()[0])

# String formating
# 2 ways:
# the prinf (old)
# .format (new)

print('Hello {}, you must be new!'.format('Ravel'))
# print(f'Hello {name}!')
print('Hello {},{}'.format('ravel', 'joko'))
# String concatenation
print('hello ' + 'world')

# string slicing
# can use the list slice notation
# [start:end:step]
print('123456'[2::2])
print('123456'[::1])
print('123456'[5::-1])
print('123456'[:4:-1])
print('123456'[4:1:-2])
print('123456'[::3])

# PART 2 LISTS

# Declaring List
normal_list = [1, 2, 3, 'helo', True, (1, 2, 3)]
print(normal_list)

list_from_string = list('abc')
print(list_from_string)

# List methods
# Method with * is uncommon to use
# append: add to end of list
# clear: remove all elements
# copy*
# count: count the occurence of an element
# extend*
# index: find the first instance of element
# insert(index,data):insert data to index
# pop: remove the last and return
# remove:delete the first instance of dataa
# reverse
# sort

# We'll take a look at
# this in the next meeting

# special keyword

# del my_list[1]

# You can add to list with + or +=

# List slicing
# [start:end:step]
