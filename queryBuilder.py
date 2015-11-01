import StringParser as strpar

def funcQueryBuilder(formParameter):
	queryStr=strpar.parseOfString(formParameter.lower())
	print queryStr
	finQuery="Select * from Hotels where HotelId in (select hotelid from Hotels)"

	list=queryStr.split(" ")

	if "in" in list:
		place=list[list.index("in")+1]
		print place
		finQuery=finQuery+" and city like "+"'"+ place+"%"+"'"

	if "with" in list:
		yesfaci=list[list.index("with")+1]
		finQuery=finQuery+" and "+yesfaci +"=1"
		print yesfaci

	if "without" in list:
		nofaci=list[list.index("without")+1]
		finQuery=finQuery+" and "+nofaci +"=0"
		print nofaci

	print finQuery
	return finQuery


