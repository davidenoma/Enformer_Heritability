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
    #There are Datasets and there are Groups. This is composed of datasets.
    #getting the shape for SAD scores.
    # SADs = f['SAD'][()]
    # SARs = f['SAR'][()]
    # print("SAR AND SAD",SARs.shape, SADs.shape)
    snp = f['snp'].asstr()[()]
    ref = f['ref'].asstr()[()]
    alt = f['alt'].asstr()[()]
    chr = f['chr'].asstr()[()]
    pos = f['pos'][()]
    target_ids = f['target_ids'].asstr()[()]
    target_labels = f['target_labels'].asstr()[()]

    print('target_ids',target_ids.shape)
    snps = np.vstack((snp,ref,alt,chr,pos)).T
    snps  = pd.DataFrame(snps,dtype='string',)
    snps.columns = ['snp','ref','alt','chr','pos']

    targets = np.vstack((target_ids,target_labels)).T
    targets = pd.DataFrame(targets,dtype='string')
    targets.columns = ['target_ids','target_labels']
print("snps and targets shape",snps.shape,targets.shape)
f.close()
chr_number = fpath.split(".")[-2]

#
# np.savetxt("./enformer_variant_scores_csv/"+chr_number+"/SADs" + ".csv", SADs, delimiter=",")
# print("Done writing..."+"SADs"+chr_number)
# np.savetxt("./enformer_variant_scores_csv/"+chr_number+"/SARs" + ".csv", SARs, delimiter=",")
# print("Done writing..."+"SADs"+chr_number)
pd.DataFrame.to_csv(snps,"./enformer_variant_scores_csv/"+chr_number+"/snps"+chr_number + ".csv" )
print("Done writing..."+"snps"+chr_number)
pd.DataFrame.to_csv(targets,"./enformer_variant_scores_csv/"+chr_number+"/targets"+chr_number + ".csv" )
print("Done writing..."+"targets"+chr_number)
