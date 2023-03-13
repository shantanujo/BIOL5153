### Assignment 3 
###### Shantanu Joshi   


 
#1 Use rsync to upload the mt_genomes directory onto the AHPCC in /storage/username
```sh
rsync -rz mt_genomes sj058@hpc-portal2.hpc.uark.edu:/storage/sj058/ 
```
#2 Use scp or rsync to upload ‘unknown.fa’, which contains an unknown sequence
```sh
scp unknown.fa  sj058@hpc-portal2.hpc.uark.edu:/storage/sj058/mt_genomes
```

#3 Write a slurm script: job.slurm

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

```sh
scp job.slurm  sj058@hpc-portal2.hpc.uark.edu:/storage/sj058/mt_genomes
#logging on to the ssh
ssh sj058@hpc-portal2.hpc.uark.edu
cd /storage/sj058
#running the slurm script
sbatch job.slurm
exit
```
#4 Use rsync to synchronize the remote mt_genomes
```sh
rsync -azv sj058@hpc-portal2.hpc.uark.edu:/storage/sj058/mt_genomes .
```
#5 
a. How long did it take your job to complete?
Ans. Run time for this job was 00:00:07

b. What is the closest match in the database?
Ans. _Cucurbita_ was the closest match [Identities = 1566/1584 (99%)]

#6 Push the markdown to GitHub
```sh
git add assn-03.md
git commit -m "adding assignment 3 md file"
git push -u origin main
```