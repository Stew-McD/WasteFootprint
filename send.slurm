#!/bin/bash
#SBATCH --job-name=WasteDemand_ei38
#SBATCH --output=%j.out
#SBATCH --mail-user="s.c.mcdowall@leidenuniv.nl"
#SBATCH --mail-type="ALL"
##SBATCH --mem-per-cpu=10G
#SBATCH --time=00:30:00
#SBATCH --partition=cpu-short
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=20

source ~/.bashrc

# load modules (assuming you start from the default environment)
# we explicitly call the modules to improve reproducibility
# in case the default settings change

module load Python/3.9.5-GCCcore-10.3.0
module load Miniconda3 

#conda env create -f ~/alice/environment-ei38.yml
#conda init bash


#conda create env -f /home/mcdowallsc/alice/environment-ei38.xml

conda activate ei38

# Source the Python virtual environment
#source $HOME/.conda/envs/ei38/bin/python3


echo "[$SHELL] #### Starting Python test"
echo "[$SHELL] ## This is $SLURM_JOB_USER on $HOSTNAME and this job has the ID $SLURM_JOB_ID"
# get the current working directory
export CWD=$(pwd)
echo "[$SHELL] ## current working directory: "$CWD

# Run the file
echo "[$SHELL] ## Run script"
python3 main.py
echo "[$SHELL] ## Script finished"

echo "[$SHELL] #### Finished Python test. Have a nice day"
