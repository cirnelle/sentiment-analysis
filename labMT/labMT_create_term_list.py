__author__ = 'yi-linghwong'

import os
import sys
import time


class labMTSentimentAnalysis():

    def create_term_list(self):

        lines = open('test.txt', 'r').readlines()

        term_list = []

        for line in lines:

            list = []

            spline = line.replace('\n','').split('\t')
            list.append(spline[0])
            list.append(spline[2])

            term_list.append(list)

        print (term_list)


if __name__ == "__main__":

    lmt = labMTSentimentAnalysis()
    lmt.create_term_list()