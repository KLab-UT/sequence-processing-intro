# Intro To Sequence Processing
# Introduction

The aim of this exercise is to help you understand the basics of shell scripting, a skill that is used in genomic pipeline development

# Contents

-   [Getting set up](#getting-set-up)
-   [Completing the exercise](#completing-the-exercise)


# Getting set up

At this point, you should have
(1) basic knowledge on using the command line to navigate in terminal,
(2) an account on [Github](https://github.com/), and
(3) been introduced to the very basics of [Git](https://git-scm.com/).

IF you don't know how to use terminal, don't have a github account, or don't know how to use git, notify your instructor (they will help you get the pretest up and running). Otherwise, proceed to #1 below.

1.  Login to your [Github](https://github.com/) account.

1.  Fork [this repository]([https://github.com/KLab-UT/4310-pretest](https://github.com/KLab-UT/sequence-processing-intro)) by
    clicking the 'Fork' button on the upper right of the page.

    After a few seconds, you should be looking at *your* 
    copy of the repo in your own Github account.

1.  Click the 'Clone or download' button, and copy the URL of the repo via the
    'copy to clipboard' button.

1.  In your terminal, navigate to where you want to keep this repo (you can
    always move it later, so just your home directory is fine). Then type:

        $ git clone the-url-you-just-copied

    and hit enter to clone the repository. Make sure you are cloning **your**
    fork of this repo.

1.  Next, `cd` into the directory:

        $ cd the-name-of-directory-you-just-cloned

1.  At this point, you should be in your own local copy of the repository.

1.  As you work on the exercise below, be sure to frequently `add` and `commit`
    your work and `push` changes to the *remote* copy of the repo hosted on
    GitHub. Don't enter these commands now; this is just to jog your memory:

        $ # Do some work
        $ git add file-you-worked-on.py
        $ git commit
        $ git push origin master

---

# Completing the exercise

Your goal in this exercise is to create coding scripts that will (1) summarize data from a DNA sequence alignment, (2) create and analyze an amino acid alignment, and (3) create a directory for each sample containing the DNA sequence and amino acid sequence. These objectives should be completed by running a single script (but it can run other scripts). Each of these objectives is broken up below.

> note: This readme contains several code blocks. Blocks with a ```$``` prompt refer to command that can be executed using bash (or generally other shell languages). Blocks with a ```>>>``` prompt refer to python code. Blocks without a prompt refer to content within a text file.

## Summarize data from a DNA sequence alignment
You should create a script that will process a DNA sequence alignment in fasta format. This script should out put a file called "log.txt" that contains (1) the number of samples, (2) the number of unique sampling dates, and (3) the number of variable sites (see below for definition of variable site). 

> note: You can use any scripting language for this objective. You will draw from computer science skills you have learned in classes up to this point (e.g., storing information in collections, performing simple calculations).

#### What is a FASTA file?
A fasta file stores genetic sequence data and a descriptive header for each sequence. A fasta file can have a single header or multiple headers. The header line can contain various items pertaining to the sequence, such as the chromosome, species, and individual ID. A header line is demarcated by the '>' character, and the following line(s) contain the sequence information pertaining to this specific header. The sequence line should only contain information pertaining to the sequence described by the previous header. A single fasta file can contain multiple sequences. Here is an example of what this can look like:

```
>Gene_4310, Brooks
AUGCACCGCUAG
>Gene_4310, Bailey
AUGGACCTCUAG
>Gene_4310, Benjamin
AUGTACCGCUAG
```
#### Variable Site
In an alignment, the index of each nucleotide corresponds to the same genetic position in the aligned sequences. For example, in the example above with Gene_4310 from Brooks and Bailey, you can see that usually the nucleotide at each position is the same between both sequences. In alignments of closely related organisms, this will generally be the case. However, it is possible to see differences between sequences in an alignment. For instance, at position 4 in this sequence there is a 'C' for Brooks and a 'G' for Bailey. This is a SNP (single nucleotide polymorphism). In this case, we'd say there is a SNP at position 4. The number of positions where a SNP occurs along a gene is known as the number of variable sites (S). 

Can you count the number of variable sites in this sequence alignment? If you got '2', you're correct! However, let's make sure you are correct for the right reasons. A variable site is a position along a gene sequence that contains variation- it doesn't matter how much variation, just that it exists. So at position 4 in this alignment, even though there are three different alleles ('C' for Brooks, 'G' for Bailey, and 'T' for Benjamin), position 4 is only considered one variable site. If this is the first variable site, where is the second? Position 8 ('G' for Brooks and Benjamin, 'T' for Bailey). So position 4 and position 8 are your two variable sites. 

#### Looking at a FASTA file
Let's look at a sequence alignment. At the command line you can examine this file using ```vim ExampleAlignment.fasta```.

> note: If you are new to using vim, you can exit without saving by typing ':q!' followed by enter.

Once you exit vim, you can count the number of sequences within this file from the command line by counting the number of headers:

```
$ grep '>' ExampleFasta.fasta | wc -l
```

## Create and analyze an amino acid alignment
You should create a script that will convert the DNA sequence alignment in fasta format to an amino acid sequence alignment in fasta format. You should then add the number of variable sites in the protein alignment to the "log.txt" file.

> note: You can use any scripting language and tools to do this, but I recommend writing the script in python.

Above you became familiar with a DNA sequence alignment stored in fasta format. Protein sequences can also be stored in fasta format. The extension ".fasta" is general, and can be used for any type of sequence alignment (DNA, RNA, or protein). Alternative extensions can specify whether you are working with nucleotides (".fna") or amino acids (".faa"). For part of this activity, you will convert the DNA sequences to amino acid sequences. You will use the skills you have developed in computer science along with the knowledge you've gained from biology classes to write a script in python that will translate these sequences.

Although there are several ways to address this exercise, I recommend using the python package [Biopython](https://biopython.org/). This package contains tools that can be used in computational molecular biology. [Here](http://biopython.org/DIST/docs/tutorial/Tutorial.html#sec2) is a useful tutorial for using Biopython. I will draw from this tutorial below.

#### Install Biopython
```
$ conda install -c conda-forge biopython
```
or
```
$ pip install biopython
```

> note: This is assuming you use the python package manager conda or miniconda or have pip installed. If you don't have either of these installed, I recommend miniconda (installation instructions [here](https://docs.conda.io/en/latest/miniconda.html)).

Now within your python scripts you can import biopython using the following:

```
>>> import Bio
>>> from Bio.Seq import Seq
```

You can now create Seq objects using biopython. Try it out
```
>>> my_seq = Seq("ATGCATTAACTAGAT")
>>> nuc_string = "ATGCATGTATAC"
>>> my_seq2 = Seq(nuc_string)
>>> print(my_seq)
>>> print(my_seq2)
>>> my_seq_str = str(my_seq)
>>> print(my_seq_str)
```
In most ways, we can deal with Seq objects as if they were normal python strings:
```
>>> for index, letter in enumerate(my_seq):
>>>     print(index, letter)
>>> 
>>> print(len(my_seq))
```
Also like a python string, you can do slices iwth a start, stop, and stride. For example, we can get the first, second, and third codon positions of this DNA sequence:
```
>>> my_seq[0::3]
>>> my_seq[1::3]
>>> my_seq[2::3]
```
The Seq object differs from the Python string in the methods it supports. You can’t do this with a plain string:
```
>>> my_seq.complement()
>>> my_seq.reverse_complement()
>>> my_seq.transcribe()
>>> my_seq.translate()
```
And, although not necessary to complete this project, you can also process entire fasta files with biopython
```
>>> fna_seqs = {}
>>> from Bio import SeqIO
>>> for seq_record in SeqIO.parse("orchid.fasta", "fasta"):
>>>     fna_seqs[seq_record.id] = seq_record
```

# Your Final product
You will create a script that will process an alignment of DNA coding sequence (i.e., a sequence alignment where each sequence starts with a "start" codon and ends with a "stop" codon). The script can (and should) call other scripts (for example, the user might run "main.sh" which in turn runs "count_variable_sites.py" and "alignment_parser.sh").
#### What you start with
1. A DNA sequence alignment in fasta format
#### What you end with
Your script must generate the following:
1. A text file called "log.txt" with (1) the number of samples, (2) the number of unique sampling dates, (3) the number of variable sites in the DNA sequence, and (4) the number of variable sites in the protein sequence.
1. A protein alignment file in fasta format
1. A directory for each sequence that contains its individual DNA sequence and protein sequence

# Final recommendations
Use ExampleAlignment.fasta as a test fasta file- but this will not be the file that will be used to test your script. I would draw out your approach using pseudocode before you start coding. What are the primary tasks you need to address? What kind of script will you write to address that task? You got this!



