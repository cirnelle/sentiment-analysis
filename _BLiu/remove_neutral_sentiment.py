__author__ = 'yi-linghwong'

import sys
import os



lines = open('results/sts_gold_tweets_senti_polarity.txt','r').readlines()

results = []

for line in lines:
    spline = line.replace('\n','').split(',')
    results.append(spline)

print (len(results))

noneutral = [] #only tweets
noneutral_full = [] #tweets and sentiment
neutral = []

for r in results:
    if r[0] != 'neutral':
        noneutral.append(r[1])
        noneutral_full.append(r)

    elif r[0] == 'neutral':
        neutral.append(r[1])

    else:
        print ("error")

print (len(noneutral))
print (len(neutral))

f = open('results/sts_gold_noneutral.txt','w')

for nnf in noneutral_full:
    f.write(','.join(nnf)+'\n')

f.close()



# remove noneutral from labelled tweets
# tweets of the labelled tweets are not preprocessed, can't compare directly, need to zip two files

lines = open('../tweets/labelled_tweets_sts_gold.txt','r').readlines()

polarity = []

for line in lines:
    spline = line.replace('\n','').split(',')
    polarity.append(spline[0])

print (len(polarity))

lines = open('../tweets/preprocessed_tweets_sts_gold.txt','r').readlines()

preprocessed = []

for line in lines:
    spline = line.replace('\n','')
    preprocessed.append(spline)

print (len(preprocessed))

combined = zip(polarity,preprocessed)

labelled = []

for c in combined:
    c = list(c)
    labelled.append(c)

print (len(labelled))

labelled_noneutral = []

f = open('results/labelled_sts_gold.txt','w')

for l in labelled:
    f.write(','.join(l)+'\n')

f.close()

# remove neutral from labelled list

for l in labelled:
    l[1] = ' '+l[1]+' '
    #l[1] = l[1].lower()

    if l[1] in noneutral:
        labelled_noneutral.append(l)

print (len(labelled_noneutral))

f = open('results/labelled_sts_gold_noneutral.txt','w')

for ln in labelled_noneutral:
    f.write(','.join(ln)+'\n')

f.close()
