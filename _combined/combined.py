

__author__ = 'yi-linghwong'

####################
# Get sentiment of tweets using piping
# first BLiu, then SentiStrength
####################

import os
import sys
from sklearn import metrics


#sys.path.append('/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/')
#from compare_performance import ComparePerformance

#cp = ComparePerformance()
#os.chdir('/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/')


class Combined():

    def __init__(self):
        print ("Running piping script ...")

    def run_bliu(self):

        os.chdir('/Users/yi-linghwong/GitHub/sentiment-analysis/_BLiu/')
        os.system("/Users/yi-linghwong/GitHub/sentiment-analysis/_BLiu/bliu.py"+" "
                  +bliu_path_to_processed_tweet_file+" "
                  +bliu_path_to_store_results_score+" "
                  +bliu_path_to_store_results_polarity)

    def extract_neutral(self):

        os.chdir('/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/')
        os.system("/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/extract_neutral_sentiment.py"+" "
                  +path_to_sentiment_result_file+" "
                  +path_to_store_only_neutral_file_lexicon+" "
                  +path_to_store_noneutral_file_lexicon+" "
                  +path_to_unprocessed_labelled_tweets+" "
                  +path_to_preprocessed_tweets+" "
                  +path_to_store_labelled_noneutral_list+" "
                  +path_to_store_labelled_neutral_list)

    def compare_performance_bliu(self):

        os.chdir('/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/')
        os.system("/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/compare_performance.py"+" "
                  +bliu_path_to_gold_standard+" "
                  +bliu_path_to_file_to_compare)

        lines = open('../_combined/results/neutral/gold_standard.txt','r').readlines()

        gold_standard = []

        for line in lines:
            spline = line.replace('\n','')
            gold_standard.append(spline)

        print ("Length of gold standard for bliu is "+str(len(gold_standard)))

        lines = open('../_combined/results/neutral/to_compare.txt','r').readlines()

        to_compare = []

        for line in lines:
            spline = line.replace('\n','')
            to_compare.append(spline)

        print ("Length of to compare for bliu is "+str(len(to_compare)))

        return gold_standard, to_compare

    def run_sentistrength(self):

        os.chdir('/Users/yi-linghwong/GitHub/sentiment-analysis/_SentiStrength/')
        os.system("/Users/yi-linghwong/GitHub/sentiment-analysis/_SentiStrength/sentistrength.py"+" "
                  +ss_path_to_tweet_file+" "
                  +ss_path_to_output_folder+" "
                  +ss_option+" "
                  +ss_path_to_tweet_score_file+" "
                  +ss_path_to_store_labelled_tweets+" ")

    def compare_performance_ss(self):

        os.chdir('/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/')
        os.system("/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/compare_performance.py"+" "
                  +ss_path_to_gold_standard+" "
                  +ss_path_to_file_to_compare)

        lines = open('../_combined/results/neutral/gold_standard.txt','r').readlines()

        gold_standard = []

        for line in lines:
            spline = line.replace('\n','')
            gold_standard.append(spline)

        print ("Length of gold standard for sentistrength is "+str(len(gold_standard)))

        lines = open('../_combined/results/neutral/to_compare.txt','r').readlines()

        to_compare = []

        for line in lines:
            spline = line.replace('\n','')
            to_compare.append(spline)

        print ("Length of to compare for sentistrength is "+str(len(to_compare)))

        return gold_standard, to_compare

    def get_overall_performance(self):

        self.run_bliu()
        self.extract_neutral()

        gold_standard_bliu = self.compare_performance_bliu()[0]
        to_compare_bliu = self.compare_performance_bliu()[1]

        self.run_sentistrength()

        gold_standard_ss = self.compare_performance_ss()[0]
        to_compare_ss = self.compare_performance_ss()[1]

        gold_standard_all = gold_standard_bliu + gold_standard_ss
        to_compare_all = to_compare_bliu + to_compare_ss

        print ("Length of complete gold standard list is "+str(len(gold_standard_all)))
        print ("Length of complete to compare list is "+str(len(to_compare_all)))

        not_equal = [(i,j) for i,j in zip(gold_standard_all,to_compare_all) if i!=j]

        performance = round((((len(gold_standard_all)-len(not_equal)) / len(gold_standard_all)) *100),2)

        print ("Overall accuracy is "+str(performance)+"%")


        print(metrics.classification_report(gold_standard_all,to_compare_all))
        cm = metrics.confusion_matrix(gold_standard_all,to_compare_all)
        print (cm)

###############
# variables
###############


# bliu.py
bliu_path_to_processed_tweet_file = '../tweets/preprocessed_tweets_sts_gold.txt'
bliu_path_to_store_results_score = 'results/sts_gold_tweets_senti_score.txt'
bliu_path_to_store_results_polarity = 'results/sts_gold_tweets_senti_polarity.txt'

# extract_neutral_sentiment.py
path_to_sentiment_result_file = '../_BLiu/results/sts_gold_tweets_senti_polarity.txt'
path_to_store_only_neutral_file_lexicon = '../_BLiu/results/neutral/sts_gold_neutral.txt'
path_to_store_noneutral_file_lexicon = '../_BLiu/results/neutral/sts_gold_noneutral.txt'

path_to_unprocessed_labelled_tweets = '../tweets/labelled_tweets_sts_gold.txt'
path_to_preprocessed_tweets = '../tweets/preprocessed_tweets_sts_gold.txt'

path_to_store_labelled_noneutral_list = '../tweets/neutral/bliu_labelled_noneutral_sts_gold.txt'
path_to_store_labelled_neutral_list = '../tweets/neutral/bliu_labelled_neutral_sts_gold.txt'

# compare_performance.py - 1
bliu_path_to_gold_standard = '../tweets/neutral/bliu_labelled_noneutral_sts_gold.txt'
bliu_path_to_file_to_compare = '../_BLiu/results/neutral/sts_gold_noneutral.txt'

# sentistrength.py
ss_path_to_tweet_file = '../_BLiu/results/neutral/sts_gold_neutral.txt'
ss_path_to_output_folder = 'results/neutral/'
ss_option = 'trinary'
ss_path_to_tweet_score_file = 'results/neutral/sts_gold_neutral0_out.txt'
ss_path_to_store_labelled_tweets = 'results/neutral/sts_gold_neutral_senti_polarity.txt'

# compare_performance.py - 2
ss_path_to_gold_standard = '../tweets/neutral/bliu_labelled_neutral_sts_gold.txt'
ss_path_to_file_to_compare = '../_SentiStrength/results/neutral/sts_gold_neutral_senti_polarity.txt'


if __name__ == '__main__':

    cb = Combined()
    #cb.run_bliu()
    #cb.extract_neutral()
    #cb.compare_performance_bliu()
    #cb.run_sentistrength()
    #cb.compare_performance_ss()
    cb.get_overall_performance()

