# Assignment 1
# 
# Robert Garza, Jheovanny Camacho, Robert Hovanesian
# 03-05-2019

def pascals(row):
	nCk = lambda n, r: fact(n) / (fact(r) * fact(n-r))
	result = []
	for i in range(row):
		lines = []
		for num in range(i + 1):
			lines.append(nCk(i, num))
		result.append(lines)
	spaces = row-1
	for rows in result:
		for i in range(spaces):
			print(' ', end=' ')
		spaces -= 1
		for num in rows:
			print(int(num),' ',end=' ')
		print()

def fact(n):
    if n == 0:
        return 1
    elif n > 0:
        return n * fact(n-1)

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

user_input = ''

while user_input != 'q':
	user_input = input()
	if user_input == 'a':
		h = -1
		while h < 0:
			h = int(input('Enter triangle height as a non-negative number'))
		pascals(h)
	elif user_input == 'b':
		f = -1
		while f < 0:
			f = int(input('Enter a non-negative number:'))
		print(fact(f))
	elif user_input == 'c':
		euler()
	elif user_input == 'd':
		sin_of_x()
	elif user_input == 'm':
		display_menu()
