__author__ = 'yi-linghwong'

import sys

lines = open('emoticons/emo_dict.txt', 'r').readlines()


emo_list = []

for line in lines:
    new_list = []
    spline = line.replace('\n', '').split('\t')

    if spline[1] == 'sad':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'happy':
        new_list.append(spline[0])
        new_list.append('1')
        emo_list.append(new_list)

    elif spline[1] == 'evil':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'playful':
        new_list.append(spline[0])
        new_list.append('1')
        emo_list.append(new_list)

    elif spline[1] == 'surprised':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'uneasy':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'confused':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'angry':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'disapproval':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'kiss':
        new_list.append(spline[0])
        new_list.append('1')
        emo_list.append(new_list)

    elif spline[1] == 'smile':
        new_list.append(spline[0])
        new_list.append('1')
        emo_list.append(new_list)

    elif spline[1] == 'frowning':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'evil':
        new_list.append(spline[0])
        new_list.append('-1')
        emo_list.append(new_list)

    elif spline[1] == 'wink':
        new_list.append(spline[0])
        new_list.append('0')
        emo_list.append(new_list)

    elif spline[1] == 'grinning':
        new_list.append(spline[0])
        new_list.append('1')
        emo_list.append(new_list)

    elif spline[1] == 'sift':
        new_list.append(spline[0])
        new_list.append('0')
        emo_list.append(new_list)

    elif spline[1] == 'love':
        new_list.append(spline[0])
        new_list.append('1')
        emo_list.append(new_list)


f = open('emoticon_score.txt','w')

for el in emo_list:
    f.write('\t'.join(el)+'\n')

f.close()
