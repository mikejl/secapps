# 
# binscraper.py
# Used to collect string data from binary files and list summary
# Mike Libassi
# 7-11-16
# 
# Ver 1.  Read files from soure and write results to text
# Ver 2 . Parst and list items my count
# 
# 
# ######################################################################### 

import sys
import string
import csv
import os
import re
from subprocess import call 
from collections import Counter

# Local dir of raw file = source
sourcedir = "./source"
if not os.path.exists(sourcedir):
	print "creating input directory (source) place files to read here"
	print "Exiting."
	os.makedirs(sourcedir)
	exit()


# local dir of results = results
outdir = "./results"
if not os.path.exists(outdir):
	print "creating output directory (results) for .txt results"
	os.makedirs(outdir)

# Strings each file in source directory 
for infile in os.listdir(sourcedir):
	print "Parsed: " + infile
	outfile = infile+".txt"
	fpath = os.path.join(sourcedir, infile)
	opath = os.path.join(outdir, outfile)
	strcmd = "strings"+" "+fpath+" "+">>"+opath
	os.system(strcmd)

# Pasre lies and count items
for resultsfile in os.listdir(outdir):
	ofile = os.path.join(outdir, resultsfile)
	with open (ofile) as rf:
		counts = Counter(rf)


# Print a sorted list of items found
print 'Most common (count and item):'
for item, count in counts.most_common():
    print '%7d: %s ' % (count, item)

# TODO: parse into CSV and(or) db?
# TODO: preform analysis for encoding types, keywords, most used words, connection strings, etc

# END
	
	

	

	


