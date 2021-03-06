__author__ = 'yi-linghwong'

import sys
import os


class ProcessLabelledTweets():

    def create_raw_tweet_sts_gold(self):

    ############
    # extract only the raw tweets from labelled file
    ############

        lines = open(path_to_labelled_tweet_file_sts_gold, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        raw_tweets = []

        for line in lines:

            spline = line.replace('\n','').split(';')

            # there are semicolons ; in the tweet as well, so need to join them into one tweet
            joined = ' '.join(spline[2:])

            new_list = [spline[0],spline[1],joined]
            if len(new_list) == 3:
                raw_tweets.append(new_list[2])

            else:
                print ("error")
                print (line)

        print ("Length of raw tweet is "+str(len(raw_tweets)))

        f = open(path_to_store_raw_tweets_sts_gold,'w')

        for rt in raw_tweets:
            f.write(rt+'\n')

        f.close()

        return raw_tweets


    def convert_labels_sts_gold(self):

    ############
    # convert the labels of labelled tweets to 'pos', 'neg'
    ############

        lines = open(path_to_labelled_tweet_file_sts_gold, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        tweet_sentiment_list = []

        for line in lines:

            tweet_sentiment = []

            spline = line.replace('\n','').split(';')

            # there are semicolons ; in the tweet as well, so need to join them into one tweet

            joined = ' '.join(spline[2:])

            new_list = [spline[1],joined]

            if new_list[0] == '"0"':

                tweet_sentiment.append('neg')

            elif new_list[0] == '"4"':

                tweet_sentiment.append('pos')

            else:
                print ("error")
                print (spline)

            tweet_sentiment.append(new_list[1])
            tweet_sentiment_list.append(tweet_sentiment)

        print ("Length of labelled tweet list is "+str(len(tweet_sentiment_list)))

        f = open(path_to_store_labelled_tweets_sts_gold,'w')

        for tsl in tweet_sentiment_list:
            f.write(','.join(tsl)+'\n')

        f.close()

        return tweet_sentiment_list

    def create_raw_tweet_SA(self):

    ###############
    # Extract only raw tweets from the Sentiment Analysis Dataset (which contains around 1.5 million tweets)
    ###############

        lines = open(path_to_labelled_tweet_file_SA, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        raw_tweets = []

        for line in lines:

            spline = line.replace('\n','').split(',')

            # in case there are commas in the tweet as well, so need to join them into one tweet
            joined = ' '.join(spline[3:])

            new_list = [spline[1],joined]
            if len(new_list) == 2:
                raw_tweets.append(new_list[1])

            else:
                print ("error")
                print (line)

        print ("Length of raw tweet is "+str(len(raw_tweets)))

        f = open(path_to_store_raw_tweets_SA,'w')

        for rt in raw_tweets:
            f.write(rt+'\n')

        f.close()

        return raw_tweets

    def convert_labels_SA(self):

    ############
    # convert the labels of labelled tweets to 'pos', 'neg' for Sentiment Analysis Dataset (1.5 million tweets)
    ############

        lines = open(path_to_labelled_tweet_file_SA, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        tweet_sentiment_list = []

        for line in lines:

            tweet_sentiment = []

            spline = line.replace('\n','').split(',')

            # in case there are commas in the tweet as well, so need to join them into one tweet

            joined = ' '.join(spline[3:])

            new_list = [spline[1],joined]

            if new_list[0] == '0':

                tweet_sentiment.append('neg')

            elif new_list[0] == '1':

                tweet_sentiment.append('pos')

            else:
                print ("error")
                print (spline)

            tweet_sentiment.append(new_list[1])
            tweet_sentiment_list.append(tweet_sentiment)

        print ("Length of labelled tweet list is "+str(len(tweet_sentiment_list)))

        f = open(path_to_store_labelled_tweets_SA,'w')

        for tsl in tweet_sentiment_list:
            f.write(','.join(tsl)+'\n')

        f.close()

        return tweet_sentiment_list


    def create_raw_tweet_SS(self):

    ###############
    # Extract only raw tweets from the SentiStrength Dataset
    ###############

        lines = open(path_to_labelled_tweet_file_SS, 'r', encoding='ISO-8859-1').readlines()

        print ("Length of input list is "+str(len(lines)))

        raw_tweets = []

        for line in lines:

            spline = line.replace('\n','').split('\t')

            # in case there are tabs in the tweet as well, so need to join them into one tweet
            joined = ' '.join(spline[2:])

            new_list = [spline[0],spline[1],joined]

            senti_score = int(new_list[0]) - int(new_list[1])

            if len(new_list) == 3:

                # the following THREE lines are only for if we don't want to include neutral sentiments!

                if senti_score == 0:

                    continue

                else:

                    raw_tweets.append(new_list[2])

            else:
                print ("error")
                print (line)

        print ("Length of raw tweet is "+str(len(raw_tweets)))

        f = open(path_to_store_raw_tweets_SS,'w')

        for rt in raw_tweets:
            f.write(rt+'\n')

        f.close()

        return raw_tweets

    def convert_labels_SS(self):

    ############
    # convert the labels of labelled tweets to 'pos', 'neg' for SentiStrength dataset
    ############

        lines = open(path_to_labelled_tweet_file_SS, 'r', encoding='ISO-8859-1').readlines()

        print ("Length of input list is "+str(len(lines)))

        tweet_sentiment_list = []

        for line in lines:

            tweet_sentiment = []

            spline = line.replace('\n','').split('\t')

            # in case there are tabs in the tweet as well, so need to join them into one tweet
            joined = ' '.join(spline[2:])

            new_list = [spline[0],spline[1],joined]

            senti_score = int(new_list[0]) - int(new_list[1])

            if senti_score > 0:

                tweet_sentiment.append('pos')

            elif senti_score < 0:

                tweet_sentiment.append('neg')

            elif senti_score == 0:

                #tweet_sentiment.append('neutral')
                continue

            else:
                print ("error")

            tweet_sentiment.append(new_list[2])
            tweet_sentiment_list.append(tweet_sentiment)

        print ("Length of labelled tweet list is "+str(len(tweet_sentiment_list)))

        f = open(path_to_store_labelled_tweets_SS,'w')

        for tsl in tweet_sentiment_list:
            f.write(','.join(tsl)+'\n')

        f.close()

        return tweet_sentiment_list

    def create_raw_tweet_stanford(self):

        lines = open(path_to_labelled_tweet_file_stanford, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        raw_tweets = []

        for line in lines:

            spline = line.replace('\n','').split(',')

            # there are commas in the tweet as well, so need to join them into one tweet
            joined = ' '.join(spline[5:])

            new_list = [spline[0],joined]
            if len(new_list) == 2:
                raw_tweets.append(new_list[1])

            else:
                print ("error")
                print (line)

        print ("Length of raw tweet is "+str(len(raw_tweets)))

        f = open(path_to_store_raw_tweets_stanford,'w')

        for rt in raw_tweets:
            f.write(rt+'\n')

        f.close()

        # create no neutral raw tweets

        lines = open(path_to_labelled_tweet_file_stanford, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        raw_tweets_noneutral = []
        neutral = []

        for line in lines:

            spline = line.replace('\n','').split(',')

            # there are commas in the tweet as well, so need to join them into one tweet
            joined = ' '.join(spline[5:])

            new_list = [spline[0],joined]

            if new_list[0] != '"2"':
                if len(new_list) == 2:
                    raw_tweets_noneutral.append(new_list[1])

                else:
                    print ("error")
                    print (line)

            elif new_list[0] == '"2"':
                if len(new_list) == 2:
                    neutral.append(new_list[1])

                else:
                    print ("error")
                    print (line)

            else:
                print ("error occured")

        print ("Length of raw tweet noneutral is "+str(len(raw_tweets_noneutral)))

        f = open(path_to_store_raw_tweets_stanford_noneutral,'w')

        for rtn in raw_tweets_noneutral:
            f.write(rtn+'\n')

        f.close()

        return raw_tweets

    def convert_labels_stanford(self):

        lines = open(path_to_labelled_tweet_file_stanford, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        tweet_sentiment_list = []

        for line in lines:

            tweet_sentiment = []

            spline = line.replace('\n','').split(',')

            # there are commas in the tweet as well, so need to join them into one tweet

            joined = ' '.join(spline[5:])

            new_list = [spline[0],joined]

            if new_list[0] == '"0"':

                tweet_sentiment.append('neg')

            elif new_list[0] == '"4"':

                tweet_sentiment.append('pos')

            elif new_list[0] == '"2"':

                tweet_sentiment.append('neutral')

            else:
                print ("error")
                print (new_list)

            tweet_sentiment.append(new_list[1])
            tweet_sentiment_list.append(tweet_sentiment)

        print ("Length of labelled tweet list is "+str(len(tweet_sentiment_list)))

        f = open(path_to_store_labelled_tweets_stanford,'w')

        for tsl in tweet_sentiment_list:
            f.write(','.join(tsl)+'\n')

        f.close()

        # create no neutral labelled tweets

        lines = open(path_to_labelled_tweet_file_stanford, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        tweet_sentiment_noneutral_list = []
        neutral = []

        for line in lines:

            tweet_sentiment_noneutral = []

            spline = line.replace('\n','').split(',')

            # there are commas in the tweet as well, so need to join them into one tweet

            joined = ' '.join(spline[5:])

            new_list = [spline[0],joined]

            if new_list[0] == '"0"':

                tweet_sentiment_noneutral.append('neg')
                tweet_sentiment_noneutral.append(new_list[1])

            elif new_list[0] == '"4"':

                tweet_sentiment_noneutral.append('pos')
                tweet_sentiment_noneutral.append(new_list[1])

            elif new_list[0] == '"2"':

                neutral.append('neutral')
                continue

            else:
                print ("error")
                print (spline)

            tweet_sentiment_noneutral_list.append(tweet_sentiment_noneutral)

        print ("Length of labelled tweet noneutral list is "+str(len(tweet_sentiment_noneutral_list)))

        f = open(path_to_store_labelled_tweets_stanford_noneutral,'w')

        for tsnl in tweet_sentiment_noneutral_list:
            f.write(','.join(tsnl)+'\n')

        f.close()

    def create_raw_tweets_semeval(self):

        lines = open(path_to_labelled_tweet_file_semeval, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        raw_tweets = []

        for line in lines:

            spline = line.replace('\n','').split('\t')

            # skip lines with error
            if (len(spline)) > 1:

                # in case there are tabs in the tweet as well, so need to join them into one tweet
                joined = ' '.join(spline[5:])

                new_list = [spline[4],joined]

                if (new_list[0] == 'positive' or new_list[0] == 'negative'):

                    if len(new_list) == 2:
                        raw_tweets.append(new_list[1])

                    else:
                        print ("error")
                        print (line)
                else:
                    continue

        print ("Length of raw tweet is "+str(len(raw_tweets)))

        f = open(path_to_store_raw_tweets_semeval,'w')

        for rt in raw_tweets:
            f.write(rt+'\n')

        f.close()


    def convert_labels_semeval(self):

        lines = open(path_to_labelled_tweet_file_semeval, 'r').readlines()

        print ("Length of input list is "+str(len(lines)))

        tweet_sentiment_list = []

        for line in lines:

            tweet_sentiment = []

            spline = line.replace('\n','').split('\t')

            # skip lines with error
            if (len(spline)) > 1:

                # in case there are tabs in the tweet as well, so need to join them into one tweet
                joined = ' '.join(spline[5:])

                new_list = [spline[4],joined]

                if new_list[0] == 'positive':

                    tweet_sentiment.append('pos')
                    tweet_sentiment.append(new_list[1])
                    tweet_sentiment_list.append(tweet_sentiment)

                elif new_list[0] == 'negative':

                    tweet_sentiment.append('neg')
                    tweet_sentiment.append(new_list[1])
                    tweet_sentiment_list.append(tweet_sentiment)

                else:
                    continue

            else:
                continue

        print ("Length of labelled tweet list is "+str(len(tweet_sentiment_list)))

        f = open(path_to_store_labelled_tweets_semeval,'w')

        for tsl in tweet_sentiment_list:
            f.write(','.join(tsl)+'\n')

        f.close()



################
# variables
################

path_to_labelled_tweet_file_sts_gold = '../../data_files/labelled_tweets/sts_gold_v03/sts_gold_tweet.csv'
path_to_store_raw_tweets_sts_gold = '../tweets/raw_tweets_sts_gold.txt'
path_to_store_labelled_tweets_sts_gold = '../tweets/labelled_tweets_sts_gold.txt'

path_to_labelled_tweet_file_SA = '../../data_files/labelled_tweets/SA/Sentiment_Analysis_Dataset_small.csv'
path_to_store_raw_tweets_SA = '../tweets/raw_tweets_SA.txt'
path_to_store_labelled_tweets_SA = '../tweets/labelled_tweets_SA.txt'

path_to_labelled_tweet_file_SS = '../../data_files/labelled_tweets/SentiStrength/twitter4242.txt'
path_to_store_raw_tweets_SS = '../tweets/raw_tweets_SS_noneutral.txt'
path_to_store_labelled_tweets_SS = '../tweets/labelled_tweets_SS_noneutral.txt'

path_to_labelled_tweet_file_stanford = '../../data_files/labelled_tweets/stanford_sts/testdata.csv'
path_to_store_raw_tweets_stanford = '../tweets/raw_tweets_stanford.txt'
path_to_store_labelled_tweets_stanford = '../tweets/labelled_tweets_stanford.txt'

path_to_labelled_tweet_file_stanford = '../../data_files/labelled_tweets/stanford_sts/testdata.csv'
path_to_store_raw_tweets_stanford_noneutral = '../tweets/raw_tweets_stanford_noneutral.txt'
path_to_store_labelled_tweets_stanford_noneutral = '../tweets/labelled_tweets_stanford_noneutral.txt'

path_to_labelled_tweet_file_semeval = '../../data_files/labelled_tweets/SemEval/tweeti-a.tsv'
path_to_store_raw_tweets_semeval = '../tweets/raw_tweets_semeval_4.txt'
path_to_store_labelled_tweets_semeval = '../tweets/labelled_tweets_semeval_4.txt'



if __name__ == '__main__':

    pt = ProcessLabelledTweets()

    #############
    # for sts_gold dataset
    #############

    #pt.create_raw_tweet_sts_gold()
    #pt.convert_labels_sts_gold()


    #############
    # for Sentiment Analysis Dataset (1.5 mil tweets)
    #############

    #pt.create_raw_tweet_SA()
    #pt.convert_labels_SA()


    #############
    # for SentiStrength dataset
    #############

    #pt.create_raw_tweet_SS()
    #pt.convert_labels_SS()

    #############
    # for Stanford dataset
    #############

    #pt.create_raw_tweet_stanford()
    #pt.convert_labels_stanford()

    #############
    # for SemEval dataset
    #############

    #pt.create_raw_tweets_semeval()
    pt.convert_labels_semeval()