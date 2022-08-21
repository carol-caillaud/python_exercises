# "12111990" -> "12/11/1990"
# "13072010" -> "13/07/2010" 
# "20012020" -> "20/01/2020"

#relation between the cases 
def date_format(x):
	return f"{x[0:2]}/{x[2:4]}/{x[4:8]}"
print(date_format("20012020"))
	


