#find the relatiton between the the cases then write a function
# "a" -> "A"
# "b" -> "B"
# "c" -> "C"

#1st case
def fdr(x):
	return "A"

#1st and 2nd case
def fdr(x):
	if x == "a":
		return "A"
	elif x == "b":
		return "B"

#1st, 2nd and 3th case
def fdr(x):
	if x == "a":
		return "A"
	elif x == "b":
		return "B"
	elif x == "c":
		return "C"

#relation between the cases
def upper_case(x):
	return x.upper()
print(upper_case("h"))
