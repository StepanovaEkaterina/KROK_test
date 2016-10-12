count = 10
ships = [1,2,3,4]
while count >= 0:
	temp = 0
	str = input()
	for each in str:
		if each == 'X':
			temp += 1
		if temp > 0 and each == '.':
			ships[temp-1] -= 1;
		elif temp>4:
			print ('NO')
			return 
	for each in ships:
		if each < 0:
			print ('NO')
			return	
			