#! /usr/bin/env python3

import argparse
parser= argparse.ArgumentParser("Running a job on AHPCC with variables")

# adding opsitional argument
parser.add_argument("job_name", help='specifies the job name',type=str)

#adding optional args
parser.add_argument("-q","--queue", help='specifies the queue', type=str, default= 'comp01')
parser.add_argument("-n", "--nodes", help='specifies the number of nodes', type=str, default='1')
parser.add_argument("-np","--num_processors", help='specifies the number of prcessors to use', type=str, default='32')
parser.add_argument("-w","--walltime", help='specifies the walltime', type=str)

args= parser.parse_args()

#print variables
print('#SBATCH --job-name=' + args.job_name)
print('#SBATCH --partition', str(args.queue))
print('#SBATCH --nodes=' + str(args.nodes))
print('#SBATCH --qos comp')
print('#SBATCH --tasks-per-node=' + str(args.num_processors))
print('#SBATCH --time=' + str(args.walltime) + ':00:00')
print('#SBATCH -o test_%j.out')
print('#SBATCH -e test_%j.err')
print('#SBATCH --mail-type=ALL')
print('#SBATCH --mail-user=sj058@uark.edu')
#cd $SLURM_SUBMIT_DIR

