import random
print('find the smallest number in the given list:')

li = [i for i in range(0,20)]
#shuffle list , every shuffle makes list randomly shorted
random.shuffle(li)
print('\t\t',li)

def minn(n):
	minimum  = n[0]

	for x in n:
		if x < minimum:
			minimum = x
	return f'\t\t\t\tthe smallest number is : {minimum}'

#call function 
print(minn(li))

