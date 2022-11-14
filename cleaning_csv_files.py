import sys
import numpy as np
import pandas as pd

file = sys.argv[1]

file = pd.read_csv('~/Data/EnformerHeritability/snps22.csv')
print(file.shape,file.head())

