#!/bin/sh
#SBATCH --job-name=init    # Job name
#SBATCH --mail-type=ALL               # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --ntasks=1                    # Run on a single CPU
#SBATCH --mem=4000mb                   # Memory limit
#SBATCH --time=2-00:00:00               # Time limit hrs:min:sec
#SBATCH -o initialize_%j.out      # File to which STDOUT will be written
#SBATCH -e initialize_%j.err      # File to which STDERR will be written

pwd; hostname; date

module load python

echo "Running python INITILIZATIONS on a single CPU core"

python initializations.py

date

echo "Job is finished"