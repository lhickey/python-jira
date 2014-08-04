from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
import xlwt
from xlwt import Workbook


wb = xlwt.Workbook()
wb_name = 'Sprint report data.xls'
# wb = copy(open_workbook('report_data.xlsx'))

def write_bug_count_in_sprint(report_data):
    w_sheet = wb.add_sheet("bug breakdown")
    # w_sheet = wb.get_sheet(0)

    w_sheet.write(0, 0, "Blocker")
    w_sheet.write(1, 0, "Critical")
    w_sheet.write(2, 0, "Major")
    w_sheet.write(3, 0, "Minor")
    w_sheet.write(4, 0, "Trivial")
    w_sheet.write(0, 1, report_data.blocker_bugs_in_sprint())
    w_sheet.write(1, 1, report_data.critical_bugs_in_sprint())
    w_sheet.write(2, 1, report_data.major_bugs_in_sprint())
    w_sheet.write(3, 1, report_data.minor_bugs_in_sprint())
    w_sheet.write(4, 1, report_data.trivial_bugs_in_sprint())

    w_sheet.write(6, 0, "Bugs Opened in Sprint")
    w_sheet.write(6, 1, report_data.bugs_opened_in_sprint())
    w_sheet.write(7, 0, "Bugs Fixed in Sprint")
    w_sheet.write(7, 1, report_data.bugs_fixed_in_sprint())

    wb.save(wb_name)


def write_stories_passed_by_qa(report_data):

    # w_sheet = wb.get_sheet(1)
    w_sheet = wb.add_sheet("stories passed by qa")
    results = report_data.open_bugs_list()

    for index, result in enumerate(results):
        for column_index in range(0, 2):
            w_sheet.write(index, column_index, result[column_index])

    wb.save(wb_name)


def write_open_bugs_in_project(report_data):

    # w_sheet = wb.get_sheet(2)
    w_sheet = wb.add_sheet("Open bugs in project")
    results = report_data.open_bugs_list()

    for index, result in enumerate(results):
        for column_index in range(0, 6):
            w_sheet.write(index, column_index, result[column_index])

    wb.save(wb_name)