#1.Create three cariables in a single line with different values and data types
a,b,c = 7,3.2,"python"
print (a,b,c)

#2.Create 2 variables,assign one complex and other with integer and swap it.
a = 2
b = 3+4j
z = b
a = b
b = z
print(b)

#3.Swap 2 numbers using 3rd
a = 2
b = 3
z = b
a = b
b = z
print(b)

#3.1 Swap 2 numbers without 3rd
x = 3
y = 2
x = x * y
y = x / y
x = x / y
print(x)

#4 Write a program to print the value given by the user by using both Python 2.x and Python 3.x Version.
value = input("enter the value")
print (value)

#5.Write a program to complete the task given below:
#Ask the user to enter any 2 numbers in between 1-10 and add both of them to another variable call z.
#Use z for adding 30 into it and print the final result by using variable results
first = (int(input("Enter your no from 1 -10: ")))
Second = (int(input("Enter your no from 1 -10: ")))
print(int(first + Second + 30))

#6.Write a program to check the data type of the entered values. HINT: Printed output should say -  The input value data type is: int/float/string/etc
x = eval(input("Enter you value: "))
print(type(x))

#7.If one data type value is assigned to ‘a’ variable and then a different data type value is assigned to ‘a’ again. Will it change the value
# Solution : Yes the value will change because the string will overwirte the in int below
a = 3
a = "python"
print(a)
