import pandas as pd
import sys
fpath = sys.argv[1]
print(len(fpath),)
if len(sys.argv) > 2:
    key = sys.argv[2]
    df = pd.read_hdf(fpath, key=key)
else:
    df = pd.read_hdf(fpath)

df.to_csv(sys.stdout, index=False)