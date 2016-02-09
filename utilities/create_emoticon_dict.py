__author__ = 'yi-linghwong'

import sys


lines = open('emoticons/emoticons.txt', 'r').readlines()


list = []

for line in lines:

    line = line.replace('\n', '')
    l = []

    try:
        if '>:)'in line or '>:-)' in line or '>;)' in line or '>;-)' in line or '(:<' in line or '(-:<' in line or '(;<' in line or '(-;<' in line:
            l.append(line)
            l.append('evil')
            list.append(l)
            continue
    except:
        pass


    try:

        if '>:(' in line or '>:-(' in line or '>:O' in line or '>:0' in line or '):<' in line or ')-:<' in line or 'O:<' in line or '0:<' in line:
            l.append(line)
            l.append('angry')
            list.append(l)
            continue
    except:
        pass

    try:
        if '^^' in line or '^.^' in line or 'xD' in line or 'XD' in line or 'x-D' in line or 'X-D' in line:
            l.append(line)
            l.append('grinning')
            list.append(l)
            continue

    except:
        pass

    try:

        if '<3' in line:
            l.append(line)
            l.append('love')
            list.append(l)
            continue
    except:
        pass

    try:

        if ';-)' in line or ';)' in line or '(-;' in line or '(;' in line:
            l.append(line)
            l.append('wink')
            list.append(l)
            continue

    except:
        pass

    try:

        if line[1] == '\\' or line[2] == '\\' or line[3] == '\\':
            l.append(line)
            l.append('confused')
            list.append(l)
            continue
    except:
        pass

    try:
        if line[1] == ')' or line[2] == ')' or line[3] == ')':
            l.append(line)
            l.append('happy')
            list.append(l)
            continue
    except:
        pass

    try:

        if line[1] == ']' or line[2] == ']' or line[3] == ']':
            l.append(line)
            l.append('happy')
            list.append(l)
            continue
    except:
        pass


    try:

        if line.index('(') == 1 or line.index('(') == 2 or line.index('(') == 3:
            l.append(line)
            l.append('sad')
            list.append(l)
            continue
    except:
        pass


    try:

        if line.index('[') == 1 or line.index('[') == 2 or line.index('[') == 3:
            l.append(line)
            l.append('sad')
            list.append(l)
            continue
    except:
        pass

    try:

        if line.index('d') == 1 or line.index('d') == 2 or line.index('d') == 3:
            l.append(line)
            l.append('happy')
            list.append(l)
            continue
    except:
        pass

    
    try:

        if line.index('D') == 1 or line.index('D') == 2 or line.index('D') == 3:
            l.append(line)
            l.append('happy')
            list.append(l)
            continue
    except:pass
    
    try:

        if line.index('p') == 1 or line.index('p') == 2 or line.index('p') == 3:
            l.append(line)
            l.append('playful')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('P') == 1 or line.index('P') == 2 or line.index('P') == 3:
            l.append(line)
            l.append('playful')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('/') == 1 or line.index('/') == 2 or line.index('/') == 3:
            l.append(line)
            l.append('uneasy')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('}') == 1 or line.index('}') == 2 or line.index('}') == 3:
            l.append(line)
            l.append('happy')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('{') == 1 or line.index('{') == 2 or line.index('{') == 3:
            l.append(line)
            l.append('sad')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('@') == 1 or line.index('@') == 2 or line.index('@') == 3:
            l.append(line)
            l.append('angry')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('|') == 1 or line.index('|') == 2 or line.index('|') == 3:
            l.append(line)
            l.append('disapproval')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('*') == 1 or line.index('*') == 2 or line.index('*') == 3:
            l.append(line)
            l.append('kiss')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('>') == 1 or line.index('>') == 2 or line.index('>') == 3:
            l.append(line)
            l.append('smile')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('<') == 1 or line.index('<') == 2 or line.index('<') == 3:
            l.append(line)
            l.append('frowning')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('0') == 1 or line.index('0') == 2 or line.index('0') == 3:
            l.append(line)
            l.append('surprised')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('O') == 1 or line.index('O') == 2 or line.index('O') == 3:
            l.append(line)
            l.append('surprised')
            list.append(l)
            continue
    except:pass

    try:

        if line.index(')') == 0:
            l.append(line)
            l.append('sad')
            list.append(l)
            continue
    except:pass

    try:

        if line.index(']') == 0:
            l.append(line)
            l.append('sad')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('(') == 0:
            l.append(line)
            l.append('happy')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('[') == 0:
            l.append(line)
            l.append('happy')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('d') == 0:
            l.append(line)
            l.append('playful')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('D') == 0:
            l.append(line)
            l.append('surprised')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('p') == 0:
            l.append(line)
            l.append('playful')
            list.append(l)
    except:pass

    try:

        if line.index('P') == 0:
            l.append(line)
            l.append('playful')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('/') == 0:
            l.append(line)
            l.append('uneasy')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('}') == 0:
            l.append(line)
            l.append('sad')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('{') == 0:
            l.append(line)
            l.append('happy')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('@') == 0:
            l.append(line)
            l.append('angry')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('|') == 0:
            l.append(line)
            l.append('disapproval')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('*') == 0:
            l.append(line)
            l.append('kiss')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('>') == 0:
            l.append(line)
            l.append('frowning')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('<') == 0:
            l.append(line)
            l.append('smile')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('0') == 0:
            l.append(line)
            l.append('surprised')
            list.append(l)
            continue
    except:pass

    try:

        if line.index('O') == 0:
            l.append(line)
            l.append('surprised')
            list.append(l)
            continue
    except:pass

    '''

    try:

        if line.index(':') == 1 or line.index(':') == 2 or line.index(':') == 3:

            l.append(line)
            l.append('sift')
            list.append(l)
            continue
    except:pass

    try:

        if line.index(':') == 0:

            l.append(line)
            l.append('sift')
            list.append(l)
            continue
    except:pass

    '''



f = open('emoticons/emo_dict.txt', 'w')

for l in list:

    f.write('\t'.join(l)+'\n')



f.close()