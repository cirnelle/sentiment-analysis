__author__ = 'yi-linghwong'

import sys
import time

print (time.time())




'''
lines = open('emoticons/emo_dict.txt', 'r').readlines()

emoticons_old = []
emoticons_new = []
emoticons_ss = []

print (len(lines))

for line in lines:
    spline = line.replace('\n','').split('\t')
    emoticons_old.append(spline[0])

lines = open('emoticons_sentistrength.txt', 'r').readlines()

for line in lines:
    spline = line.replace('\n','').split('\t')
    emoticons_ss.append(spline[0])

for es in emoticons_ss:

    if es not in emoticons_old:
        emoticons_new.append(es)


print (len(emoticons_new))


f = open('emoticons.txt','w')

for en in emoticons_new:
    f.write(str(en)+'\n')

f.close()
'''
