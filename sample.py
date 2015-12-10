#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 14:30:08 2015

@author: ismtabo
"""

import csvunicode
import itertools
from sys import argv
from sys import exit
import sys
from os import path
from os import popen

if len(argv) < 2:
    exit('Usage: %s path-csv-file destination-path' % argv[0])

# Verify all arguments are introduce
if not path.exists(argv[1]):
    exit('Error: csv file, %s doesn\'t exists' % argv[1])

if not path.exists(argv[1]):
    exit('Error: destination path, %s doesn\'t exists' % argv[1])

file_path = argv[1]
dest_path = argv[2]

# Read source CSV 
reader = csvunicode.UnicodeReader(file(file_path,'r'),delimiter=';')

# Define de header of the table
header = reader.next()
rows = []

# Separate each row
for row in reader:
    rows.append(row)


print 'Total %d rows readed' % (len(rows)+1)

# Group csv tuples by its first value name
groups = itertools.groupby(rows,lambda x: x[0].split('. ')[0])
keys = []
mini_groups = []
for k,g in groups:
    keys.append(k)
    mini_groups.append(list(g))

# Rewrite each group in its own file
for key, group in zip(keys,mini_groups):
    writer = csvunicode.UnicodeWriter(file(dest_path+'/'+key+'.csv','w'),delimiter=';')
    writer.writerow(header[1:])
    for elem in list(group):
        writer.writerow(elem[1:])

print 'Total %d files created' % (len(keys))
