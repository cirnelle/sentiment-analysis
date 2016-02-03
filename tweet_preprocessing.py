__author__ = 'yi-linghwong'


import re
import sys
import os
import html.entities as htmlentitydefs


class TweetPreprocessing():



    def remove_url_mention_hashtag(self):
        tweet_list = []

        lines = open('test.txt', 'r').readlines()

        for line in lines:

            #remove URLs
            t1 = re.sub(r'(?:https?\://)\S+', '', line)


            #remove mentions
            t2 = re.sub(r'(?:\@)\S+', '', t1)

            #remove hashtags (just the symbol, not the key word)

            t3 = re.sub(r"#","", t2).strip()

            # replace &amp; with 'and'

            t4 = re.sub(r"&amp;", "and", t3).strip()

            tweet_list.append(t4)

        return tweet_list

    def expand_contraction(self):

        contractions_dict = {
            'isn\'t': 'is not',
            'isnt': 'is not',
            'aren\'t': 'are not',
            'arent': 'are not',
            'wasn\'t': 'was not',
            'wasnt': 'was not',
            'weren\'t': 'were not',
            'werent': 'were not',
            'haven\'t': 'have not',
            'havent': 'have not',
            'hasn\'t': 'has not',
            'hasnt': 'has not',
            'hadn\'t': 'had not',
            'hadnt': 'had not',
            'won\'t': 'will not',
            'wouldn\'t': 'would not',
            'wouldnt': 'would not',
            'didn\'t': 'did not',
            'didnt' : 'did not',
            'don\'t' : 'do not',
            'dont' : 'do not',
            'doesn\'t': 'does not',
            'doesnt': 'does not',
            'can\'t': 'can not',
            'cant': 'can not',
            'couldn\'t': 'could not',
            'couldnt': 'could not',
            'shouldn\'t': 'should not',
            'shouldnt': 'should not',
            'mightn\'t': 'might not',
            'mightnt': 'might not',
            'mustn\'t': 'must not',
            'mustnt': 'must not',
            'shan\'t': 'shall not',
            'shant': 'shall not',
            }

        list = self.remove_url_mention_hashtag()
        tweet_list = []



        contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()), re.IGNORECASE)


        def replace(match):

            return contractions_dict[match.group(0).lower()]

        for l in list:

            tweet_list.append(contractions_re.sub(replace, l))

        return tweet_list


    def replace_emoticon(self):

        ####################
        # The regex list below is taken from Chris Pott's tokenizer script
        ####################

        # the smiley ':-\' is compiled as ':-\\'

        emoticon_dict = {':)': 'happy', ':-(': 'disappointed', ':*': 'kiss'}

        emoticon_string = r"""
            (?:
              [<>]?
              [:;=8^]                     # eyes
              [\-o\*\'.]?                 # optional nose
              [\)\]\(\[dDpP/\:\}\{@\|\\\*\>\<\0\O] # mouth
              |
              [\)\]\(\[dDpP/\:\}\{@\|\\\*\>\<\0\O] # mouth
              [\-o\*\'.]?                 # optional nose
              [:;=8^]                     # eyes
              [<>]?
            )"""

        ######################

        list = self.expand_contraction()

        tweet_list = []


        for l in list:

            emoticon_re = re.compile(emoticon_string, re.VERBOSE | re.I | re.UNICODE)

            # re.findall() method returns all non-overlapping matches of pattern in string, as a list of strings.(e.g. [':)', ':-(']
            emoticon = emoticon_re.findall(l)

            # if no emoticons in tweet, append the tweet to tweet list unchanged
            if emoticon == []:
                tweet_list.append(l)

            else:

                for e in emoticon:

                    el = l.replace(e, emoticon_dict[e])

                    # the following line makes sure that if there are more than one emoticon in the tweet,
                    # all emoticons are replaced
                    l = el

                tweet_list.append(el)

        print (tweet_list)
        print (len(tweet_list))


if __name__ == "__main__":

    tp = TweetPreprocessing()
    #tp.remove_url_mention_hashtag()
    #tp.expand_contraction()
    tp.replace_emoticon()



