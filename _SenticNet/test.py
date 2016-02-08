__author__ = 'yi-linghwong'

import sys

lines = open('dictionary/polarity_list.txt','r').readlines()

polarity_list = []

for line in lines:
    spline = line.replace('\n','').split('\t')

    polarity_list.append(spline[0])

print (len(polarity_list))

concept_list = []

lines = open('dictionary/concepts.txt','r').readlines()

for line in lines:
    spline = line.replace('\n','')

    concept_list.append(spline)

print (len(concept_list))

temp = []

for cl in concept_list:

    if cl not in polarity_list:

        temp.append(cl)

print (temp)
