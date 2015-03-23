#!/usr/bin/python

from collections import defaultdict
import string
import os
import sys
from heapq import heappush as push, heappop as pop, heappushpop as pushpop

# Initialization
print "Executing word_count_running_median.py...\n"
max_heap = []
min_heap = []
N = 0
file_names  = []
word_count = defaultdict(int)

# Opening files to write results
wc_file = open(sys.argv[2], 'w')
median_file = open(sys.argv[3], "w")

# creating a generator to read files line by line
def sentences(file_name):
    with open(file_name) as f:
       for line in f:
           yield [sentence for sentence in line.lower().translate(string.maketrans("",""), string.punctuation).strip().split()]

# routine to find running median
def median(element):
    global N
    if N%2 == 0:
        push(max_heap, -1*element)
        N += 1
        if len(min_heap)==0:
            return -1*max_heap[0]
        elif -1*max_heap[0]>min_heap[0]:
            from_max = -1*pop(max_heap)
            from_min = pop(min_heap)
            push(min_heap, from_max)
            push(max_heap, -1*from_min)
    else:
        from_max = -1*pushpop(max_heap, -1*element)
        push(min_heap, from_max)
        N += 1
    if N%2 == 0:
        return float(-1*max_heap[0] + min_heap[0])/2.0
    else:
         return -1*max_heap[0]

# read all text files in the wc_input directory
for file in os.listdir(sys.argv[1]):
    if file.endswith(".txt"):
        file_names.append(file)

file_names = sorted(file_names)

# display the number of text files in wc_input and their names
print ("%d text files found in the directory wc_input\nFiles are-" % len(file_names))
for i, name in enumerate(file_names):
    print ("%d. %s" % (i+1, name))

# read each file, count word occurences and find running median of the line lenth
for each_file in file_names:
    for lines in sentences(sys.argv[1]+"/"+each_file):
        if lines==['']:
            length_of_line = 0
        else:
            length_of_line = len(lines)
        median_file.write("%.1f \n" % median(float(length_of_line)))
        for words in lines:
            if words != "" and words != " " and words not in string.punctuation:
                word = words.lower().translate(string.maketrans("",""), string.punctuation)
                if word != "" and word != " ":
                    word_count[word] += 1

# save the word counts in a file
for keys in sorted(word_count):
    wc_file.write(keys+"\t"+str(word_count[keys])+"\n") 

# close result files
wc_file.close()
median_file.close()

print ("\n%d unique words found\n" % len(word_count))
print ("Results have been saved to %s and %s" % (sys.argv[2], sys.argv[3]))