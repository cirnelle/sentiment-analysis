__author__ = 'yi-linghwong'

import os
import sys

lines = open('../tweets/ground_truth/labelled_ALL.txt')

tweets = []

for line in lines:
    spline = line.replace('\n','').split(',')

    if len(spline) == 2:
        tweets.append(spline[1])

    else:
        pass

print (len(tweets))

no_dup = []

for t in tweets:
    if t not in no_dup:
        no_dup.append(t)

    else:
        print (t)

print (len(no_dup))
