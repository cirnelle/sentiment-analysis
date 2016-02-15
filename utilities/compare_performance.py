#!/usr/local/bin/python3

__author__ = 'yi-linghwong'

import sys
import os
from sklearn import metrics

class ComparePerformance():

    def calculate_performance(self):

    ############
    # Calculate overall accuracy, percision, recall and f1-score
    ############

        lines = open(path_to_gold_standard,'r').readlines()

        gold_standard = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            gold_standard.append(spline[0])

        print ("Length of gold standard is "+str(len(gold_standard)))

        lines = open(path_to_file_to_compare,'r').readlines()

        to_compare = []

        for line in lines:
            spline = line.replace('\n','').split(',')
            to_compare.append(spline[0])

        print ("Length of target list is "+str(len(to_compare)))

        not_equal = [(i,j) for i,j in zip(gold_standard,to_compare) if i!=j]

        print (len(not_equal))

        performance = round((((len(gold_standard)-len(not_equal)) / len(gold_standard)) *100),2)

        print ("Overall accuracy is "+str(performance)+"%")


        print(metrics.classification_report(gold_standard,to_compare))
        cm = metrics.confusion_matrix(gold_standard,to_compare)
        print (cm)

        # write gold standard to file

        f = open(path_to_store_gold_standard,'w')

        for gs in gold_standard:
            f.write(gs+'\n')

        f.close()

        # write to compare list to file

        f = open(path_to_store_to_compare,'w')

        for tc in to_compare:
            f.write(tc+'\n')

        f.close()

        return

##############
# variables
##############

path_to_store_gold_standard = '../_combined/results/neutral/gold_standard.txt'
path_to_store_to_compare = '../_combined/results/neutral/to_compare.txt'

# command line
path_to_gold_standard = sys.argv[1]
# 2 stage
#path_to_gold_standard = '../tweets/neutral/bliu_labelled_noneutral_sts_gold.txt'
#path_to_gold_standard = '../tweets/neutral/bliu_labelled_neutral_sts_gold.txt'
# 3 stage
#path_to_gold_standard = '../tweets/neutral/emoticon_labelled_noneutral_SA.txt'
#path_to_gold_standard = '../tweets/neutral/bliu_labelled_noneutral_SA.txt'
#path_to_gold_standard = '../tweets/neutral/bliu_labelled_neutral_SA.txt'
# big file
#path_to_gold_standard = '../../data_files/labelled_tweets/SA_1.5milliontweets/labelled_tweets_SA.txt'

# command line
path_to_file_to_compare = sys.argv[2]
# 2 stage
#path_to_file_to_compare = '../_BLiu/results/neutral/sts_gold_noneutral.txt'
#path_to_file_to_compare = '../_SentiStrength/results/neutral/sts_gold_neutral_senti_polarity.txt'
# 3 stage
#path_to_file_to_compare = '../_emoticon/results/neutral/SA_noneutral.txt'
#path_to_file_to_compare = '../_BLiu/results/neutral/SA_noneutral.txt'
#path_to_file_to_compare = '../_SentiStrength/results/neutral/SA_neutral_senti_polarity.txt'
# big file
#path_to_file_to_compare = '../_SentiStrength/results/neutral/sts_gold_neutral_senti_polarity.txt'


if __name__ == '__main__':

    cp = ComparePerformance()
    cp.calculate_performance()




