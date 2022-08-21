#[1,2,3] -> [2,4,4]
#[3,3,3] -> [4,5,4]
#[4,5,6,7] -> [5,7,7,8]

#import pdb; pdb.set_trace()

def t1(x):
	return [2,4,4]
print("first case")
print(t1([1,2,3]))

def t1(x):
	if x == [1,2,3]:
		return [2,4,4]
	elif x == [3,3,3]:
		return [4,5,4]
print("second case")
print(t1([1,2,3]))
print(t1([3,3,3]))

def t1(x):
	if x == [1,2,3]:
		return [2,4,4]
	elif x == [3,3,3]:
		return [4,5,4]
	elif x == [4,5,6,7]:
		return [5,7,7,8]

print("third case")
print(t1([1,2,3]))
print(t1([3,3,3]))
print(t1([4,5,6,7]))

def add(x):
	x == ()
	return  x + 5
print(add(10))
