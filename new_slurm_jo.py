#! /usr/bin/env python3

import argparse
parser= argparse.ArgumentParser("Running a job on AHPCC with variables")

# adding opsitional argument
parser.add_argument("job_name", help='specifies the job name',type=str)

#adding optional args
parser.add_argument("-q","--queue", help='specifies the queue', type=str, default= 'comp01')
parser.add_argument("-n", "--nodes", help='specifies the number of nodes', type=int, default='1')
parser.add_argument("-p","--num_processors", help='specifies the number of prcessors to use', type=int, default='24')
parser.add_argument("-w","--walltime", help='specifies the walltime', type=int, default='1')

args= parser.parse_args()

print('#!/bin/bash')
print()
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
print()
print('module purge')
print()
print('cd $SLURM_SUBMIT_DIR')

#job commands here

