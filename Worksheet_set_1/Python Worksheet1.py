#!/usr/bin/env python
# coding: utf-8

# In[1]:


#11. Write a python program to find the factorial of a number

num=int(input('Enter the number: '))

factorial =1
if num<0:
    print("Factorial for the number does not exist")
elif num==0:
    print("Factorial for 0 is 1")
else:
    for i in range(1, num+1):
        factorial = factorial*i
print('Factorial for', num, 'is', factorial)


# In[ ]:


#12. Write a python program to find whether a number is prime or composite
num= int(input("Enter the number:"))

if num==0|1:
    print(num, 'is neither prime nor composite')
elif num>1:
    for i in range(2, num):
        if (num%i)==0:
            print(num, 'is not a prime number')
            break
        else:
            print(num, 'is a composite number')
            break


# In[3]:


#13. Write a python program to check whether a given string is palindrome or not
def palindrome(str):
    if (str==str[::-1]):
        print(str, 'is a palindrome string')
    else:
        print(str, 'is not palindrome')
        
palindrome("ram")
    


# In[ ]:


#14. Write a Python program to get the third side of right-angled triangle from two given sides.

side1= int(input('Enter side1: '))
side2= int(input('Enter side2: '))

hypotenuse=((side1)**2+(side2)**2)**(1/2)
print ('Hypotenuse is', hypotenuse)


# In[ ]:


#15 Write a python program to print the frequency of each of the characters present in a given string
string=str(input('Enter the string: '))
character= str(input('Enter the character whose frequency you want to find out: '))
count = 0
for i in range(len(string)):
    if string[i] == character:
        count =count+1
print('Frequency of', character, 'in', string, 'is', count)
    


# In[ ]:





# In[ ]:




