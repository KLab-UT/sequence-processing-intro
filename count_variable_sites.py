#! /usr/bin/env python
"""
Script to find out the number of variable sites in a multiple sequence alignment

------------------
Assumption: All sequences are of equal length

Input: fasta file
Output: log file

Example: python alignment_comparison.py ExampleAlignment.fasta
"""

import sys
import Bio
from Bio.Seq import Seq

class SampleSeq:
    """
    Class for samples in a multiple sequence alignment
    """
    def __init__(self, name_in, date_in, seq_id_in, seq_type_in, dna_seq_in):
        self.name = name_in
        self.date = date_in
        self.seq_id = seq_id_in
        self.seq_type_in = seq_type_in
        self.dna_seq = dna_seq_in
        self.aa_seq = str(Seq(dna_seq_in.translate()))


def get_ref_seq(instream, peptide_out):
    for fna_line in instream:
        faa_line = translate(fna_line)
        peptide_out.write(faa_line)
        if fna_line[0] != ">":
            ref_seq_out = fna_line.strip()
            break
    return ref_seq_out

def get_var_sites(instream, ref_dna, peptide_out):
    ref_aa = str(Seq(ref_dna).translate())
    var_sites = []
    fna_var_sites = set()
    faa_var_sites = set()
    for fna_line in instream:
        faa_line = translate(fna_line)
        peptide_out.write(faa_line)
        fna_var_sites = compare_seqs(ref_dna, fna_line.strip(), fna_var_sites)
        faa_var_sites = compare_seqs(ref_aa, faa_line.strip(), faa_var_sites)
    var_sites.append(fna_var_sites)
    var_sites.append(faa_var_sites)
    varsites = tuple(var_sites)
    return var_sites

def compare_seqs(seq1, seq2, var_sites):
    if (seq1 != seq2) and (seq2[0] != '>'):
        new_var = find_var(seq1, seq2)
        for site in new_var:
           var_sites.add(site) 
    return var_sites

def find_var(seq1, seq2):
    var_sites = [
        i for i in range(len(seq1))
        if seq1[i] != seq2[i]
    ]
    return var_sites

def translate(fna_line):
    if fna_line[0] != '>':
        fna_line = fna_line.strip()
        faa_line = str(Seq(fna_line).translate()) + "\n"
    else:
        faa_line = fna_line
    return faa_line

if __name__ == "__main__":
    with open(sys.argv[1], 'r') as infile:
        with open(sys.argv[2], 'a') as logfile:
            with open((sys.argv[1].split(".")[0]) + ".faa", 'w') as peptide_out:
                ref_seq = get_ref_seq(infile, peptide_out)
                var_sites = get_var_sites(infile, ref_seq, peptide_out) 
                n_DNA_var = len(var_sites[0])
                n_AA_var = len(var_sites[1])
                logfile.write("number of variable sites in DNA alignment: " + str(n_DNA_var) + '\n')
                logfile.write("positions of variable sites in DNA alignment: " + str(var_sites[0]) + '\n')
                logfile.write("number of variable sites in AA alignment: " + str(n_AA_var) + '\n')
                logfile.write("positions of variable sites in AA alignment: " + str(var_sites[1]) + '\n')
