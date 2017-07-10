#!/bin/sh
#SBATCH --job-name=slopeAdj    # Job name
#SBATCH --mail-type=ALL               # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --ntasks=1                    # Run on a single CPU
#SBATCH --mem=4000mb                   # Memory limit
#SBATCH --time=10-00:00:00               # Time limit hrs:min:sec
#SBATCH -o slopeAdj_%j.out      # File to which STDOUT will be written
#SBATCH -e slopeAdj_%j.err      # File to which STDERR will be written

pwd; hostname; date

module load python

echo "Running python SLOPE on a single CPU core"

python slopeAdjusted.py

date

echo "Job is finished"