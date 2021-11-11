#Program to determine whether a person is eligible for voting
age = int(input("Enter your age: "))
if age == 18:
	print("You are aligible for voting")
elif age >= 18:
	print("You are eligible for voting")
else:
	print("You are below 18, you are not eligible for voting!")