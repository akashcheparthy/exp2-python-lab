#!/usr/bin/env python
# coding: utf-8

# In[26]:


#1.Write a program to accept floating point number from keyboard 
x=float(input("enter number:"))
print(x)


# In[28]:


#2Write a program to convert distance in kilometer to meter or centimeter. Your program should read distance in kilometer and then ask for choice of conversion, 1 for converting to meter and 2 for converting to centimeter and display accurate conversion. Test your program for both conversion. 

kilometer=float(input("enter kilo meter:"))
conversion=input("press 1 to convert in meter \n press 2 to covert in centimeter \n enter a number 1 or 2:")
if conversion=='1':
    print(kilometer*1000 ,"m")
elif conversion=='2':
    print(kilometer*1000*100 ,"cm")
else:
    print("invalid input")


# In[7]:


#3.Program to display day of a week by reading number from 1-7. 
day=input("enter a number to know the day:")
if day=="1":
    print("monday")
elif day=="2":
    print("tuesday")
elif day=="3":
    print("wednesday")
elif day=="4":
    print("thursday")
elif day=="5":
    print("friday")
elif day=="6":
    print("saturday")
elif day=="7":
    print("sunday")
else:
    print("invalid input")
 


# In[9]:


#4.Write a python program to display number from 1 to 10 [using while loop] 
i=1
while i<=10:
    print(i)
    i=i+1


# In[13]:


#Write a python program to display number from 1 to 10 [using for loop]
for i in range(1,11):
    print(i)


# In[16]:


#Write a python program to display odd number between 100 and 200.
for i in range(100,200):
    if i%2 !=0:
        print(i)


# In[17]:


#Write a program to work with range and display range.
for i in range(1,11):
    print(i)


# In[19]:


#Write a program to find factorial of a number. 
factorial=1
x=int(input("enter a number:"))
for i in range(1,x+1):
    factorial=factorial*i
print(factorial)
    
    


# In[23]:


#Write a program to display following pattern 
for i in range(1,6):
    print(i*"*",end="\n")


# In[21]:


print(5*"hello")


# In[ ]:




