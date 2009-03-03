#!/usr/bin/env python

import sys
sys.path.append('/n/taskbin')

import indexer

indexer.delete_words()
indexer.create_words()

print "Done indexing taskbin."
