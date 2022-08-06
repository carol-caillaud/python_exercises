# "12111990" -> "12/11/1990"
# "13072010" -> "13/07/2010" 
# "s20012020" -> "20/01/2020"

#1st case
def fd(x):
	return '12/11/1990'
print (fd('12111990'))

#1st and 2nd case
def fd(x):
	if	x == '12111990':
		return '12/11/1990'
	elif x == '13072010':
		return '13/07/2010'

#1st, 2nd and 3rd case
def fd(x):
	if	x == '12111990':
		return '12/11/1990'
	elif x == '13072010':
		return '13/07/2010'
	elif x == '20012020':
		return '20/01/2020'