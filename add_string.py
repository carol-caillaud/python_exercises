# [1,2] -> [1,'a', 2,'a']
# [3,4,5] -> [3,'a', 4,'a',5,'a']
# [6,99,100,200] -> [6,'a', 99,'a',100,'a', 200, 'a']

#1st case
def f1(x):
	x.insert(1,'a')
	x.insert(3,'a')
	return x

print("first case")
print(f1([1,2]))

#1st and 2nd case
def f2(x):
	if x == [1,2]:
		x.insert(1,'a')
		x.insert(3,'a')
		return x
	elif x == [3,4,5]:
		x.insert(1,'a')
		x.insert(3,'a')
		x.insert(5,'a')
		return x

print("second case")
print(f2([3,4,5]))

#1st, 2nd and 3th case
def f3(x):
	if x == [1,2]:
		x.insert(1,'a')
		x.insert(3,'a')
		return x
	elif x == [3,4,5]:
		x.insert(1,'a')
		x.insert(3,'a')
		x.insert(5,'a')
		return x
	elif x == [6,99,100,200]:
		x.insert(1,'a')
		x.insert(3,'a')
		x.insert(5,'a')
		x.insert(7,'a')
		return x

print("third case")
print(f3([6,99,100,200]))

#relation between the cases
def add_string(x):
	z = 1
	i = 0
	x_len = len(x)
	while i < x_len:
		x.insert(z,'a')
		z += 2
		i += 1
	return x
print("relation case")
print(add_string([8,98,150,200]))

def add_string(x):
	r = []
	for i in x:
		r = r + [i, 'a']
	return r
print("relation case")
print(add_string([8,98,150,200]))
 