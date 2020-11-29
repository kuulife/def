import  random
print('this is the sort list program:\n')

li = [random.randint(0,i) for i in range(20)]
print(f'original list: {li}\n')


def set(n): #function to remove all the duplicated numbers
	newlist = []
	for i in n:
		if i not in newlist:
			newlist.append(i)
	return newlist

def sort(n):
	newlist = []
	while n:
		initial = n[0]
		for i in n:
			if i < initial:
				initial = i
		newlist.append(initial)
		n.remove(initial)
	result = set(newlist) #remove all the duplicated numbers in the list
	return f'sorted list: {result}' # return f'sorted list: {result[::-1]}' #sort by descending order

print(sort(li))