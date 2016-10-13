count = 10
ships = [1,2,3,4]
field = []
positions = []
while True:
	try:
		field.append(input())
	except EOFError:
		break

def Check(field):	
	for line in range(10):
		for row in range(10):
			if field[line][row] == 'X':
				if line - 1 >= 0 and row - 1 >= 0 and field[line - 1][row - 1] == 'X':
					print ('kek')
					print ('NO')
					return 0
				elif line - 1 >= 0 and row + 1 < 10 and field[line - 1][row + 1] == 'X':
					print ('kek')
					print ('NO')
					return 0
				elif line + 1 < 10 and row - 1 >= 0 and field[line + 1][row - 1] == 'X':
					print ('kek')
					print ('NO')
					return 0
				elif line + 1 < 10 and row + 1 < 10 and field[line + 1][row + 1] == 'X':
					print ('kek')
					print ('NO')
					return 0
				else:
					return 1
print (Check(field))