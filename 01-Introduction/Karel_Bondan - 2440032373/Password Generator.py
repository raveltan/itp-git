# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 14:43:59 2020

@author: karel
"""

import random
a = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
punctuations = "~`@$%^&*()-_=+[{}]\|;:?/.>,<#"
total = alphabets + punctuations
total = list(total)
c = 0
password = []
aaa = len(total)
    
print('')
print("                   ---Simple Password Generator---")
print('')
print("Welcome! This simple program will generate a random strong password for you.")
print("How long would your password be?")
t = eval(input("Enter a number (Min is 6 characters, max is 20 characters, Recommended is 10 characters): ", ))
y = False

while (c<=t-1):
    if (t<6):
        print("Too short! Password length must be between 6 and 20 characters!")
        tt = input("Do you want to try again? Yes or No (Case sensitive): ",)
        if (tt=='Yes'):
            t = eval(input("Enter a number (Min is 6 characters, max is 20 characters, Recommended is 10 characters): ", ))
            if(t>20):
                print("Too long! Password length must be between 6 and 20 characters!")
            if (t<6):
                print("Too short! Password length must be between 6 and 20 characters!")
            elif(6<=t<=20):
                a = random.randint(0,aaa)
                aa = total[a]
                total.pop(a)
                password.append(aa)
                c+=1
                y = True
                aaa = len(total)-1
                if (c==t-1):
                    break
        else:
            print("\nThank you for using our service!")
            break
    if(t>20):
        print("Too long! Password length must be between 6 and 20 characters!")
        tt = input("Do you want to try again? Yes or No (Case sensitive): ",)
        if (tt=='Yes'):
            t = eval(input("Enter a number (Min is 6 characters, max is 20 characters, Recommended is 10 characters): ", ))
            if(t>20):
                print("Too long! Password length must be between 6 and 20 characters!")
            if (t<6):
                print("Too short! Password length must be between 6 and 20 characters!")
            elif(6<=t<=20):
                a = random.randint(0,aaa)
                aa = total[a]
                total.pop(a)
                password.append(aa)
                c+=1
                y = True
                aaa = len(total)-1
                if (c==t-1):
                    break
        else:
            print("\nThank you for using our service!")
            break
    elif(6<=t<=20):
        a = random.randint(0,aaa)
        aa = total[a]
        total.pop(a)
        password.append(aa)
        c+=1
        y = True
        aaa = len(total)-1

if (y==True):
    print("")
    print("Your password is:")
    for i in password:
        print(i, end='')
    print("\n\nThank you for using our service!")