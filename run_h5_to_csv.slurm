#!/bin/bash
# ---------------------------------------------------------------------
# An example SLURM script for running a job on a Compute Canada cluster.
# ---------------------------------------------------------------------
#SBATCH --job-name=run_h5_to_csv
#SBATCH --nodes=1
#SBATCH --ntasks=2
#SBATCH --cpus-per-task=4
#SBATCH --time=0-10:00:00
#SBATCH --mem=64gb
#SBATCH --partition=cpu2019-bf05
# ---------------------------------------------------------------------
echo "Current working directory: `pwd`"
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
module load python
for file in enformer_variant_scores/;
do echo $file;
done
echo "hi"

python myscript.py

# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------
