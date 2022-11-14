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
    SADs = f['SAD'][()]
    SARs = f['SAR'][()]
    # print(SARs.shape, SADs.shape)
    snp = f['snp'][()]
    ref = f['ref'][()]
    alt = f['alt'][()]
    chr = f['chr'][()]
    pos = f['pos'][()]

    target_ids = f['target_ids'][()]
    target_labels = f['target_labels'][()]
    print('target_ids',target_ids.shape)
    snps = np.vstack((alt,chr,pos,ref,snp)).T
    snps  = pd.DataFrame(snps,dtype='string')
    targets = np.vstack((target_ids,target_labels)).T
    targets = pd.DataFrame(targets,dtype='string')
print(snps.shape,targets.shape)
f.close()
chr_number = fpath.split(".")[-2]


np.savetxt("./enformer_variant_scores_csv/SADs"+chr_number + ".csv", SADs, delimiter=",")
print("Done writing..."+"SADs"+chr_number)
np.savetxt("./enformer_variant_scores_csv/SARs"+chr_number + ".csv", SARs, delimiter=",")
print("Done writing..."+"SADs"+chr_number)
pd.DataFrame.to_csv(snps,"./enformer_variant_scores_csv/snps"+chr_number + ".csv" )
print("Done writing..."+"snps"+chr_number)
pd.DataFrame.to_csv(targets,"./enformer_variant_scores_csv/targets"+chr_number + ".csv" )
print("Done writing..."+"targets"+chr_number)
