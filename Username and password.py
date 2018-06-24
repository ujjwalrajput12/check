userName = input("Hello! Welcome to Python! \n\nUsername: ")
password = input("Password: ")
count = 0
count += 1
while userName == userName and password == password:
	if count == 1:
		print("\nYou are login Successfully. Welcome")
		break
	elif userName == 'elmo' and password == 'blue':
		print("Your Username and Password is right!")
		userName = input("\n\nUsername: ")
		password = input("Password: ")
		count += 1
		continue
	elif userName == userName and password == password:
	        print("Your Password is wrong!")
	        userName = input("\n\nUsername: ")
	        password = input("Password: ")
	        count += 1
	        continue
