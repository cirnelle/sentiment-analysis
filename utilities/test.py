__author__ = 'yi-linghwong'

import os
import sys

'''

lines = open('../tweets/ground_truth/source/labelled_ground_truth_combined.txt','r').readlines()

tweets = []

for line in lines:
    spline = line.replace('\n','').split(',')

    if len(spline) == 2:
        tweets.append(spline)

    else:
        pass

print (len(tweets))

temp = []
no_dup = []

for t in tweets:
    if t[1] not in temp:
        temp.append(t[1])
        no_dup.append(t)

    else:
        pass

print (len(no_dup))


f = open('../tweets/ground_truth/source/labelled_ground_truth_nodup.txt','w')

for nd in no_dup:
    f.write(','.join(nd)+'\n')

f.close()
'''

lines = open('../tweets/ground_truth/source/labelled_ground_truth_nodup.txt','r').readlines()
lines2 = open('../tweets/ground_truth/preprocessed/preprocessed_tweets_groundtruth.txt','r').readlines()

raw = []

for line in lines:
    spline = line.replace('\n','').split(',')
    raw.append(spline[1])

print (len(raw))

processed = []

for line in lines2:
    spline = line.replace('\n','')
    processed.append(spline)

print (len(processed))

zipped = zip(processed,raw)

both = []

for z in zipped:

    z = list(z)
    both.append(z)

print (len(both))
print (both[:1])

lines3 = open('../tweets/ground_truth/labelled_preprocessed.txt','r').readlines()

labelled = []

for line in lines3:
    spline = line.replace('\n','').split(',')
    labelled.append(spline)

print (len(labelled))
print (labelled[:1])

final = []

for l in labelled:
    l[1] = l[1].rstrip()

    for b in both:

        if l[1] == b[0]:
            final.append([l[0],b[1]])
            break


print (len(final))

no_dup = []
temp = []

for fi in final:
    if fi[1] not in temp:
        temp.append(fi[1])
        no_dup.append(fi)

print (len(no_dup))


f = open('../tweets/ground_truth/labelled_raw.txt','w')

for nd in no_dup:
    f.write(','.join(nd)+'\n')

f.close()









