# huamulantool
# Where to get it
pip install huamulantool

# 需要一下依赖
import datetime
import hashlib
import json
import requests


# 打工人api使用方法
from huamulantool.dgrapi import dgrapi

a = dgrapi('appkey','appsecret')
d = a.get_qcSmartChain('https://item.jd.com/10038553891397.html',1000546666)

