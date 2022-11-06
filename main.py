import modules

from modules.mod_openpyxl import wb_read
from modules.mod_openpyxl import wb_write
from modules.mod_XlsxWriter import wb_2


print(modules.NAME)

# Модуль 1
sheet_read = wb_read["Лист1"]
print(sheet_read["A1"].value)

sheet_write = wb_write.active
sheet_write["A2"] = 2
wb_write.save("./Excel/test2.xlsx")
