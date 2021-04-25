log='128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"'

address=log.split()
address=address[0]

date=log
table=str.maketrans('[]', '  ')
date=date.translate(table)
date=date.split()
date=date[3]+date[4]

print(address)
print(date)