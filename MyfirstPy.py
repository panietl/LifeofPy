#!/usr/bin/python
import csv
count = len(open('C:\phy_test\FlashInfo_FR_WW.csv', "r").readlines(  ))
a=10
from itertools import islice
from operator import itemgetter
get_columns = itemgetter('CRPCD','YEAR')
f = open('C:\phy_test\FlashInfo_FR_WW.csv', "r")
for x in f:print(x)
#if x >10:break
print(count)
if f.readlines() == a:breakpoint()

#f.write("Sarang inserted a record")
#print (reader)       <-- fail


#if(i >=5):break