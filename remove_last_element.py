#[1,2,3] -> [1,2]
#[4,99,10] -> [4,99]
#[10,11,20] -> [10,11]

#1st case
def fd(x):
	return [1,2]

#1st and 2nd case
def fd(x):
	if	x == [1,2,3]:
		return [1,2]
	elif x == [4,99,10]:
		return [4,99]

#1st, 2nd and 3rd case
def fd(x):
	if	x == [1,2,3]:
		return [1,2]
	elif x == [4,99,10]:
		return [4,99]
	elif x == [10,11,20]:
		return [10,11]

#relation between the cases
def remove_last_element(x):
	del x[-1] #faster
	return x
print(remove_last_element([1,2,3]))

def remove_last_element(x):
	return x[: -1]
print(remove_last_element([1,6,9,0]))

def remove_last_element(x):
	x.pop()
	return x
print(remove_last_element([1,6,9,0]))
