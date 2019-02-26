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
	euler_num = 0
	sequence = 0
	next_term = 1 / fact(sequence)
	while  next_term > 10e-10:
		euler_num += next_term
		sequence += 1
		next_term = 1/fact(sequence)
	return euler_num

def absolute_value(num):
	if num < 0:
		return num * (-1)
	return num

def sin_of_x(x):
	sin_x = 0
	n = 0
	next_term = (((-1)**n)*(x**(2*n + 1)))/ fact((2*n + 1))
	while absolute_value(next_term) > 10e-8:
		sin_x += next_term
		n += 1
		next_term = (((-1)**n)*(x**(2*n + 1)))/ fact((2*n + 1))
	return sin_x

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
		row = -1
		while row < 0:
			row = int(input('Enter triangle height as a non-negative number: '))
		pascals(row)
	elif user_input == 'b':
		n = -1
		while n < 0:
			n = int(input('Enter a non-negative number: '))
		print(fact(n))
	elif user_input == 'c':
		print(euler())
	elif user_input == 'd':
		x = int(input('Enter X in radians: '))
		print(sin_of_x(x))
	elif user_input == 'm':
		display_menu()
