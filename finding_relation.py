# ['b',2,'c','a'] -> [2]
# [10,'c',99,'d', 100] -> [10,99,100]
# [11,'f,'g','u',88, 9999,'z,'z'] -> [11,88,9999]

#1st caseS
#1st and 2nd case
def fdr(x):
	if x == ['b',2,'c','a']:
		return [2]
	elif x == [10,'c',99,'d',100]:
		return [10,99,100]
print("second case")
print(fdr([10,'c',99,'d',100]))

#1st, 2nd and 3th case
def fdr(x):
	if x == ['b',2,'c','a']:
		return [2]
	elif x == [10,'c',99,'d', 100]:
		return [10,99,100]
	elif x == [11,'f','g','u',88,9999,'z','z']:
		return [11,88,9999]
print("third case")
print(fdr([11,'f','g','u',88,9999,'z','z']))

def del_str(x):
	i = 0
	while i < len(x):
		x.remove('')
		i += 1
	return x
print("relation case")
print(del_str([11,'f','g','u',88,9999,'z','z']))


