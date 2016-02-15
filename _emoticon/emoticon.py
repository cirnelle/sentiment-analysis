__author__ = 'yi-linghwong'

###############
# calculate sentiment of tweets using emoticon dictionary
###############

import sys
import os
import time

class Emoticon():

    def sync_emo_dict_emo_score(self):

    #############
    # check if all emoticons in emo dict is also in emo score
    #############

        lines = open(path_to_emoticon_dict,'r').readlines()

        emo_dict = []
        emoticon_dict = []

        for line in lines:
            spline = line.replace('\n','').split('\t')
            emo_dict.append(spline[0])
            emoticon_dict.append(spline)

        #print ("Length of emoticon dict list is "+str(len(emo_dict)))

        lines = open(path_to_emoticon_score,'r').readlines()

        emo_score = []

        for line in lines:
            spline = line.replace('\n','').split('\t')
            emo_score.append(spline[0])

        #print ("Length of emoticon score list "+str(len(emo_score)))

        extra_emoticon = []

        for ed in emo_dict:
            if ed not in emo_score:
                extra_emoticon.append(ed)

        if len(emo_dict) != len(emo_score):
            print ("Length of emo dict and emo score unequal")
            print ("Extra emoticons are "+str(extra_emoticon))
            sys.exit()


    def create_emoticon_dict(self):

        lines = open(path_to_emoticon_score,'r').readlines()

        emo_dict = {}

        print ("Creating emoticon dict ...")

        for line in lines:
            spline = line.replace('\n','').split('\t')

            # add space to front and end of emoticon so whole emoticons can be detected
            spline[0] = ' '+spline[0]+' '

            emo_dict[spline[0]] = spline[1]

        print ("Length of emoticon dict is "+str(len(emo_dict)))

        return emo_dict

    def create_tweet_list(self):

        # create a list of tweets, e.g. ['This is the first tweet', 'This is another tweet', ...]
        # splitlines method to remove '\n' from end of line
        lines = open(path_to_raw_tweets).read().splitlines()

        tweets = []

        for l in lines:

            # if tweet starts and ends with double quotes, remove them

            if l.startswith('"') and l.endswith('"'):
                l = l[1:-1]
            tweets.append(l)

        # add blank space to front and end of line for each tweet, in case the ngram is the first or last word in the sentence
        # e.g. ngram = ' the end ', and the tweet is 'that is the end', if we don't add space the ngram won't be detected

        tweets=[' '+t+' ' for t in tweets]

        return tweets

    def create_emoticon_list(self):

        ################
        # create a list of the emoticons from emoticon dictionary (only the emoticons, without their score)
        ################

        emoticon_list = []

        lines = open(path_to_emoticon_score, 'r').readlines()

        print ("Creating emoticon list ...")

        for line in lines:
            spline = line.replace('\n', '').split('\t')
            emoticon_list.append(spline[0])


        return emoticon_list

    def calculate_senti_score(self):

        self.sync_emo_dict_emo_score()
        emo_dict = self.create_emoticon_dict()
        emo_list = self.create_emoticon_list()
        tweet_list = self.create_tweet_list()

        print ("Length of tweet list is "+str(len(tweet_list)))

        # add white space to front and end of emoticons so whole emoticons can be matched

        emo_list = [' '+el+' ' for el in emo_list]

        print ("Length of emoticon list is "+str(len(emo_list)))

        tweet_score_list = []
        tweet_score_list_polarity = []

        print("Calculating sentiment score ...")

        t1 = time.time()

        for tl in tweet_list:

            tweet_score = []
            tweet_score_c = []

            string = tl

            senti_score = 0

            for el in emo_list:

                substring = el

                if substring in string:

                    senti_score += int(emo_dict[substring])

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

        total_time = (t2 - t1) / 60

        print("Computing time was " + str(total_time) + " minutes.")

        f = open(path_to_store_results_score, 'w')

        for tsl in tweet_score_list:
            f.write(','.join(tsl) + '\n')

        f.close()

        ##################
        # Preprocess tweets before writing them to file
        ##################

        print ("................ zipping preprocess and polarity...................")

        polarity = []

        for tslp in tweet_score_list_polarity:
            polarity.append(tslp[0])

        print ("Length of polarity list is "+str(len(polarity)))

        lines = open(path_to_preprocessed_tweets,'r').readlines()

        preprocessed = []

        for line in lines:
            spline = line.replace('\n','')
            spline = ' '+spline+' '
            preprocessed.append(spline)

        print ("Length of preprocessed tweets is "+str(len(preprocessed)))

        combined = zip(polarity,preprocessed)

        labelled_preprocessed = []

        for c in combined:
            c = list(c)
            labelled_preprocessed.append(c)


        print ("Length of labelled preprocessed tweet is "+str(len(labelled_preprocessed)))


        f = open(path_to_store_results_polarity, 'w')

        for lp in labelled_preprocessed:
            f.write(','.join(lp) + '\n')

        f.close()

        return tweet_score_list

if __name__ == '__main__':

    path_to_emoticon_dict = '../emoticons/emo_dict.txt'
    path_to_emoticon_score = '../emoticons/emoticon_score.txt'

    path_to_raw_tweets = '../tweets/raw_tweets_SA.txt' #use raw tweets!
    path_to_preprocessed_tweets = '../tweets/preprocessed_tweets_SA.txt'
    path_to_store_results_score = 'results/SA_tweets_senti_score.txt'
    path_to_store_results_polarity = 'results/SA_tweets_senti_polarity.txt'


    em = Emoticon()
    #em.sync_emo_dict_emo_score()
    #em.create_emoticon_dict()
    em.create_tweet_list()
    em.create_emoticon_list()
    em.calculate_senti_score()