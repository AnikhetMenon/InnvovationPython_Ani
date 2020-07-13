#Prob1
List = [1, 3 , "Anikhet", 7,"Consult", 4.4 ,2j, 8,9 10 ]

#Prob2
list1 = [0, 1 , 2 ,3 ,4 ,5  ]
print(list1[0:2],list1[::-1],list1[::2])

#Prob3
add = 0
mul = 1
for i in list(range(1,7)):
    add += i
    mul *=i
print("the addition of the list is: ", add)
print("the multiplication of the list is:" ,mul)

#Prob4
list = [1,3,4,6,8,9]
print("the min integer in the list is ",min(list))
print("the max integer in the list is ",max(list))

#Prob5
list = [2,3,4,67,45,32,46,554,235]
for num in list:
    if num % 2 == 0:
        list.remove(num)
print("final list: ",list)

#Prob6
list = []
for num in range(1,31):
    list.append(num **2)
print(list[5:] + list[:25])

#Prob7
list=[[1, 3, 5, 7, 9, 10], [2, 4, 6, 8]]
print(list[0][:4]+ list[1])

#Prob8
a={1: 10, 2: 20}
b={3: 30, 4: 40}
c= {**a , **b}
print(c)

#Prob9
dict = {}
for x in range(1, 6):
    dict[x] = x * x
print(dict)

#Prob10
num = input("enter the num in list : ")
list = num.split(",")
tuple_value = tuple(list)
print(list)
print(tuple_value)