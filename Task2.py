#Problem1
num = int(input("enter your number: "))
def number(num):
  if  num % 5 == 0 and  num % 3 == 0:
     print ("Consultadd Python training")
  elif num % 3 == 0:
     print("Consultadd")
  elif num % 5 == 0:
     print("c")
  else:
      pass
number(num)

#Problem2:
print("Calculator:")

for num in range(1,6):
    num = int(input("Enter your choice : "))
    while num <= 6:
        a= eval(input("Choose your 1st number :"))
        b = eval(input("Choose your 2nd number :"))


        if num == 1:
           print("the Addition of",a + "and ",b + " is :", a+b )
        elif  num == 2:
           print("the substraction of 1st and 2nd is :", a-b )
        elif  num == 3:
           print("the mul of 1st and 2nd  is :", a*b )
        elif num == 4:
           print("the division of 1st and 2nd  is :", a/b )
        elif num == 5:
           print("the  avg of 1st and 2nd is :", a+b/2 )
        else:
           print("Reenter")

#Problem3:
age = int(input("Enter your age: "))
if age >= 11:
    print("You are eligible to see a the Football Match")
    if age <=20 or age>=60:
        print("Ticket price is $12")
    else:
        print("Kit is 20$")
else:
    pirnt("You're not eligible to buy a tikcet")



#Problem4
num = int(input("Enter your number: " ))
while True:
    if num > 0:
        continue:
        print("Good Going")
    else:
        print("It's over")
        break

#Problem5
for num in range(2000,3201):
    if num % 7 == 0 and num/5 !=0:
        print(int(num))
    else:
        pass

#Problem6.1:
Traceback (most recent call last):

    for i in x:
TypeError: 'int' object is not iterable

#Problem6.2:
    print(“error”)
                ^
SyntaxError: invalid character in identifier

#Problem6.3
0
Traceback (most recent call last):
1
  File "C:/Users/anikh/PycharmProjects/untitled1/venv/task2meta.py", line 6, in <module>
    Break
2
NameError: name 'Break' is not defined
3
4

#Problem7
for num in range(0,7):
    if num % 3 !=0:
        print(num)
    else:
        continue

#Problem8
num = (input("Enter your input: "))
print(len(num))
for i in num:
    if i.isdigit() == True:
        print(i)
    else:
        pass

#Problem9
import random
luckynum = random.randint()
num = int(input("enter your lucky number: "))
while True:
    if num ==luckynum:
        break
    else:
        continue

#Problem10
import random
counter = 1
luckynum = random.randint(0,100)
while counter <=5:
    num = int(input("enter your lucky number: "))
    if num != luckynum:
       print("try again")
       counter +=1
    else:
        print("You are Lucky today")
        break


