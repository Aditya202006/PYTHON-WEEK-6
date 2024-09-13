# write a python program to find the length of the string without using the len() method \

input_string= input("Enter a string :")
count = 0
for i in input_string:
   count += i
print("Length of the string is ",count)

'''
output:
Enter a string :python
Length of the string is 6
