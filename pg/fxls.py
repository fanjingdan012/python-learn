from mmap import mmap, ACCESS_READ
from xlrd import open_workbook,XL_CELL_TEXT

testxls = './SwClass.xlsx'

#print(open_workbook(testxls))

with open(testxls, 'rb') as f:
	book = open_workbook(testxls)
 	#print(open_workbook(file_contents=mmap(f.fileno(),0,access=ACCESS_READ)))
	#sheet = book.sheet_by_index(0)
	for s in book.sheets():
		print ('Sheet:',s.name)
		for i in range(s.nrows):
			print( s.cell_value(i, 1))


		# 	values = []
		# 	for col in range(s.ncols):
		# 		values.append(s.cell(row,col).value)
		# 	print (','.join(str(values)))


		# cell = sheet.cell(0,0)

		# print(cell)
		# print(cell.value)
		# print(cell.ctype==XL_CELL_TEXT)
