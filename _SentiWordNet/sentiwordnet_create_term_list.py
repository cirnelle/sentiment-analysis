#!/usr/bin/python

__author__ = 'yi-linghwong'


import os
import sys
import re
import numpy as np



class SentiWordNetList():

    def create_term_list(self):

    ###########
    # create a separate list for each synonymous term which are separated by white space
    ###########


        tl1 = []
        tl2 = []
        tl3 = []
        term_list = []

        lines = open(path_to_term_file, 'r').readlines()

        for line in lines:
            spline = line.replace('\n', '').split('\t')
            tl1.append(spline)

        ###########
        # create a separate list for each synonymous term which are separated by white space
        ###########

        for tl in tl1:

            split_white_space = tl[2].split()
            split_white_space.append(tl[1])
            split_white_space.append(tl[0])
            split_white_space.reverse()
            tl2.append(split_white_space)



        for tl in tl2:

            for i in range(2,len(tl)):

                tl3 = []

                tl3.append(tl[i])
                tl3.append(tl[0])
                tl3.append(tl[1])

                term_list.append(tl3)

        print ("Length of term list is "+str(len(term_list)))

        return (term_list)



    def top_sense_list(self):

    ##############
    # retain only words with sense number 1
    ##############

        term_list = self.create_term_list()


        only_top_sense = []

        for tl in term_list:
            if '#1' in tl[0]:

                # remove the terms with sense number #10, #11, #12, ...
                if not (re.search('[#]+[0-9]+[0-9]', tl[0])):

                    # remove hash followed by 1 from terms
                    tl[0] = re.sub('[#]+[0-9]+','', tl[0])
                    # replace underscore with white space
                    tl[0] = tl[0].replace('_', ' ')
                    only_top_sense.append(tl)

        only_top_sense.sort(key=lambda x: x[0])

        print ("Length of top sense list is "+str(len(only_top_sense)))


        f = open('dictionary/SentiWordNet_top.txt', 'w')

        for ots in only_top_sense:
            f.write(', '.join(ots)+'\n')

        f.close()

        return (only_top_sense)




    def without_neutral(self):

    #############
    # remove words with neutral sentiment (pos and neg both 0)
    #############

        list_to_neutralise = self.top_sense_list()

        without_neutral = []

        for ltn in list_to_neutralise:
            if not (ltn[1] == '0' and ltn[2] == '0'):
                without_neutral.append(ltn)



        without_neutral.sort(key=lambda x: x[0])


        print ("Length of without neutral list is "+str(len(without_neutral)))



        f = open('dictionary/without_neutral.txt', 'w')

        for wn in without_neutral:
            f.write(', '.join(wn)+'\n')

        f.close()


        return without_neutral

    def average_sentiments(self):

        term_list = self.top_sense_list()


        #############
        # Create a list containing the duplicated terms, each appearing only once (e.g. ['able', 'unable', ...])
        #############

        tl1 = []
        dup_terms = []

        print ("Creating list of duplicated terms ...")

        for tl in term_list:

            if tl[0] not in tl1:

                tl1.append(tl[0])

            else:

                dup_terms.append(tl[0])

            dup_terms = set(dup_terms)
            dup_terms = list(dup_terms)

        print ("There are "+str(len(dup_terms))+" duplicated terms.")

        #############
        # Create a list containing the average sentiment score of duplicated terms (e.g. [['able', '0.33', '0'],['unable, '0', '0.87']]
        #############

        avg_term_list = []

        print ("Calculating average ...")

        for t in dup_terms:

            dup_list = []
            avg_list = []

            for tl in term_list:
                if tl[0] == t:
                    dup_list.append(tl)

            # get average of positive score and negative score

            pos_avg = np.mean([float(x[1]) for x in dup_list])
            neg_avg = np.mean([float(x[2]) for x in dup_list])

            avg_list.append(t)
            avg_list.append(str(pos_avg))
            avg_list.append(str(neg_avg))

            avg_term_list.append(avg_list)


        ############
        # Create a list without the duplicate terms
        ############

        # IMPORTANT! cannot do without_dup_list = term_list because both will change every time either one is changed!

        without_dup_list = list(term_list)

        print ("Creating no dup list ...")

        for t in dup_terms:

            for tl in term_list:

                if tl[0] == t:
                    without_dup_list.remove(tl)


        final_list = []
        final_list.extend(avg_term_list)
        final_list.extend(without_dup_list)

        final_list.sort(key=lambda x: x[0])

        print ("Length of average sentiment list is "+str(len(final_list)))

        f = open('dictionary/average_sentiment.txt', 'w')

        for wn in final_list:
            f.write(', '.join(wn)+'\n')

        f.close()

    def average_no_neutral(self):

        avg_sentiment_list = []

        lines = open('dictionary/average_sentiment.txt', 'r').readlines()

        for line in lines:
            # also remove underscore in between ngram words!
            spline = line.replace('\n', '').split(', ')
            avg_sentiment_list.append(spline)

        print ("Length of average sentiment list is "+str(len(avg_sentiment_list)))

        without_neutral = []

        for asl in avg_sentiment_list:
            if not ((asl[1] == '0' and asl[2] == '0') or (asl[1] == '0.0' and asl[2] == '0.0')):

                # replace underscore in between words with blank
                asl[0] = asl[0].replace('_', ' ')

                without_neutral.append(asl)

        without_neutral.sort(key=lambda x: x[0])


        print ("Length of average no neutral list is "+str(len(without_neutral)))


        f = open('dictionary/avg_no_neutral.txt', 'w')

        for wn in without_neutral:
            f.write(', '.join(wn)+'\n')

        f.close()


        return without_neutral




if __name__ == "__main__":

    swn = SentiWordNetList()

    #####################
    # Run code from IDE #
    #####################

    path_to_term_file = 'dictionary/SentiWordNet_INPUT.txt'

    ############
    # Create list with top sense
    ############

    #swn.top_sense_list()

    ###########
    # Create top sense list without neutral terms
    ###########

    # Use EITHER without_neutral OR average_sentiments, not both!

    swn.without_neutral()

    ##########
    # Create list with average sentiments (from top sense list)
    ##########

    #swn.average_sentiments()

    ##########
    # Create average sentiment list without neutral terms
    ##########

    #swn.average_no_neutral()


    ################################
    # Run script from command line #
    ################################

    '''

    path_to_term_file = sys.argv[1]


    if (sys.argv[2]=='top_sense_list'):
        swn.top_sense_list()

    elif (sys.argv[2]=='without_neutral'):
        swn.without_neutral()

    elif (sys.argv[2]=='average_sentiments'):
        swn.average_sentiments()
    elif (sys.argv[2]=='average_no_neutral'):
        swn.average_no_neutral()

    else:
        print ("Invalid argument")

    '''














