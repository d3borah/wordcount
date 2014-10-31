#!/usr/bin/env python
import fileinput
import re
import sys

#compile a regular expression to later use to exclude words consisting of only 
#one or more dashes
pat = re.compile(r"^[\-\_]+$")

#create words by iterating the file object corresponding to the input file (or sys.stdin if none supplied),
#and substituting a space for non-word starting characters (ie. punctuation) and then splitting on space. 
#If the word is not just a line of - or _, and is not empty, emit it with a count of "1". 
for line in fileinput.input():
    for word in re.sub('[^a-z0-9\-\_]', ' ', line.strip().lower()).split(" "):  
        if not re.search(pat, word) and len(word) > 0:
            print "\t".join([word, "1"])
