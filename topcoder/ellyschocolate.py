class ellyschocolates():
	def getcount(P,K,N):
		choccount=N//P
		quotn=choccount
		totalrmnd=0
		while quotn>2:
			(quotn,rmnd) = divmod(quotn,K)
			choccount=choccount+quotn
			totalrmnd = totalrmnd + rmnd 
		quotn2 = totalrmnd//K
		return choccount+quotn2

print("Exit Print",ellyschocolates.getcount(1,3,15))
print("Exit Print",ellyschocolates.getcount(41,4,1337))
print("Exit Print",ellyschocolates.getcount(666,222,444))
