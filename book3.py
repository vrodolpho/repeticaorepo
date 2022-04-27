import openpyxl

book = openpyxl.load_workbook('Planilha de Compras.xlsx')
frutas_page =  book['Frutas']
rows = frutas_page.iter_rows(min_row=2, max_row=5, min_col=1, max_col=3)
print(rows)

for a,b,c in rows:
  print(a.value, b.value, c.value)