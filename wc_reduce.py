#!/usr/bin/env python

import sys
from collections import defaultdict

#initialize dictionary with defaultdict to call a factory function to supply missing values
word_list = defaultdict(int)

for line in sys.stdin:
    try:
        word, count = line.strip().split("\t", 2)
        word_list[word] += int(count)

    except ValueError, err:
        sys.stderr.write("Value ERROR: %(err)s\n%(data)s\n" % {"err": str(err), "data": line})

for word, count in word_list.items():
    print "\t".join([word, str(count)])
