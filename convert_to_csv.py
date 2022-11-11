import h5py
import sys
import numpy as np

fpath = sys.argv[1]
ds_arr = ""

with h5py.File(fpath, "r") as f:
    # Print all root level object names (aka keys)
    # these can be group or dataset names
    print("Keys: %s" % f.keys())
    group_keys = list(f.keys())
    ds_arr = np.empty([f[group_keys[0]].shape[0], len(group_keys)])
    i = 0
    for key in group_keys:
        ds_arr[:, i] = f[key]
        i += 1
f.close()
np.savetxt(fpath + ".csv", ds_arr, delimiter=",")
