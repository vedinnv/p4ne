#Корреляция между солнечной активностью и глобальным изменением климата.

from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')

sheet = wb['Data']

def getvalue(x): return x.value

col_a = map(getvalue, sheet['A'][1:])
col_c = map(getvalue, sheet['C'][1:])
col_d = map(getvalue, sheet['D'][1:])

list_a = list(col_a)
list_c = list(col_c)
list_d = list(col_d)

pyplot.plot(list_a, list_c, label="Temp")
pyplot.plot(list_a, list_d, label="Sun")

pyplot.show()


