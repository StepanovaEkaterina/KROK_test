depth = 0
result = []
str = ''
while True:
	try:
		str = input()
	except EOFError:
		break
	str = str.strip()
	if str.startswith('}') and depth > 0:
		depth -= 4
	if str != "":
		result.append(' ' * depth + str)
	else:
		result.append(str)
	if str.endswith('{'):
		depth += 4
	
	
for each in result:
	print (each)