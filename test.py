import os
import sys
from thread_pool import ThreadPool

def myTest(s1, s2):
    print s1,s2

tp = ThreadPool(3)
for i in xrange(3):
    tp.add_job(myTest, str(i), str(i+10))
tp.begin_to_finish()
