__author__ = 'yi-linghwong'

import sys
import os

class SentiStrength():

    def run_sentistrength(self):

        os.system("java -jar /Users/yi-linghwong/GitHub/data_files/SentiStrength/SentiStrengthCom.jar "
                  "sentidata /Users/yi-linghwong/GitHub/data_files/SentiStrength/SentStrength_Data_December2015English/ "
                  "input "+path_to_tweet_file+" outputFolder "+path_to_output_folder+" "+option)

    def label_tweets_binary(self):

        lines = open(path_to_tweet_score_file,'r').readlines()

        # ignore first line as it is the line with headings
        lines = lines[1:]
        print ("Length of tweet list is "+str(len(lines)))

        tweet_pol_list = []

        for line in lines:

            tweet_pol = []

            spline = line.replace('\n','').split('\t')

            # in case there are tabs in the tweet as well, so need to join them into one tweet
            joined = ' '.join(spline[1:])

            new_list = [spline[0],joined]

            if new_list[0] == '1':
                tweet_pol.append('pos')

            elif new_list[0] == '-1':
                tweet_pol.append('neg')

            # sometimes tweets will be labelled as '0' and the tweet text disappears in output file
            # in this case categorise as 'neg'

            else:
                print ("error")
                tweet_pol.append('neg')

            tweet_pol.append(new_list[1])
            tweet_pol_list.append(tweet_pol)

        print ("Length of labelled tweets is "+str(len(tweet_pol_list)))

        f = open(path_to_store_labelled_tweets,'w')

        for tpl in tweet_pol_list:
            f.write(','.join(tpl)+'\n')

        f.close()


    def label_tweets_trinary(self):

        lines = open(path_to_tweet_score_file,'r').readlines()

        # ignore first line as it is the line with headings
        lines = lines[1:]
        print ("Length of tweet list is "+str(len(lines)))

        tweet_pol_list = []

        for line in lines:

            tweet_pol = []

            spline = line.replace('\n','').split('\t')

            # in case there are tabs in the tweet as well, so need to join them into one tweet
            joined = ' '.join(spline[1:])

            new_list = [spline[0],joined]

            if new_list[0] == '1':
                tweet_pol.append('pos')

            elif new_list[0] == '-1':
                tweet_pol.append('neg')

            elif new_list[0] == '0':
                tweet_pol.append('neg')

            else:
                print ("error")

            tweet_pol.append(new_list[1])
            tweet_pol_list.append(tweet_pol)

        print ("Length of labelled tweets is "+str(len(tweet_pol_list)))

        f = open(path_to_store_labelled_tweets,'w')

        for tpl in tweet_pol_list:
            f.write(','.join(tpl)+'\n')

        f.close()





if __name__ == "__main__":

    path_to_tweet_file = '../tweets/preprocessed_tweets_sts_gold.txt'
    path_to_output_folder = 'results/'
    option = 'binary'  #trinary (report positive-negative-neutral classifcation instead)
                        #binary (report positive-negative classifcation instead)
                        #scale (report single -4 to +4 classifcation instead)

    path_to_tweet_score_file = 'results/preprocessed_tweets_sts_gold0_out.txt'
    path_to_store_labelled_tweets = 'results/sts_gold_tweets_senti_polarity.txt'


    ss = SentiStrength()

    #ss.run_sentistrength()
    ss.label_tweets_binary()
    #ss.label_tweets_trinary()

