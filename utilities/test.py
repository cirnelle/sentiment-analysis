__author__ = 'yi-linghwong'

import os
import sys


sys.path.append('/Users/yi-linghwong/GitHub/sentiment-analysis/utilities/')
from compare_performance import ComparePerformance

sys.path.append('/Users/yi-linghwong/GitHub/sentiment-analysis/_BLiu/')
from bliu import BLiu


class Test():

    def test(self):
        cp = ComparePerformance()
        cp.calculate_performance()

    def bliu(self):
        os.chdir('/Users/yi-linghwong/GitHub/sentiment-analysis/_BLiu/')
        bl = BLiu()
        bl.combine_dicts()


t = Test()
t.test()
t.bliu()