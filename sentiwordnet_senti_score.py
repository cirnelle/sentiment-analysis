__author__ = 'yi-linghwong'

import os
import sys
import time


class SentiWordNetScore():

    def create_senti_dict(self):

        lines = open('test.txt', 'r').readlines()

        senti_dict = {}

        for line in lines:
            spline = line.replace("\n","").split(', ')

            senti_dict[spline[0]] = {'pos':spline[1],'neg':spline[2]}

        return senti_dict


    def create_tweet_list(self):

        # create a list of tweets, e.g. ['This is the first tweet', 'This is another tweet', ...]
        # splitlines method to remove '\n' from end of line
        lines = open('tweets.txt').read().splitlines()

        return lines


    def create_ngram_list(self):

        ngram_list = []

        lines = open('test.txt', 'r').readlines()

        for line in lines:
            spline = line.replace('\n', '').split(', ')
            ngram_list.append(spline[0])


        return ngram_list


    def calculate_senti_score(self):

        senti_dict = self.create_senti_dict()
        tweet_list = self.create_tweet_list()
        ngram_list = self.create_ngram_list()

        tweet_score_list = []


        for tl in tweet_list:

            tweet_score = []

            string = tl

            pos_score = 0
            neg_score = 0


            for nl in ngram_list:

                substring = nl

                if substring in string:

                    print (str(substring)+" found")
                    pos_score += float(senti_dict[substring]['pos'])
                    neg_score += float(senti_dict[substring]['neg'])

                    # remove the substring (which are ngrams) from the tweet
                    string = string.replace(substring,'')

                    print ("Pos score is "+str(pos_score))
                    print ("Neg score is "+str(neg_score))

            tweet_score.append(pos_score)
            tweet_score.append(neg_score)
            tweet_score.append(tl)

            tweet_score_list.append(tweet_score)

        print (tweet_score_list)








if __name__ == "__main__":

    swn = SentiWordNetScore()

    #swn.create_senti_dict()

    #swn.create_tweet_list()

    #swn.create_ngram_list()

    swn.calculate_senti_score()
