"""
在贴吧里看到了大神通过对cet的app抓包得到了考号，大神的方法用的js，我将方法转换成了python程序
有问题请联系：992871471
"""
import requests
import json
from requests import ConnectionError
from pyquery import PyQuery as pq
url1 = 'http://app.cet.edu.cn:7066/baas/app/setuser.do?method=UserVerify'
url2 = 'http://www.chsi.com.cn/cet/query?zkzh={id}&xm={name}'
info = {
 "ks_xm": "姓名",
 "ks_sfz": "身份证号",
 "jb": "1",
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Referer':'http://www.chsi.com.cn/cet/',
}

info['ks_xm'] = input('请输入姓名:')
info['ks_sfz'] = input('请输入身份证号:')
info['jb'] = input('四级请输入1，六级请输入2:')

data=json.dumps(info)
postdata = {
 "action": "",
 "params": data,
}
try:
    response = requests.post(url1, data=postdata)
    if response.status_code == 200:
        content = json.loads(response.text)
        kh = content['ks_bh']
        url3 =url2.format(id=kh,name=info['ks_xm'])
        response = requests.get(url3,headers=headers)
        doc = pq(response.text)
        items = doc.items('.m_cnt_m tr')
        for i in items:
            print(i.text())
except Exception as e:
    print(e.args)
