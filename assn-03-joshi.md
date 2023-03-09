### Assignment 3 
###### Shantanu Joshi   

	
1. How long did it take your job to complete?
	Ans. Run time for this job was 00:00:07

2. What is the closest match in the database?
	And. Cucurbita was the closest match [Identities = 1566/1584 (99%)]

code:
```sh
#copying files to ahpcc storage/username
rsync -rz mt_genomes sj058@hpc-portal2.hpc.uark.edu:/storage/sj058/
scp unknown.fa  sj058@hpc-portal2.hpc.uark.edu:/storage/sj058/mt_genomes
scp job.slurm  sj058@hpc-portal2.hpc.uark.edu:/storage/sj058/mt_genomes
#logging on to the ssh
ssh sj058@hpc-portal2.hpc.uark.edu
cd /storage/sj058
#running the slurm script
sbatch job.slurm
exit
##syncing back the mt_genomes directory
rsync -azv sj058@hpc-portal2.hpc.uark.edu:/storage/sj058/mt_genomes .
```

job.slurm

```sh
#!/bin/bash
#SBATCH --job-name=sj058
#SBATCH --partition comp01
#SBATCH --nodes=1
#SBATCH --qos comp
#SBATCH --tasks-per-node=32
#SBATCH --time=0:01:00
#SBATCH -o test_%j.out
#SBATCH -e test_%j.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=sj058@uark.edu
export OMP_NUM_THREADS=32
module purge
module blast/2.10.0
cd $SLURM_SUBMIT_DIR
# job command here
cat *.fasta > genomes.fas
makeblastdb -in genomes.fas -dbtype nucl
blastn -query unknown.fa -db genomes.fas > unknown.vs.genomes.blastn
```

