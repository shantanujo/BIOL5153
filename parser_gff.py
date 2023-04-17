#! /usr/bin/env python3
import argparse
import csv
from Bio import SeqIO

parser= argparse.ArgumentParser("reading a GFF file")
# adding positional argument
parser.add_argument("gff", help='opens specified gff file',type=str)
parser.add_argument("fasta", help= 'opens FASTA file', type=str)

## optional arguments
args= parser.parse_args()


#FASTA file
genome = SeqIO.read("covid.fasta", "fasta")

#open files
gff_file = open(args.gff, "r")
fasta_file = open(args.fasta, "r")

with open (args.fasta) as y:
	for line in y:
		print(line.rstrip())
line = 0

#feature type, length
with open(args.gff) as x:
	reader = csv.reader(x, delimiter='\t')
	for line in reader:
		if not line:
			continue
		else:
			start = int(line[3])
			end = int(line[4])
			lent = end - start + 1
			print(line[2], lent)
			line[5] = str(lent)
			new_line = "\t".join(line)
			feat_seq = genome.seq[start-1: end]
			organism = line[0]
			source = line[1]
			attri = line[8]
			feat_type = line[2]
			print(">" + organism, feat_type, attri, feat_seq)
			print(feat_seq)
