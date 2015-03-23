#!/usr/bin/env python

import sys
import os
import Bio.SeqIO
import seq_stats2

if len(sys.argv) != 2:
    exit("Usage: {} <FASTA file>".format(os.path.basename(sys.argv[0])))

filename = sys.argv[1]
for seq in Bio.SeqIO.parse(filename, 'fasta'):
    print "{} {}%".format(seq.id, int(seq_stats2.gc_content(str(seq.seq))))


