#!/usr/bin/env python 3

job_name = "job_assn04"
queue_name= "comp007"
num_nodes= "1"
num_processors= "32"
walltime= "0"

print('#SBATCH --job-name=',job_name)
print('#SBATCH --partition', queue_name)
print('#SBATCH --nodes=',num_nodes)
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=',num_processors)
print('#SBATCH --time=',walltime)
print('#SBATCH -o test_%j.out')
print('#SBATCH -e test_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=sj058@uark.edu')

cd $SLURM_SUBMIT_DIR

# job command here
#command 1
