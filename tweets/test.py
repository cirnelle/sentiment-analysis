__author__ = 'yi-linghwong'

import sys
'''

lines = open('labelled_tweets_semeval.txt','r').readlines()

print (len(lines))

unique = []
temp = []
dup = []

for line in lines:
    spline = line.replace('\n','').split(',')

    joined = ' '.join(spline[1:])


    new_list = [spline[0],joined]

    if len(new_list) == 2:
        if new_list[1] not in temp:
            temp.append(new_list[1])
            unique.append(new_list)

        else:
            dup.append(new_list)


print (len(unique))
print (unique[:1])



f = open('labelled_tweets_semeval.txt','w')

for u in unique:
    f.write(','.join(u)+'\n')

f.close()
'''

lines = open('raw_tweets_semeval.txt','r').readlines()

print (len(lines))

unique_r = []
temp_r = []

for line in lines:
    spline = line.replace('\n','')

    if spline not in unique_r:
        unique_r.append(spline)

    else:
        temp_r.append(spline)


print (len(unique_r))

f = open('raw_tweets_semeval.txt','w')

for u in unique_r:
    f.write(u+'\n')

f.close()
