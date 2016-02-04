__author__ = 'yi-linghwong'

import sys


slang_list = ['ur', 'brb']

tweet_list = ['ur here because of our', 'i am ur uruguay']

dict = {'ur': 'you are'}

for tl in tweet_list:
    tl = tl.split()

    #for sl in slang_list:

    if any(slang in tl for slang in slang_list):

        print (tl)

        tl = [dict[slang] if x==slang else x for x in tl]

        print (tl)




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
