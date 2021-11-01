import time
import hashlib
import json
import requests

class dgrapi:
    def __init__(self,appkey,appsecret):
        """
        appkey:你的打工的key
        appsecret:你的打工人的secret
        """
        self.url = 'https://www.dgrlm.com'
        self.appkey = appkey
        self.appsecret = appsecret

    def __getsign(self,signParam):
        # 拼接预签名参数（signParam）
        sign = ''
        signParamkeys = sorted(signParam.keys())
        for k in signParamkeys:
            k += str(signParam[k])
            sign += k
        sign = self.appsecret + sign + self.appsecret

        # 拼接最终加密参数（signStr）
        sign_hash = hashlib.md5()
        sign_hash.update(sign.encode("utf8")) 
        signStr = sign_hash.hexdigest().upper()

        return signStr


    def __sendRequestUrl(self,url,param_json):
        headers = {'Content-Type' : 'application/json'}
        parameters={} # 方法内变量，可以对抗并发造成的脏变量（对抗实例变量相互的干扰）
        parameters['appKey'] = self.appkey
        parameters['timestamp'] = str(round(time.time() * 1000))
        parameters.update(param_json)
        # 去除空值参
        for k in list(parameters.keys()):
            if  parameters [k] is None or len(str(parameters [k])) == 0:
                del parameters [k]
        parameters['sign'] = self.__getsign(parameters)

        response = requests.post(self.url+url,headers=headers,data=json.dumps(parameters))
        return response


    # 智能转链
    def get_qcSmartChain(self,copywriting,unionId,positionId=None):
        """
        智能转链
        文档：https://www.dgrlm.com/open/doc?category=%E4%BE%BF%E6%8D%B7%E5%B7%A5%E5%85%B7&api=https://www.dgrlm.com/qcypopen/open/v1/qcSmartChain
        """
        try:
            param_json = {}
            param_json['copywriting'] = copywriting
            param_json['unionId'] = unionId
            param_json['positionId'] = positionId
            
            data = self.__sendRequestUrl('/qcypopen/open/v1/qcSmartChain',param_json).text
            return json.loads(data)
        
        except Exception as e:
            print("智能转链 报错了！","入参=",param_json,"返回值data=",data)
            raise e






    

