#! /usr/bin/env python3
import argparse
import csv

parser= argparse.ArgumentParser("reading a GFF file")
# adding positional argument
parser.add_argument("gff", help='opens specified gff file',type=str)
parser.add_argument("fasta", help= 'opens FASTA file', type=str)

## optional arguments
args= parser.parse_args()

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
