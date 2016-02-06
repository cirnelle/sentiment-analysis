__author__ = 'yi-linghwong'

import os
import sys
import time


class labMTSentimentAnalysis():

    def create_senti_list(self):

    #################
    # create a sentiment list with their scores, i.e. [['happy', '8.35'], ['laugh', '8.22']]
    #################

        lines = open(path_to_labMT_file, 'r').readlines()

        senti_list = []

        for line in lines:

            list = []

            spline = line.replace('\n','').split('\t')
            list.append(spline[0])
            list.append(spline[2])

            senti_list.append(list)


        f = open('dictionary/labMT_term_list_no_neutral.txt', 'w')

        for sl in senti_list:
            f.write('\t'.join(sl)+'\n')

        f.close()

        return senti_list


    def create_senti_dict(self):

    ################
    # create a sentiment dictionary, i.e {'happy': '8.25, 'happy': '8.46', ...}
    ################

        senti_list = self.create_senti_list()

        senti_dict = {}

        for sl in senti_list:

            # add blank space before and after term
            # so that later we can match whole words to terms in the dictionary
            # instead of substring (e.g. 'go' will be matched to 'going' if no blank space added before and after 'go')

            sl[0] = ' '+sl[0]+' '

            # for positive sentiments, conversion equation is y = x - 4
            if float(sl[1]) > 5.00:

                sl[1] = round((float(sl[1]) - 4.00),2)

                senti_dict[sl[0]] = {'pos':sl[1], 'neg':'0'}

            # for negative sentiments, conversion equation is y = 6 - x

            else:

                sl[1] = round((6.00 - float(sl[1])), 2)


                senti_dict[sl[0]] = {'pos':'0', 'neg':sl[1]}

        print ("Length of sentiment dictionary is "+str(len(senti_dict)))

        return senti_dict

    def create_term_list(self):

    #################
    # create a list of terms, i.e. ['happiness', 'laughing', ...]
    #################

        senti_list = self.create_senti_list()

        term_list = []

        for sl in senti_list:

            term_list.append(sl[0])


        return term_list


    def create_tweet_list(self):

        # create a list of tweets, e.g. ['This is the first tweet', 'This is another tweet', ...]
        # splitlines method to remove '\n' from end of line
        lines = open(path_to_tweet_list).read().splitlines()

        # add blank space to front and end of line for each tweet, in case the ngram is the first or last word in the sentence
        # e.g. ngram = ' the end ', and the tweet is 'that is the end', if we don't add space the ngram won't be detected

        lines=[' '+x+' ' for x in lines]

        return lines

    def calculate_sentiment_score(self):

        senti_dict = self.create_senti_dict()
        tweet_list = self.create_tweet_list()
        term_list = self.create_term_list()

        # add white space to front and end of terms so whole words can be matched

        term_list = [' '+tl+' ' for tl in term_list]

        tweet_score_list = []

        print ("Calculating sentiment score ...")

        t1 = time.time()

        for tl in tweet_list:

            tl = tl.lower()

            tweet_score = []

            string = tl

            pos_score = 0
            neg_score = 0

            for l in term_list:

                substring = l

                if substring in string:

                    print (str(substring)+" pos: "+str(senti_dict[substring]['pos'])+" neg: "+str((senti_dict[substring]['neg'])))

                    pos_score += float(senti_dict[substring]['pos'])
                    neg_score += float(senti_dict[substring]['neg'])

                    # remove the substring from the tweet and replace with space
                    # so that if two adjacent sentiment terms are found they can be detected
                    string = string.replace(substring,' ')


            tweet_score.append(str(round((pos_score),2)))
            tweet_score.append(str(round((neg_score),2)))
            tweet_score.append(tl)

            tweet_score_list.append(tweet_score)

        t2 = time.time()

        total_time = (t2 - t1)/60

        print ("Computing time was "+str(total_time)+" minutes.")

        f = open('results/tweets_senti_score.txt', 'w')

        for tsl in tweet_score_list:
            f.write(', '.join(tsl)+'\n')

        f.close()

        return tweet_score_list



if __name__ == "__main__":

    path_to_labMT_file = 'dictionary/labMT_MASTER_no_neutral.txt'
    path_to_tweet_list = 'test.txt'

    lmt = labMTSentimentAnalysis()
    #lmt.create_senti_list()
    #lmt.create_senti_dict()
    #lmt.create_term_list()
    lmt.calculate_sentiment_score()