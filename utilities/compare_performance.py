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

        performance = ((len(gold_standard)-len(not_equal)) / len(gold_standard)) *100

        print ("Overall accuracy is "+str(performance)+"%")


        print(metrics.classification_report(gold_standard,to_compare))
        cm = metrics.confusion_matrix(gold_standard,to_compare)
        print(cm)


if __name__ == '__main__':

    #path_to_gold_standard = '../tweets/labelled_tweets_sts_gold.txt'
    path_to_gold_standard = '../../data_files/labelled_tweets/SA_1.5milliontweets/labelled_tweets_SA.txt'
    path_to_file_to_compare = '../_SentiStrength/results/SA_tweets_senti_polarity.txt'


    cp = ComparePerformance()
    cp.calculate_performance()

