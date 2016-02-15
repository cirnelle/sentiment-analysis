__author__ = 'yi-linghwong'

################
# get the mean sentiment from results using different lexicons
# returns a file with mean sentiments and their corresponding tweet
################

import sys
import os
import numpy as np


class GetMeanSentiment():

    def get_sentiments_from_methods(self):

        # SentiStrength

        lines = open(path_to_sentiment_sentistrength,'r').readlines()

        sentistrength = []

        for line in lines:
            spline = line.replace('\n','').split(',')

            sentistrength.append(spline[0])

        print ("Length of SentiStrength list is "+str(len(sentistrength)))

        # SentiWordNet

        lines = open(path_to_sentiment_sentiwordnet,'r').readlines()

        sentiwordnet = []

        for line in lines:
            spline = line.replace('\n','').split(',')

            sentiwordnet.append(spline[0])

        print ("Length of SentiWordNet list is "+str(len(sentiwordnet)))

        # SenticNet

        lines = open(path_to_sentiment_senticnet,'r').readlines()

        senticnet = []

        for line in lines:
            spline = line.replace('\n','').split(',')

            senticnet.append(spline[0])

        print ("Length of SenticNet list is "+str(len(senticnet)))


        return sentistrength,sentiwordnet,senticnet



    def get_mean_sentiments(self):

        senti_lists = self.get_sentiments_from_methods()

        sentistrength = senti_lists[0]
        sentiwordnet = senti_lists[1]
        senticnet = senti_lists[2]

        # output is a zip object which is a list of tuples, i.e. [(pos,neg,neg),(neg,neg,pos),...]

        combined = zip(sentistrength,sentiwordnet,senticnet)

        mean_sentiment = []

        for c in combined:

            c = list(c)

            for i in range(3):

                if c[i] == 'pos':
                    c[i] = 1

                elif c[i] == 'neg':
                    c[i] = -1

                else:
                    print ("error")

            c_mean = np.sum(c)

            if c_mean > 0:
                mean = 'pos'

            elif c_mean < 0:
                mean = 'neg'

            else:
                print ("error")

            mean_sentiment.append(mean)

        return mean_sentiment


    def create_tweet_with_mean_sentiment(self):

        mean_sentiment = self.get_mean_sentiments()

        print ("Length of mean sentiment list is "+str(len(mean_sentiment)))

        lines = open(path_to_sentiment_sentistrength,'r').readlines()

        tweets = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            tweets.append(spline[1])

        print ("Length of tweet list is "+str(len(tweets)))

        combined = zip(mean_sentiment,tweets)

        tweet_mean_senti = []

        for c in combined:

            c = list(c)

            tweet_mean_senti.append(c)


        print ("Length of tweet mean sentiment list is "+str(len(tweet_mean_senti)))

        f = open(path_to_store_tweet_list_with_mean_sentiment,'w')

        for tms in tweet_mean_senti:
            f.write(','.join(tms)+'\n')

        f.close()




if __name__ == '__main__':

    #path_to_sentiment_sentistrength = '../../data_files/labelled_tweets/SA_1.5milliontweets/SentiStrength_results/SA_tweets_senti_polarity.txt'
    #path_to_sentiment_sentiwordnet = '../../data_files/labelled_tweets/SA_1.5milliontweets/SentiWordNet_results/SA_tweets_senti_polarity.txt'
    #path_to_sentiment_senticnet = '../../data_files/labelled_tweets/SA_1.5milliontweets/SenticNet_results/SA_tweets_senti_polarity.txt'
    path_to_sentiment_sentistrength = '../_SentiStrength/results/neutral/sts_gold_neutral_senti_polarity.txt'
    path_to_sentiment_sentiwordnet = '../_SentiWordNet/results/neutral/sts_gold_neutral_senti_polarity.txt'
    path_to_sentiment_senticnet = '../_SenticNet/results/neutral/sts_gold_neutral_senti_polarity.txt'

    path_to_store_tweet_list_with_mean_sentiment = '../_combined/neutral/sts_gold_neutral_senti_polarity.txt'

    ms = GetMeanSentiment()
    #ms.get_sentiments_from_methods()
    #ms.get_mean_sentiments()
    ms.create_tweet_with_mean_sentiment()
