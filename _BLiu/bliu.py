#!/usr/local/bin/python3

__author__ = 'yi-linghwong'

##################
# calculate sentiment of tweets using list of pos and neg words by B Liu
##################

import sys
import os
import time


class BLiu():
    def remove_duplicates(self):

        lines = open('dictionary/all_words.txt', 'r').readlines()

        words = []

        for line in lines:
            spline = line.replace('\n', '').split(',')
            words.append(spline[0])

        print(len(words))

        nodup = []

        for w in words:
            if w not in nodup:
                nodup.append(w)

            else:
                print(w)

    def combine_dicts(self):

        # positive words

        lines = open('dictionary/positive_words.txt', 'r').readlines()

        pos_words = []

        for line in lines:
            spline = line.replace('\n', '')
            pos_words.append([spline, '1'])

        print("Length of pos words is " + str(len(pos_words)))

        f = open('dictionary/pos_words_score.txt', 'w')

        for pw in pos_words:
            f.write(','.join(pw) + '\n')

        f.close()

        # negative words

        lines = open('dictionary/negative_words.txt', 'r').readlines()

        neg_words = []

        for line in lines:
            spline = line.replace('\n', '')
            neg_words.append([spline, '-1'])

        print("Length of neg words is " + str(len(neg_words)))

        f = open('dictionary/neg_words_score.txt', 'w')

        for nw in neg_words:
            f.write(','.join(nw) + '\n')

        f.close()

        # combined

        combined_words = pos_words + neg_words

        print("Length of combined list is " + str(len(combined_words)))

        f = open('dictionary/all_words.txt', 'w')

        for cw in combined_words:
            f.write(','.join(cw) + '\n')

        f.close()

    def create_senti_dict(self):

        lines = open(path_to_sentiment_dictionary, 'r').readlines()

        senti_dict = {}

        print("Creating sentiment dictionary ...")

        for line in lines:
            spline = line.replace("\n", "").split(',')

            # add blank space before and after term
            # so that later we can match whole words to terms in the dictionary
            # instead of substring (e.g. 'go' will be matched to 'going' if no blank space added before and after 'go')

            spline[0] = ' ' + spline[0] + ' '

            senti_dict[spline[0]] = spline[1]

        print("Length of sentiment dictionary is " + str(len(senti_dict)))

        return senti_dict

    def create_tweet_list(self):

        # create a list of tweets, e.g. ['This is the first tweet', 'This is another tweet', ...]
        # splitlines method to remove '\n' from end of line
        lines = open(path_to_processed_tweet_file).read().splitlines()

        # add blank space to front and end of line for each tweet, in case the ngram is the first or last word in the sentence
        # e.g. ngram = ' the end ', and the tweet is 'that is the end', if we don't add space the ngram won't be detected

        lines = [' ' + x + ' ' for x in lines]

        return lines

    def create_word_list(self):

        word_list = []

        lines = open(path_to_sentiment_dictionary, 'r').readlines()

        print("Creating word list ...")

        for line in lines:
            spline = line.replace('\n', '').split(',')
            word_list.append(spline[0])

        print(len(word_list))

        return word_list

    def calculate_senti_score(self):

        senti_dict = self.create_senti_dict()
        tweet_list = self.create_tweet_list()
        word_list = self.create_word_list()

        # add white space to front and end of terms so whole words can be matched

        word_list = [' ' + wl + ' ' for wl in word_list]

        print("Length of tweet list is " + str(len(tweet_list)))

        tweet_score_list = []
        tweet_score_list_polarity = []

        print("Calculating sentiment score ...")

        t1 = time.time()

        for tl in tweet_list:

            tl = tl.lower()

            tweet_score = []
            tweet_score_c = []

            string = tl

            senti_score = 0

            for wl in word_list:

                substring = wl

                if substring in string:

                    senti_score += int(senti_dict[substring])

                    # print ("Pos score is "+str(pos_score))
                    # print ("Neg score is "+str(neg_score))

            tweet_score.append(str(senti_score))
            tweet_score.append(tl)

            tweet_score_list.append(tweet_score)

            # calculate the polarity (i.e. 'pos', 'neg' or 'neutral')

            if senti_score > 0:
                tweet_score_c.append('pos')

            elif senti_score < 0:

                tweet_score_c.append('neg')

            # if tweet has neutral score classify it as negative (only for datasets that do not have neutral!)
            elif senti_score == 0:
                tweet_score_c.append('neutral')

            else:
                print("error")

            tweet_score_c.append(tl)
            tweet_score_list_polarity.append(tweet_score_c)

        t2 = time.time()

        total_time = round(((t2 - t1) / 60),2)

        print("Computing time was " + str(total_time) + " minutes.")

        f = open(path_to_store_results_score, 'w')

        for tsl in tweet_score_list:
            f.write(','.join(tsl) + '\n')

        f.close()

        f = open(path_to_store_results_polarity, 'w')

        for tslp in tweet_score_list_polarity:
            f.write(','.join(tslp) + '\n')

        f.close()

        return tweet_score_list


if __name__ == "__main__":

    path_to_sentiment_dictionary = 'dictionary/all_words.txt'

    path_to_processed_tweet_file = sys.argv[1]
    #path_to_processed_tweet_file = '../tweets/preprocessed_tweets_sts_gold.txt'
    #path_to_processed_tweet_file = '../_emoticon/results/neutral/SA_neutral.txt'
    #path_to_processed_tweet_file = '../../data_files/labelled_tweets/SA/preprocessed_tweets_SA.txt'

    path_to_store_results_score = sys.argv[2]
    #path_to_store_results_score = 'results/sts_gold_tweets_senti_score.txt'
    #path_to_store_results_score = 'results/neutral/emoticon_SA_senti_score.txt'
    #path_to_store_results_score = '../../data_files/labelled_tweets/SA/BLiu_results/SA_tweets_senti_score.txt'

    path_to_store_results_polarity = sys.argv[3]
    #path_to_store_results_polarity = 'results/sts_gold_tweets_senti_polarity.txt'
    #path_to_store_results_polarity = 'results/neutral/emoticon_SA_senti_polarity.txt'
    #path_to_store_results_polarity = '../../data_files/labelled_tweets/SA/BLiu_results/SA_tweets_senti_polarity.txt'

    bl = BLiu()

    #bl.remove_duplicates()
    #bl.combine_dicts()
    #bl.create_senti_dict()
    #bl.create_tweet_list()
    #bl.create_word_list()
    bl.calculate_senti_score()

