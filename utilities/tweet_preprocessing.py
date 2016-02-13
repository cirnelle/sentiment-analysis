__author__ = 'yi-linghwong'


import re
import sys
import os
import html.entities as htmlentitydefs


class TweetPreprocessing():



    def remove_url_mention_hashtag(self):

        tweet_list = []

        lines = open(path_to_raw_tweet, 'r').readlines()

        print ("Removing URL, mentions and hashtags...")

        for line in lines:

            #remove URLs
            t1 = re.sub(r'(?:https?\://)\S+', '', line)


            #remove mentions
            t2 = re.sub(r'(?:\@)\S+', '', t1)

            #remove hashtags (just the symbol, not the key word)

            t3 = re.sub(r"#","", t2).strip()

            # replace &amp; with 'and'

            t4 = re.sub(r"&amp;", "and", t3).strip()

            # replace &amp with 'and'

            t5 = re.sub(r"&amp", "and", t4).strip()

            # replace <3 with 'love'

            t6 = re.sub(r"<3", "love", t5).strip()

            tweet_list.append(t6)

        return tweet_list


    def expand_contraction(self):

        contractions_dict = {
            ' isn\'t ': ' is not ',
            ' isn’t ': ' is not ',
            ' isnt ': ' is not ',
            ' aren\'t ': ' are not ',
            ' aren’t ': ' are not ',
            ' arent ': ' are not ',
            ' wasn\'t ': ' was not ',
            ' wasn’t ': ' was not ',
            ' wasnt ': ' was not ',
            ' weren\'t ': ' were not ',
            ' weren’t ': ' were not ',
            ' werent ': ' were not ',
            ' haven\'t ': ' have not ',
            ' haven’t ': ' have not ',
            ' havent ': ' have not ',
            ' hasn\'t ': ' has not ',
            ' hasn’t ': ' has not ',
            ' hasnt ': ' has not ',
            ' hadn\'t ': ' had not ',
            ' hadn’t ': ' had not ',
            ' hadnt ': ' had not ',
            ' won\'t ': ' will not ',
            ' won’t ': ' will not ',
            ' wouldn\'t ': ' would not ',
            ' wouldn’t ': ' would not ',
            ' wouldnt ': ' would not ',
            ' didn\'t ': ' did not ',
            ' didn’t ': ' did not ',
            ' didnt ': ' did not ',
            ' don\'t ': ' do not ',
            ' don’t ': ' do not ',
            ' dont ': ' do not ',
            ' doesn\'t ': ' does not ',
            ' doesn’t ': ' does not ',
            ' doesnt ': ' does not ',
            ' can\'t ': ' can not ',
            ' can’t ': ' can not ',
            ' cant ': ' can not ',
            ' couldn\'t ': ' could not ',
            ' couldn’t ': ' could not ',
            ' couldnt ': ' could not ',
            ' shouldn\'t ': ' should not ',
            ' shouldn’t ': ' should not ',
            ' shouldnt ': ' should not ',
            ' mightn\'t ': ' might not ',
            ' mightn’t ': ' might not ',
            ' mightnt ': ' might not ',
            ' mustn\'t ': ' must not ',
            ' mustn’t ': ' must not ',
            ' mustnt ': ' must not ',
            ' shan\'t ': ' shall not ',
            ' shan’t ': ' shall not ',
            ' shant ': ' shall not ',
        }

        list = self.remove_url_mention_hashtag()
        tweet_list = []

        contractions_re = re.compile('(%s)' % '|'.join(contractions_dict.keys()), re.IGNORECASE)


        def replace(match):

            return contractions_dict[match.group(0).lower()]

        print ("Expanding contractions ...")

        for l in list:

            tweet_list.append(contractions_re.sub(replace, l))

        return tweet_list


    def replace_emoticon(self):

        ###################
        # Create emoticon dictionary from tsv
        ##################

        emoticon_dict = {}

        lines  = open(path_to_emoticon_dictionary, 'r').readlines()

        for line in lines:

            spline = line.replace('\n', '').split('\t')
            spline[0] = ' '+spline[0]+' '

            emoticon_dict[spline[0]] = spline[1]


        ####################
        # The emoticon regex list below is a modified version taken from Chris Pott's tokenizer script
        ####################

        # the smiley ':-\' is compiled as ':-\\'

        emoticon_string = r"""
            (?:
              [<>]?
              [:;=8^%xX]                     # eyes
              [\-o\*\'\.\_]?                 # optional nose
              [\)\]\(\[dDpP/\:\}\{@\|\\\*\>\<\0\O\^] # mouth
              |
              [\)\]\(\[dDpP/\:\}\{@\|\\\*\>\<\0\O\^] # mouth
              [\-o\*\'\.\_]?                 # optional nose
              [:;=8^%xX]                     # eyes
              [<>]?
            )"""

        ######################



        list = self.expand_contraction()

        # add blank space to front and end of line for each tweet, in case the emoticon is the first or last word in the sentence
        # e.g. if tweet is "this is a tweet ;)' the smiley face won't be detected because there is no space after it!

        list=[' '+l+' ' for l in list]

        tweet_list = []

        emoticon_re = re.compile(emoticon_string, re.VERBOSE | re.I | re.UNICODE)

        print ("replacing emoticons ...")

        for l in list:

            # re.findall() method returns all non-overlapping matches of pattern in string, as a list of strings.(e.g. [':)', ':-(']
            emoticon = emoticon_re.findall(l)

            # add space to front and end of emoticon so that whole emoticon can be detected
            # otherwise substring of string will also be replaced (e.g. explain => eplayfullain)
            emoticon = [' '+e+' ' for e in emoticon]


            # if no emoticons in tweet, append the tweet to tweet list unchanged
            if emoticon == []:
                #print ("no emoticon in this tweet")
                tweet_list.append(l)

            else:

                for e in emoticon:

                    key = e

                    if key in emoticon_dict:

                        #print ("emoticon "+str(e)+" in dict")

                        # add space to front and end of value (e.g. 'happy') too!
                        # to avoid situation e.g. sethappyto
                        el = l.replace(e, ' '+emoticon_dict[e]+' ')

                        # the following line makes sure that if there are more than one emoticon in the tweet,
                        # all emoticons are replaced
                        l = el

                    else:
                        #print ("emoticon "+str(e)+" not in dict")
                        el = l.replace(e,' ')
                        l = el

                tweet_list.append(el)

        return tweet_list

    def remove_punctuation(self):

        #####################
        # Need to remove punctuation because of slang lookup (and also ngram lookup)
        # e.g. 'ur' is replaced with 'you are' in slang dict, but if tweet contains 'i am ur, so i come'
        # 'ur,' wil be a word, and won't match the key in dict
        # this step must only happen after replace_emoticons and expand_contractions!
        #####################

        # Replace punctuation with white space, not nil! So that words won't join together when punctuation is removed

        tweet_list = []

        list = self.replace_emoticon()

        print ("Removing punctuations ...")

        for l in list:

            #remove special characters
            tweet = re.sub("[^A-Za-z0-9]+",' ', l)

            tweet_list.append(tweet)

        return tweet_list


    def replace_slang(self):

        ###################
        # Create slang dictionary from tsv
        ##################

        slang_dict = {}
        slang_list = []

        lines  = open(path_to_slang_dictionary, 'r').readlines()

        print ("Replacing slangs ...")

        for line in lines:

            spline = line.replace('\n', '').split('\t')
            slang_dict[spline[0]] = spline[1]
            slang_list.append(spline[0])


        # remember to make all lower case! emoticons must be processed before slangs.

        list = self.remove_punctuation()

        tweet_list = []

        for l in list:

        # IMPORTANT! must split the sentence into words
        # cannot directly match substsring to string
        # otherwise mistakes such as this will occur: 'ur here because our' ==> 'you are here because oyou are'
        # ALTERNATIVELY: add space to front and back of the slang terms in the dictionary, then no need to split string

            tl = l.lower().split()

            for sl in slang_list:

                if sl in tl:

                    tl = [slang_dict[sl] if x==sl else x for x in tl] #!important!

            # stitch the list of strings together into one single string
            final_tweet = ' '.join(tl)

            final_tweet = final_tweet.lower()


            tweet_list.append(final_tweet)


        f = open(path_to_store_preprocessed_tweets, 'w')

        for tl in tweet_list:
            f.write(tl+'\n')

        f.close()

        return (tweet_list)



if __name__ == "__main__":

    path_to_raw_tweet = '../tweets/raw_tweets_SS_noneutral.txt'
    path_to_emoticon_dictionary = '../emoticons/emo_dict.txt'
    path_to_slang_dictionary = '../slangs/SlangLookupTable.txt'
    path_to_store_preprocessed_tweets = '../tweets/preprocessed_tweets_SS_noneutral.txt'

    tp = TweetPreprocessing()
    #tp.remove_url_mention_hashtag()
    #tp.expand_contraction()
    #tp.replace_emoticon()
    #tp.remove_punctuation()
    tp.replace_slang()



