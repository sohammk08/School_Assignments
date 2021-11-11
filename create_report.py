
Name = input("Enter your name: ")
roll_no = int(input("Enter your roll number: "))
english = int(input("Enter your marks in English: "))
hindi = int(input("Enter your marks in Hindi: "))
maths = int(input("Enter your marks in Mathematics: "))
science = int(input("Enter your marks in Science: "))
computer = int(input("Enter your marks in Computer: "))

Total_marks = english + hindi + maths + science + computer
Total_percentage = int(Total_marks * 100 / 500)

print()
print(Name, ",")
print("Roll no: ", roll_no)
print("Your total marks are: ", Total_marks)
print("Your percentage is: ", Total_percentage, "%")