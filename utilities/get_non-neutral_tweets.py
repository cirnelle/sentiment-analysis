__author__ = 'yi-linghwong'

import os
import sys


lines = open('../tweets/ground_truth/raw/raw_tweets_#pluto.txt','r')
lines2 = open('../tweets/ground_truth/labelled/labelled_tweets_#pluto.txt','r')

labelled = []
raw = []

for line in lines:

    spline = line.replace('\n','').split(',')
    labelled.append(spline)

print (len(labelled))

for line in lines2:

    spline = line.replace('\n','').split(',')
    raw.append(spline)

print (len(raw))

if len(labelled) == len(raw):

    zipped = zip(raw,labelled)

    non_neutrals = []
    neutrals = []

    for z in zipped:

        z = list(z)
        z = z[0] + z[1]

        if z[0] != 'neutral':
            non_neutrals.append([z[0],z[2]])

        elif z[0] == 'neutral':
            neutrals.append([z[0],z[2]])


    print (len(non_neutrals))
    print (len(neutrals))

else:
    print ("Lengths not equal, exiting...")
    sys.exit()


# write non neutrals to file

f = open('../tweets/ground_truth/labelled_ground_truth_#pluto.csv','w')

for nn in non_neutrals:
    f.write(','.join(nn)+'\n')

f.close()

# write neutrals to file

f = open('../tweets/ground_truth/neutral/neutral_ground_truth_#pluto.csv','w')

for n in neutrals:
    f.write(','.join(n)+'\n')

f.close()