import pandas as pd
import sumpy as np

coluna = 'JAN FEV MAR'.split()
linha = 'INTERNET ÁGUA LUZ'.split()
d = np.random.randint(100,1000,len(coluna)*len(linha)).reshape(len(linha, len(coluna))

df = pd.DataFrame(d,linha, coluna)