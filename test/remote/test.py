# import huamulantool
# from 包名称.模块名称(文件名) import 类名
from huamulantool.dgrapi import dgrapi

a = dgrapi('111','222')
d = a.get_qcSmartChain('https://item.jd.com/10038553891397.html',1000546820)
print(d)