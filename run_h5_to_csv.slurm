#!/bin/bash
#SBATCH --job-name=run_h5_to_csv
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=2
#SBATCH --time=3-00:00:00
#SBATCH --mem=32gb
#SBATCH --partition=cpu2022
# ---------------------------------------------------------------------
echo "Current working directory: `pwd`"
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
module load python/3.10.4
h5files=`ls ./enformer_variant_scores/*.h5`
for file in $h5files
do echo $file
python ./Enformer_Heritability/convert_to_csv.py $file
done
echo "hi"
# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------