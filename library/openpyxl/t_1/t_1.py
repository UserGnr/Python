from openpyxl import Workbook

wb = Workbook() # Uma pasta de trabalho é sempre criada com pelo menos uma planilha. Você pode obtê-la usando a propriedade Workbook.active

ws = wb.active

ws2 = wb.create_sheet("Sheet2")
ws3 = wb.create_sheet("Sheet3")
ws4 = wb.create_sheet("Sheet4")

ws3 = wb.active

wb.save('library\\openpyxl\\t_1\\test.xlsx')