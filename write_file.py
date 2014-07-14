from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
from xlwt import easyxf # http://pypi.python.org/pypi/xlwt
import open_bugs_in_project

START_ROW = 3 # 0 based (subtract 1 from excel row number)
col_key = 0
col_summary = 1
col_priority = 2
col_severity = 3
col_status = 4
col_affects_version = 5
col_fix_version = 6

wb = copy(open_workbook('test.xlsx'))
w_sheet = wb.get_sheet(1)

results = open_bugs_in_project.open_bugs_list()

for index, result in enumerate(results):
    for column_index in range(col_key, col_fix_version):
        w_sheet.write(index + START_ROW, column_index, result[column_index])

wb.save('test.xlsx')