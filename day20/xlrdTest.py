import xlrd

from datetime import date,datetime

file = 'test.xls'

def read_excel():

	wb = xlrd.open_workbook(filename=file)#打开文件

	print(wb.sheet_names())#获取所有表格名字

	sheet1 = wb.sheet_by_index(0)#通过索引获取表格

	# sheet2 = wb.sheet_by_name('年级')#通过名字获取表格

	print(sheet1)

	print(sheet1.name,sheet1.nrows,sheet1.ncols)

	rows = sheet1.row_values(2)#获取行内容

	cols = sheet1.col_values(3) #获取列内容
	print(rows)
	print(cols)

	print(sheet1.cell(1,0).value)#获取表格里的内容，四种方式

	print(sheet1.cell_value(1, 0))

	print(sheet1.row(1)[0].value)

	print(sheet1.cell(1, 0).ctype) # python读取excel中单元格的内容返回的有5种类型，即上面例子中的ctype:ctype :  0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
	print("-------------")
	merge = []
	print(sheet1.merged_cells)
	for (rlow,rhigh,clow,chigh) in sheet1.merged_cells:
		merge.append([rlow,clow])
	for index in merge:
		print(sheet1.cell_value(index[0],index[1]))
	# xlrd.xldate_as_tuple(sheet1.cell_value(1, 2), wb.datemode)
if __name__ == '__main__':
    read_excel()
