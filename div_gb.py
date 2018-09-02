#coding:utf-8
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

from snownlp import SnowNLP

def get_goodlist(nlist, threshold = 0.4):
    num = nlist.__len__()
    goodlist = []
    for i in xrange(1, num):
        #  情感评分
        score = SnowNLP(unicode((str(nlist[i])))).sentiments
        #  分离好评和差评
        if score > threshold:
            goodlist.append(nlist[i])
    return goodlist

def get_badlist(nlist, threshold = 0.4):
    num = nlist.__len__()
    badlist = []
    for i in xrange(1, num):
        #  情感评分
        score = SnowNLP(unicode((str(nlist[i])))).sentiments
        #  分离好评和差评
        if score < threshold:
            badlist.append(nlist[i])
    return badlist