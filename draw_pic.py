#coding=utf-8
#  处理中文
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from snownlp import SnowNLP
import numpy as np
import matplotlib.pyplot as plt

def draw_pic(collection1, collection2, pointn = 400):
    #  搜索全部评论
    comment_list = []
    for item in collection1.find():
        comment_id = item["content"]
        comment_list.append(comment_id)

    #  全部星级评论
    score_list = []
    for item in collection1.find():
        score_id = item["score"]
        score_list.append(score_id)

    num = comment_list.__len__()
    x = np.arange(1, pointn)
    s1 = []
    s2 = []
    for i in x:
        #  情感评分
        s1.append(SnowNLP(unicode(str(comment_list[i]))).sentiments)
        #  星级评分
        s2.append(score_list[i])

    plt.figure(1)
    plt.grid(True)
    plt.axis([0.8, 5.2, -0.1, 1.1])
    plt.plot(s2, s1, 'x')
    plt.show()
