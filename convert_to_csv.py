import h5py
import sys
import numpy as np
import pandas as pd
fpath = sys.argv[1]
snps = ""
targets = ""
with h5py.File(fpath, "r") as f:
    # Print all root level object names (aka keys)
    # these can be group or dataset names
    print("Keys: %s" % f.keys())
    group_keys = list(f.keys())
    #Keys: <KeysViewHDF5 ['SAD', 'SAR', 'alt', 'chr', 'pos', 'ref', 'snp', 'target_ids', 'target_labels']
    #getting the shape for SAD scores.
    # SADs = f['SAD'][()]
    # SARs = f['SAR'][()]
    # print(SARs.shape, SADs.shape)
    snp = f['snp'][()]
    ref = f['ref'][()]
    alt = f['alt'][()]
    chr = f['chr'][()]
    pos = f['pos'][()]
    target_ids = f['target_ids'][()]
    target_labels = f['target_labels'][()]
    print('target_ids',target_ids.shape)
    snps = np.vstack((alt,chr,pos,ref,snp))
    snps  = pd.DataFrame(snps)
    # snps = np.empty([f['alt'].shape[0],] )
    targets = np.vstack((target_ids,target_labels))
    targets = pd.DataFrame(targets)
    # i = 2
    # for key in group_keys:
    #     print(i)
    #     if i >= 2 & i < 7:
    #         snps = np.concatenate([snps,f[group_keys[i]][()]])
    #     if i > 7:
    #         targets = np.concatenate([targets,f[group_keys[i]][()]])
    #     i+=1
print(snps.shape,targets.shape)
f.close()
chr_number = fpath.split(".")[-2]
# np.savetxt("SADs"+chr_number + ".csv", SADs, delimiter=",")
print("Done writing..."+"SADs"+chr_number)
# np.savetxt("SARs"+chr_number + ".csv", SARs, delimiter=",")
print("Done writing..."+"SADs"+chr_number)
pd.DataFrame.to_csv(snps,"snps"+chr_number + ".csv" )
print("Done writing..."+"snps"+chr_number)
pd.DataFrame.to_csv(targets,"targets"+chr_number + ".csv" )
print("Done writing..."+"targets"+chr_number)
