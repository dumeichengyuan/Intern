#coding=utf-8
#  处理中文
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_brand(collection1, collection2, comment):
    #  搜索商品id
    for item1 in collection1.find({"content":comment}):
        product_id = item1["product_id"]
        for item2 in collection2.find({"product_id": str(product_id)}):
            brand_id = item2["brand_name"]
            return brand_id