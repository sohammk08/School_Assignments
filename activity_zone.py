#Program to check for buzz numbers.

usr = int(input("Enter the number: "))

if usr % 7 == 0:
	print(usr, "Is a buzz number because it is divisible by 7.")

elif int(repr(usr)[-1]) == 7:
	print(usr, "ends with 7 and so, is a buzz number.")

elif usr % 10 == 7:
	print(usr, True)

else:
	print(usr, "Is not a buzz number because it neither ends with 7 nor is divisible by 7.")