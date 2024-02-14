# 01. Write a Python script to sort (ascending and descending) a dictionary by value.
numbers1 = {
    1:10,
    2:90,
    3:70,
    5:80,
    6:40,
    7:25, 
    8:50, 
    4:110,
    9:35
}
number1 = numbers1.values()
ascendingValue = sorted(number1)
print(ascendingValue)
descendingValue = sorted(number1 , reverse = True)
print(descendingValue)

# 02. Write a Python script to add a key to a dictionary.
students = { "name" : "safiq",
             "roll": 32,
             "class": "seven" }
print(students)
students["section"] = "A"
print(students)

# 03. Write a Python script to check whether a given key already exists in a dictionary.
student1 = { "name" : "safiq",
             "roll": 32,
             "class": "seven" }
if "name" in student1:
    print("the key already in dictionary")
else:
    print("the key not in dictionary")

# 04. Write a Python program to sum all the items in a dictionary.
numbers = {
    1:10,
    2:90,
    3:70,
    4:110,
    5:80,
    6:40,
    7:25, 
    8:50, 
    9:35
}
number = numbers.values()
print(number)
sum = 0
for num in number:
    sum = sum+num
print("the sum of values is : ", sum)