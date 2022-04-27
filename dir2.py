import os
from pathlib import Path
import pandas as pd

path_dir = "./home/runner/Estrutura-de-Repeticao"

os.walk(path_dir)
print(path_dir)

for root, subfolder, filename in os.walk(path_dir):
  for uniqueFile in filename:
    print(uniqueFile)