import datetime
import hashlib
import json
import requests
# import urllib.request as urllib2
# import urllib.parse 

class jdApi:
    """
    京东接口必传系统参数：method、app_key、timestamp、format、v、sign_method、sign
    京东接口业务参数会封装在param_json中
    """
    # parameters = {} # 类变量，同类都通用，因尽量避免会变更的变量赋值造成相互覆盖
    def __init__(self,appkey,secret):
        # self.url = 'http://router.jd.com/api' # 旧版本
        self.url = 'https://api.jd.com/routerjson' # 新版本 https://union.jd.com/searchResultDetail?articleId=108188
        self.secret = secret # 是实例变量，不同实例不通用
        self.appkey = appkey
        self.format = 'json'
        self.v = '1.0'
        self.sign_method = 'md5'

    def __sign(self,parameters):
        # Step 1：key的排序
        keys = sorted(parameters.keys())
        # Step 2&3：key和值的拼接
        sign_str = self.secret
        for k in keys:
            if k == 'sign':
                continue
            s = k + parameters[str(k)]
            sign_str+= s
        sign_str += self.secret
        # Step 4：使用MD5进行加密 并转化成大写
        sign_hash = hashlib.md5() # 初始化
        sign_hash.update(sign_str.encode("utf8")) # 对字符串进行加密
        sign = sign_hash.hexdigest() # 拿到加密后的字符串
        return sign.upper() # 返回大写的sign
    
    def __sendRequestUrl(self,method,param_json):
        parameters={} # 方法内变量，可以对抗并发造成的脏变量（对抗实例变量相互的干扰）
        parameters['app_key'] = self.appkey
        parameters['format'] = self.format
        parameters['v'] = self.v
        parameters['sign_method'] = self.sign_method
        parameters['timestamp'] =  datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') #'2021-03-29 18:47:14' 
        parameters['method'] = method
        parameters['360buy_param_json'] = json.dumps(param_json, ensure_ascii=False,separators=(',', ':'))
        parameters['sign'] = self.__sign(parameters)
        # print(self.parameters)

        response = requests.post(self.url,data=parameters)
        return response

    # 订单行接口方法
    def get_jd_union_open_order_row_query(self,pageIndex,startTime,endTime,pageSize=500,_type=3):
        try:
            # 业务参数param_json格式
            # param_json={"orderReq":{"pageIndex":"1","pageSize":"10","startTime":"2021-03-31 00:0:00","endTime":"2021-03-31 00:00:10","type":"3"}}
            param_json = {'orderReq':{}}
            param_json['orderReq']['pageIndex'] = pageIndex
            param_json['orderReq']['pageSize'] = pageSize
            param_json['orderReq']['startTime'] = startTime
            param_json['orderReq']['endTime'] = endTime
            param_json['orderReq']['type'] = _type
            param_json['orderReq']['fields'] = 'goodsInfo,categoryInfo'
            
            data = self.__sendRequestUrl('jd.union.open.order.row.query',param_json).text
            return json.loads(data)
        
        except Exception as e:
            print("get_jd_union_open_order_row_query 报错了！","入参=",param_json,"返回值data=",data)
            # 会返回一个none类型的值
            #return response.text
            raise e

    # 关键词商品查询接口方法
    def jd_union_open_goods_query(self,skilist):
        """
        - 业务参数param_json格式
        - param_json={"goodsReqDTO":{"skuIds":["1857014","100018834988"]}}
        """
        
        try:
            param_json = {'goodsReqDTO':{}}
            param_json['goodsReqDTO']['skuIds'] = skilist

            data = self.__sendRequestUrl('jd.union.open.goods.query',param_json).text

            return json.loads(data)
        except Exception as e:
            print("jd_union_open_goods_query 报错了！","入参=",param_json,"返回值data=",data)
            raise e


    # 优惠券领取查询接口方法
    def jd_union_open_coupon_query(self,coupon):
        """
        - 业务参数param_json格式
        - coupon = ["http://coupon.m.jd.com/coupons/show.action?linkKey=AAROH_xIpeffAs_-naABEFoeegMSphNTmCsgOeraLJTVIVTZGigswFY62GWdJiqMP2VurXlSObuY9eiOWLMiMnbqkVUmoQ"]
        """
        
        try:
            param_json = {'couponUrls':coupon}
            data = self.__sendRequestUrl('jd.union.open.coupon.query',param_json).text
            return json.loads(data)
        except Exception as e:
            print("jd_union_open_goods_query 报错了！","入参=",param_json,"返回值data=",data)
            raise e

    # 工具商转链接口
    def jd_union_open_promotion_byunionid_get(self,materialId,unionId,positionId=None,pid=None,couponUrl='',giftCouponKey='',subUnionId='',channelId=None,chainType=2):
        """
        - 业务参数param_json格式
        - 
        """
        
        try:
            param_json = {'promotionCodeReq':{}}
            param_json['promotionCodeReq']['materialId'] = materialId
            param_json['promotionCodeReq']['unionId'] = unionId
            param_json['promotionCodeReq']['positionId'] = positionId
            param_json['promotionCodeReq']['pid'] = pid
            param_json['promotionCodeReq']['couponUrl'] = couponUrl
            param_json['promotionCodeReq']['giftCouponKey'] = giftCouponKey
            param_json['promotionCodeReq']['subUnionId'] = subUnionId
            param_json['promotionCodeReq']['channelId'] = channelId
            param_json['promotionCodeReq']['chainType'] = chainType

            data = self.__sendRequestUrl('jd.union.open.promotion.byunionid.get',param_json).text
            return json.loads(data)
        except Exception as e:
            print("jd_union_open_goods_query 报错了！","入参=",param_json,"返回值data=",data)
            raise e








