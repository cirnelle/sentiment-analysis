__author__ = 'yi-linghwong'

list1 = ['1','0','1','0','1','0']

list2 = ['1','1','0','0','1','0']


not_equal = [(i,j) for i,j in zip(list1,list2) if i!=j]

print (not_equal)