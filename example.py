#!/usr/local/bin/python3
from openpyxl import load_workbook

wb2 = load_workbook('Workbook1.xlsx')
print (wb2.get_sheet_names())
