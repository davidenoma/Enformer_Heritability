import h5py
import sys
import numpy as np

fpath = sys.argv[1]
with h5py.File(fpath, "r") as f:
    # Print all root level object names (aka keys)
    # these can be group or dataset names
    print("Keys: %s" % f.keys())
    group_keys = list(f.keys())
    #Keys: <KeysViewHDF5 ['SAD', 'SAR', 'alt', 'chr', 'pos', 'ref', 'snp', 'target_ids', 'target_labels']
    #getting the shape for SAD scores.
    snp_activity_difference = np.empty([f[group_keys[0]].shape[0], f[group_keys[0]].shape[1]])
    snps = np.empty([f[group_keys[2]].shape[0],] )
    targets = np.empty([f[group_keys[7]].shape[0], ])
    i = 0
    for key in group_keys:
        print("Key for: ",group_keys[i])
        print(f[key].shape,key)
        # if i < 2:
        #     snp_activity_difference = f[key][()]
        # if i >= 2 & i < 7:
        #     snps = f[key][()]
        # if i > 7:
        #     targets = f[key][()]
        i+=1
f.close()
chr_number = fpath.split(".")[-2]
np.savetxt("SA_"+chr_number + ".csv", snp_activity_difference, delimiter=",")
np.savetxt("snp"+chr_number + ".csv", snps, delimiter=",")
np.savetxt("targets"+chr_number + ".csv", targets, delimiter=",")
