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
    SADs = f['SAD'][()]
    SARs = f['SAR'][()]

    print(SARs.shape,SADs.shape)
    snps = np.empty([f['alt'].shape[0],] )
    targets = np.empty([f['target_ids'].shape[0],])
    i = 2
    for key in group_keys:
        print(i)
        if i >= 2 & i < 7:
            snps = np.concatenate([snps,f[group_keys[i]][()]])
        if i > 7:
            targets = np.concatenate([targets,f[group_keys[i]][()]])
        i+=1
print(snps.shape,targets.shape)
f.close()
chr_number = fpath.split(".")[-2]
np.savetxt("SADs"+chr_number + ".csv", SADs, delimiter=",")
np.savetxt("SARs"+chr_number + ".csv", SARs, delimiter=",")
np.savetxt("snp"+chr_number + ".csv", snps, delimiter=",")
np.savetxt("targets"+chr_number + ".csv", targets, delimiter=",")
