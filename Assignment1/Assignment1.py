# Assignment 1
# 
# Robert Garza, Jheovanny Camacho, Robert Hovanesian
# 03-05-2019

def pascals():
	return

def factorial():
	return

def euler():
	return

def sin_of_x():
	return

def display_menu():
	print('Type \'A\', \'B\', \'C\', \'D\', \'M\', \'Q\'')
	print('A. Display Pascal\'s triangle of height H.')
	print('B. Display the value of the factorial of N.')
	print('C. Approximate and display the Euler’s number.')
	print('D. Approximate and display the value of the sine of X.')
	print('M. Display these menu options.')
	print('Q. Exit from the program.')

display_menu()

user_input = input()

while user_input != 'q':
	user_input = input()
	if user_input == 'a':
		pascals()
	elif user_input == 'b':
		factorial()
	elif user_input == 'c':
		euler()
	elif user_input == 'd':
		sin_of_x()
	elif user_input == 'm':
		display_menu()
