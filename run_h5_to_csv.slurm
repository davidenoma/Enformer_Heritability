#!/bin/bash
# ---------------------------------------------------------------------
# An example SLURM script for running a job on a Compute Canada cluster.
# ---------------------------------------------------------------------
#SBATCH --job-name=SLURM_example

#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=0-05:00:00
#SBATCH --mem=64gb
#SBATCH --partition=cpu2021
# ---------------------------------------------------------------------
echo "Current working directory: `pwd`"
echo "Starting run at: `date`"
# ---------------------------------------------------------------------
module load python

echo "hi"
python myscript.py

# ---------------------------------------------------------------------
echo "Job finished with exit code $? at: `date`"
# ---------------------------------------------------------------------
