from xlutils.copy import copy # http://pypi.python.org/pypi/xlutils
from xlrd import open_workbook # http://pypi.python.org/pypi/xlrd
import open_bugs_in_project
import report_data


wb = copy(open_workbook('test.xlsx'))

def write_bug_count_in_sprint():
    w_sheet = wb.get_sheet(0)

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

    wb.save('test.xlsx')


def write_stories_passed_by_qa():

    w_sheet = wb.get_sheet(1)

    results = open_bugs_in_project.open_bugs_list()

    for index, result in enumerate(results):
        for column_index in range(0, 2):
            w_sheet.write(index, column_index, result[column_index])

    wb.save('test.xlsx')


def write_open_bugs_in_project():

    w_sheet = wb.get_sheet(2)

    results = report_data.open_bugs_list()

    for index, result in enumerate(results):
        for column_index in range(0, 6):
            w_sheet.write(index, column_index, result[column_index])

    wb.save('test.xlsx')