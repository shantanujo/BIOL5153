#!/usr/bin/env python 3

job_name = 'job_assn04'
queue = 'comp01'
num_nodes = 1
num_processors = 24
walltime = 1

#print bash header

print('#SBATCH --job-name=' + job_name)
print('#SBATCH --partition' + queue)
print('#SBATCH --nodes=' + str(num_nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(num_processors))
print('#SBATCH --time=' + str(walltime) + ':00:00')
print('#SBATCH -o test_%j.out')
print('#SBATCH -e test_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=sj058@uark.edu')

#cd $SLURM_SUBMIT_DIR

# job command here
#command 1
