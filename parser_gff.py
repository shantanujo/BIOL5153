#! /usr/bin/env python3
import argparse


parser= argparse.ArgumentParser("reading a GFF file")

# adding positional argument
parser.add_argument("gff", help='opens specified gff file',type=str)
parser.add_argument("fasta", help= 'opens FASTA file', type=str)

## optional arguments

args= parser.parse_args()

#open files
gff_file = open(args.gff, "r")
fasta_file = open(args.fasta, "r")

#read the files
#with open(args.gff) as x:
	#for line in x:
		#print(line.rstrip())

with open(args.fasta) as y:
	for line in y:
		print(line.rstrip())
line = 0
lent= 0
#feature type, length
with open(args.gff) as x:
		for line in x:
			line = line.rstrip()
			line = line.split('\t')
			lent = int(line[4]) - int(line[3])
			lent += 1
			feat_name = line[2]
			print(feat_name, lent)
