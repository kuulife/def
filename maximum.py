import random

print('find the largest number in the list:')

li = [random.randint(0,i) for i in range(100)] #li contains random numbers between 0,100
print(li)  #printing list to verify our code is working correct

def maxx(n): #defing function to find the largest number
	maximum = n[0]
	for i in n:
		new_list = []
		if i > maximum:
			maximum = i
	return f'the largest number is : {maximum}'

print(maxx(li))