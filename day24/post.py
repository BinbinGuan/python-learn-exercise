import requests
import json
#用两个星号表示关键字参数
""""
def f1(a, b, c=0, *args, **kw):
    print("a = ", a, "b = ", b, "args = ", args, "kw = ",kw)
def f2(a, b, c=0, *, d, **kw):
    print("a = ", a, "b = ", b, "c = ", c, "d = ", d, "kw = ", kw)

>>> f1(1, 2)
a = 1 b = 2 c = 0 args =() kw = {}
>>> f1(1, 2, c=3)
a = 1 b = 2 c = 3 args = () kw = {}
>>> f1(1, 2, 3, 'a', 'b')
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
>>> f1(1, 2, 3, 'a', 'b', x = 99)
a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x':99}
>>> f2(1, 2, d = 99, ext = None)
a = 1 b =2 c = 0 d = 99 kw = {'ext':None}
"""

# post请求介绍
"""
HTTP协议规定post提交的数据必须放在消息主体中，但是协议并没有规定必须使用什么编码方式。服务端通过是根据请求头中的Content-Type字段来获知请求中的消息主体是用何种方式进行编码，再对消息主体进行解析。具体的编码方式包括

1. application/x-www-form-urlencoded 
   最常见post提交数据的方式，以form表单形式提交数据。
2. application/json 
   以json串提交数据。
3. multipart/form-data 
   一般使用来上传文件。
"""
def loginByPostForm(name,**kwargs):
    headers = {
        "Host": "192.168.12.24",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Referer": "http://192.168.12.24/",  # 必须带这个参数，不然会报错
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36",
             }
    url = "http://192.168.12.24/login"
    # form_data = {"data": '{"result": {"model": "Homepage", "action": "BuildClass", "parameters": {"id": -6}}}'}
    form_data = "username=" + name + "&password=4342b2e3478c53a5d080f252c1fa06b6&encrypted=true&loginType=Normal&tenant=&captcha=";
    results = requests.post(url, data=form_data, headers=headers).json()
    print(results)

def loginByPostJson(name,**kwargs):
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Referer": "http://jinbao.pinduoduo.com/index?page=5",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    url = "http://jinbao.pinduoduo.com/network/api/common/goodsList"
    pyload = {"keyword": "", "sortType": 0, "withCoupon": 0, "categoryId": 16, "pageNumber": 1, "pageSize": 60}
    response = requests.post(url, data=json.dumps(pyload), headers=headers).text
    print(response)

def postMultipart():
    url = 'http://httpbin.org/post'
    files = {'file': open('report.txt', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)

def getTest():
    headers = {
        "Content-Type": "application/json; charset=UTF-8",
        "Referer": "http://jinbao.pinduoduo.com/index?page=5",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36",
    }
    url = 'http://192.168.12.24/users/sysadmin/loginType'
    # params = {“wd”: “股票”}
    # 带参数
    # response = requests.get(url=url, params=params, headers=headers).text
    # 不带参数
    response = requests.get(url=url, headers=headers).text
    print(response)
if __name__ == "__main__":
    loginByPostForm("sysadmin")
    getTest()
