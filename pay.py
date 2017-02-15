#to calculate the split pay

def price1(itmes):
	print itmes
	result = itmes.split(' ');
	finaleresult = map(float, result)
	print finaleresult
	return finaleresult

def splitpay(user):
	items = raw_input("items price is: ")
	tax = raw_input("sell tax is: ")
	priceint = price1(items)
	totalspend = 0
	for i in priceint:
		totalspend += i
	tax = float(tax)
	tax *= totalspend
	return float(tax) + totalspend
	
while True:
	user = raw_input("name of user is: ")
	print user
	if user != '':
		print user + 'need to pay: ' + str(splitpay(user))
	else:
		break