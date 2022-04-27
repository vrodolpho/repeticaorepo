import os
from pathlib import Path
import pandas as pd

caminho= Path.cwd()
print(caminho)

vendas = pd.DataFrame(columns=['LOJA', 'Vendedor', 'Valor da Venda'])

for pasta in caminho.iterdir():
  if pasta.is_dir():
    os.chdir(pasta)
    caminho= Path.cwd()
for arquivo in caminho.iterdir():
  venda = pd.read_excel(arquivo)
  vendas = vendas.append(venda,ignore_index=True)

display(vendas)