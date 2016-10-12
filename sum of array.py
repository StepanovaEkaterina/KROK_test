count = int(input())
num_list = list(map(int, input().split(" ")))
result = []

if len(num_list) == count:
	next = 1
	for each in range(1,count+1):
		result.insert(0,next)
		next = num_list[next-1]
	print (' '.join([str(x) for x in result]))
else:
	print('Input error')