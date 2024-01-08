import re
import os
import io
import os.path
import openpyxl

path1 = os.path.dirname(os.path.abspath(__file__))
# print(path1)
excelname = 'charc.xlsx'
filepath = os.path.join(path1,excelname)
wb = openpyxl.load_workbook(filepath)
print(wb)
# truesheet = wb.get_sheet_names('ger_event')
# print(path1)