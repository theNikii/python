from datetime import datetime as dt


#The Moscow Times - Wednesday, October 2, 2002
date1 = dt.strptime('Wednesday, October 2, 2002','%A, %B %d, %Y')
#The Guardian - Friday, 11.10.13
date2 = dt.strptime('Friday, 11.10.13','%A, %d.%m.%y')
#Daily News - Thursday, 18 August 1977
date3 = dt.strptime('Thursday, 18 August 1977','%A, %d %B %Y')

print(date1)
print(date2)
print(date3)