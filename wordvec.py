#coding=utf-8
#  处理中文

import gensim
# 导入模型
#  model = word2vec.Word2Vec.load("/Users/stille/Desktop/intern/baidubaike.model")
model = gensim.models.KeyedVectors.load_word2vec_format("./baidubaike.bin", binary=True)

result1 = model.most_similar(u'物流')
for each in result1:
    print each[0] , each[1]

result2 = model.most_similar(u'运输')
for each in result2:
    print each[0] , each[1]

result3 = model.similarity(u'瓶子', u'包装')
print result3

result4 = model.most_similar(u'醇正')
for each in result4:
    print each[0] , each[1]

result5 = model.most_similar(u'骑士乳业')
for each in result5:
    print each[0] , each[1]



