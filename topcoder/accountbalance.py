class AccountBalance():
	def processTransactions(startingbalance, transactions):
		totaldebit=0
		totalcredit=0
		for each in transactions:
			if each.startswith('D'): totaldebit = totaldebit + int(each.split()[1])
			if each.startswith('C'): totalcredit = totalcredit + int(each.split()[1])
		return (startingbalance + totalcredit - totaldebit)



print (AccountBalance.processTransactions(100, {"C 1000", "D 500", "D 350"}))
print (AccountBalance.processTransactions(100, {"D 50", "D 20", "D 40"}))
print (AccountBalance.processTransactions(53874, {"D 1234", "C 987", "D 2345", "C 654", "D 6789", "D 34567"})) 
