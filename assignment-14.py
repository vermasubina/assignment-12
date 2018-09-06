#Python Advanced Topics
#Q.1- Write a python program to print the cube of each value of a list using list comprehension.
a=[1,2,3,4]
lst = [ a[i]**3 for i in range(0,4)]
print(lst)


#Q.2- Write a python program to get all the prime numbers in a specific range using list comprehension.
lst= [x for x in range(2,500) if not [y for y in range(2,x) if x%y ==0]]
print(lst)


#Q.3- Write the main differences between List Comprehension and Generator Expression.
'''A List Comprehension,executes immediately and returns a list.
A Generator Expression,returns and object that can be iterated over.
The difference between the two kinds of expressions is that the List comprehension is enclosed in square brackets []
while the Generator expression is enclosed in plain parentheses ().
l = [n*2 for n in range(1000)] # List comprehension
g = (n*2 for n in range(1000))  # Generator expression'''


#LAMBDA & MAP
#Q.1- Celsius = [39.2, 36.5, 37.3, 37.8] Convert this python list to Fahrenheit using map and lambda expression.
def double(c):
    return ((9/5)*c)+32

Celsius = [39.2, 36.5, 37.3, 37.8]
d = list(map(double, Celsius))
print(d)


#Q.2- Apply an anonymous function to square all the elements of a list using map and lambda.
lst = [1,2,3,4,5]
d = list(map(lambda x : x**2, lst))
print(d)


#FILTER & REDUCE
#Q.1- Filter out all the primes from a list.
prime=[2,3,6,7,10]
def isPrime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True

f = list(filter(isPrime,prime))
print(f)


#Q.2- Write a python program to multiply all the elements of a list using reduce.
from functools import *
l = [1, 2, 3, 4, 5]
a = reduce(lambda x,y : x*y, l)
print(a)
